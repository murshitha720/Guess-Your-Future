import pandas as pd
import random

# Define interest to career mapping
interest_career_map = {
    "coding": "Software Developer",
    "business": "Business Analyst",
    "biology": "Biotechnologist",
    "art": "Graphic Designer",
    "writing": "Content Writer",
    "finance": "Financial Analyst",
    "teaching": "Teacher",
    "networking": "Network Engineer",
    "psychology": "Counselor",
    "marketing": "Digital Marketer"
}

# Define aptitude types mapped to careers
aptitude_career_map = {
    "logical": ["Software Developer", "Financial Analyst", "Business Analyst", "Network Engineer"],
    "creative": ["Graphic Designer", "Content Writer", "Digital Marketer"],
    "scientific": ["Biotechnologist"],
    "interpersonal": ["Teacher", "Counselor", "Digital Marketer"],
    "analytical": ["Financial Analyst", "Business Analyst", "Biotechnologist"]
}

# Possible aptitude types
aptitude_types = list(aptitude_career_map.keys())

data = []
interests = list(interest_career_map.keys())

for _ in range(80):
    interest = random.choice(interests)
    career = interest_career_map[interest]

    # Pick an aptitude type that matches the career
    matching_aptitudes = [apt for apt, careers in aptitude_career_map.items() if career in careers]
    aptitude_type = random.choice(matching_aptitudes)

    row = {
        "math": random.randint(1, 5),
        "science": random.randint(1, 5),
        "english": random.randint(1, 5),
        "communication": random.randint(1, 5),
        "programming": random.randint(1, 5),
        "interest": interest,
        "aptitude_type": aptitude_type,
        "career": career
    }
    data.append(row)

# Save to CSV
df = pd.DataFrame(data)
df.to_csv("dataset.csv", index=False)


