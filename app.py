from flask import Flask, render_template, request
from question import career_data1
from question_bank import quizzes
import joblib
import numpy as np
import pandas as pd

app = Flask(__name__)

# Load model and encoders
model = joblib.load("career_guidance_model.pkl")
interest_encoder = joblib.load("interest_encoder.pkl")
aptitude_encoder = joblib.load("aptitude_type_encoder.pkl")
career_encoder = joblib.load("career_encoder.pkl")

# Optional: Map careers to details
career_data = pd.read_csv("dataset.csv")
career_explain = career_data1

@app.route("/")
def home():
    return render_template('recent.html')

@app.route("/item")
def item():
    return render_template('item.html')

@app.route("/predict", methods=["GET","POST"])
def predict():
    if request.method == "POST":
        # Get form data
        math = int(request.form.get("math"))
        science = int(request.form.get("science"))
        english = int(request.form.get("english"))
        communication = int(request.form.get("communication"))
        programming = int(request.form.get("programming"))

        # Encode interest text to numeric
        interest_text = request.form.get("interest").lower().strip()

        # Encode interest text to numeric
        aptitude_text = request.form.get("aptitude_type")

        # Encode interest
        if interest_text in interest_encoder.classes_:
            interest_encoded = interest_encoder.transform([interest_text])[0]
        else:
            interest_encoded = 0  # default fallback

        # Encode aptitude_type
        if aptitude_text in aptitude_encoder.classes_:
            aptitude_encoded = aptitude_encoder.transform([aptitude_text])[0]
        else:
            aptitude_encoded = 0

        # Make prediction
        features = np.array([[math, science, english, communication, programming, interest_encoded,aptitude_encoded]])
        prediction = model.predict(features)[0]
        career = career_encoder.inverse_transform([prediction])[0]

    career_info = None
    for career_name,details in career_explain.items():
        if career_name == career:
            career_info ={"overview":details.get("overview",""),
                           "skills": details.get("skills", "").split(","),
                           "study_next":details.get("study_next","").split(","),
                           "resources": details.get("resources", "").split(",")
                           }
            break

    # If still not found, use default
    if not career_info:
        career_info = {
            "overview": "",
            "skills": [],
            "study_next": [],
            "resources": []
        }

    return render_template('result.html', result= career, overview=career_info["overview"],
                               skills=career_info["skills"],
                               study_next=career_info["study_next"],
                               resources=career_info["resources"])

@app.route("/test")
def test_page():
    return render_template("test.html", quizzes=quizzes)

@app.route("/submit_test", methods=["POST"])
def submit_test():
    name = request.form.get("name")
    interest_text = request.form.get("interest").strip()

    scores = {}
    # Calculate category-wise scores
    for category, questions in quizzes.items():
        correct = 0
        for i, q in enumerate(questions):
            user_ans = request.form.get(f"{category}_q{i}")
            if user_ans == q["answer"]:
                correct += 1
        # Scale score (1–5 range)
        score = round((correct / len(questions)) * 5)
        scores[category] = score
    # Ensure all categories have values (default = 2)
    categories = ["math", "science", "english", "communication",
              "programming", "interpersonal", "scientific", "technology"]
    for cat in categories:
        scores.setdefault(cat, 2)
    # Get user interest text
    interest_text = request.form.get("interest", "").strip().lower()
    # Encode interest feature safely
    try:
        interest_value = interest_encoder.transform([interest_text])[0]
    except Exception:
        interest_value = 0  # fallback if unseen interest
    # Create feature vector for model
    features = np.array([[
    scores["math"],
    scores["science"],
    scores["english"],
    scores["communication"],
    scores["programming"],
    scores["interpersonal"],
    scores["scientific"],
    scores["technology"],
    interest_value
    ]])
    # Make prediction
    prediction = model.predict(features)[0]
    career = career_encoder.inverse_transform([prediction])[0]


    # Fetch career data
    career_info = career_explain.get(career, {
        "overview": "",
        "skills": [],
        "study_next": [],
        "resources": []
    })

    return render_template("result.html", result=career,
                           overview=career_info["overview"],
                           skills=career_info["skills"],
                           study_next=career_info["study_next"],
                           resources=career_info["resources"])

if __name__ == "__main__":
    app.run(debug=True)

