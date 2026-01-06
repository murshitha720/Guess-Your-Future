import pandas as pd
import random

# Define mapping from interest to career and extended info
career_data1 = {
"Software Developer": {
        "career": "Software Developer",
        "overview": "Designs and builds software applications and systems.",
        "skills": "Programming, Problem Solving, Debugging, Software Design",
        "study_next": "Data Structures, Algorithms, Web/Software Development",
        "resources": "https://www.freecodecamp.org/, https://www.codecademy.com/"
    },
    "Business Analyst": {
        "career": "Business Analyst",
        "overview": "Analyzes business needs and suggests solutions to improve processes.",
        "skills": "Analytical Thinking, Communication, Excel, SQL",
        "study_next": "Business Analysis, Data Analysis, Project Management",
        "resources": "https://www.coursera.org/, https://www.edx.org/"
    },
    "Biotechnologist":{
        "career": "Biotechnologist",
        "overview": "Works with living organisms to develop products and technologies.",
        "skills": "Lab Skills, Molecular Biology, Research, Data Analysis",
        "study_next": "Genetics, Biochemistry, Microbiology",
        "resources": "https://www.khanacademy.org/, https://www.coursera.org/"
    },
    "Graphic Designer": {
        "career": "Graphic Designer",
        "overview": "Creates visual concepts to communicate ideas.",
        "skills": "Creativity, Adobe Suite, Typography, Color Theory",
        "study_next": "Graphic Design, UI/UX, Visual Communication",
        "resources": "https://www.canva.com/learn/, https://www.udemy.com/"
    },
    "Content Writer": {
        "career": "Content Writer",
        "overview": "Writes engaging content for websites, blogs, and marketing.",
        "skills": "Grammar, SEO, Creativity, Research",
        "study_next": "Content Strategy, Digital Marketing, Copywriting",
        "resources": "https://neilpatel.com/blog/, https://www.hubspot.com/"
    },
    "Financial Analyst": {
        "career": "Financial Analyst",
        "overview": "Evaluates financial data to help companies make decisions.",
        "skills": "Excel, Accounting, Financial Modeling, Statistics",
        "study_next": "Finance, Economics, Investment Analysis",
        "resources": "https://www.investopedia.com/, https://cfainstitute.org/"
    },
    "Teacher": {
        "career": "Teacher",
        "overview": "Educates and inspires students in various subjects.",
        "skills": "Communication, Patience, Planning, Subject Mastery",
        "study_next": "Educational Psychology, Curriculum Design, Pedagogy",
        "resources": "https://www.edutopia.org/, https://www.teachthought.com/"
    },
    "Network Engineer": {
        "career": "Network Engineer",
        "overview": "Designs and maintains computer networks.",
        "skills": "Networking, Security, Troubleshooting, Scripting",
        "study_next": "CCNA, Network Security, Cloud Infrastructure",
        "resources": "https://www.cisco.com/, https://networklessons.com/"
    },
    "Counselor": {
        "career": "Counselor",
        "overview": "Helps individuals deal with emotional and mental challenges.",
        "skills": "Empathy, Listening, Critical Thinking, Ethics",
        "study_next": "Psychotherapy, Human Behavior, Mental Health",
        "resources": "https://www.psychologytoday.com/, https://www.coursera.org/"
    },
    "Digital Marketer": {
        "career": "Digital Marketer",
        "overview": "Promotes products/services through digital channels.",
        "skills": "SEO, SEM, Analytics, Social Media Marketing",
        "study_next": "Digital Marketing, Consumer Behavior, Branding",
        "resources": "https://www.google.com/skillshop/, https://moz.com/"
    },
    "Doctor": {
        "career":"Doctor",
        "overview":"Diagnoses and treats illnesses,improves patient health and wellbeing.",
        "skills":"Biology,Empathy,Communication",
        "study_next":"Anatomy,Physiology,Medical School",
        "resources":"https://www.khanacademy.org/science/biology"
    }
}

# Generate dataset
data1 = []
interests1 = list(career_data1.keys())

for _ in range(80):
    interest = random.choice(interests1)
    details = career_data1[interest]

    row = {
        "math": random.randint(1, 5),
        "science": random.randint(1, 5),
        "english": random.randint(1, 5),
        "communication": random.randint(1, 5),
        "programming": random.randint(1, 5),
        "interest": interest,
        "aptitude": random.randint(1, 5),
        "career1": details["career"],
        "career_overview": details["overview"],
        "skills_to_develop": details["skills"],
        "what_to_study_next": details["study_next"],
        "recommended_resources": details["resources"]
    }
    data1.append(row)

# Save to CSV
df = pd.DataFrame(data1)
df.to_csv("question.csv", index=False)

