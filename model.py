import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import joblib

# Load dataset
df = pd.read_csv("dataset.csv")

# Encode categorical columns: 'interest', 'aptitude_type', and 'career'
label_encoders = {}
for column in ['interest', 'aptitude_type', 'career']:
    le = LabelEncoder()
    df[column] = le.fit_transform(df[column])
    label_encoders[column] = le

# Define features and target
X = df[['math', 'science', 'english', 'communication', 'programming', 'interest', 'aptitude_type']]
y = df['career']

# Split the dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save model and encoders
joblib.dump(model, "career_guidance_model.pkl")
joblib.dump(label_encoders['interest'], "interest_encoder.pkl")
joblib.dump(label_encoders['aptitude_type'], "aptitude_type_encoder.pkl")
joblib.dump(label_encoders['career'], "career_encoder.pkl")


