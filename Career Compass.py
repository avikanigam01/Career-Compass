# Student Career Recommendation System
#Features: Personality Assessment,Career Recommendation
def get_valid_inputs(question):
    print(question)
    while True:
        try:
            choice=int(input("Enter your choice:\n"))
            if choice in[1,2,3,4]:
                return choice
            else:
                print("❌ Invalid input. Please enter a number between 1 and 4.")
        except  ValueError:
            print("❌ Invalid input. Please enter a number between 1 and 4.")

def get_user_info():
    activity = get_valid_inputs("Which activity sounds most exciting(select number):"
                         " 1. Building apps and software,\n"
                         " 2. Analyzing data and finding patterns,\n"
                         " 3. Designing creative things,\n "
                         "4. Managing people and projects\n")

    subject = get_valid_inputs("\nWhich subject do you enjoy the most?(select number):\n"
                        "1. Computer Science\n"
                        "2. Mathematics\n"
                        "3. Arts\n"
                        "4. Business Studies\n")

    enjoy = get_valid_inputs("\nWhat do you enjoy most?(select number)\n"
                      "1. Solving problems\n"
                      "2. Working with data\n"
                      "3. Creating designs\n"
                      "4. Leading teams\n")

    environment = get_valid_inputs("\nWhat type of work environment do you prefer?(select number)\n"
                            "1. Technology\n"
                            "2. Data and research\n"
                            "3. Creative projects\n"
                            "4. Business and management\n")

    interest = get_valid_inputs("\nIf given a free weekend, what would you choose?(select number)\n"
                        "1. Build a project\n"
                        "2. Solve puzzles and analyze trends\n"
                        "3. Create content or designs\n"
                        "4. Launch a startup or organize a large event\n")

    return activity, subject, enjoy, environment, interest

def recommendation(activity, subject, enjoy, environment, interest):
    career_scores = {
        "Software & Technology": 0,
        "Data & AI": 0,
        "Design & Creativity": 0,
        "Management & Business": 0
    }
    if activity == 1:  # Building apps and software
        career_scores["Software & Technology"] += 2
        career_scores["Data & AI"] += 1

    elif activity == 2:  # Analyzing data and patterns
        career_scores["Data & AI"] += 2
        career_scores["Software & Technology"] += 1

    elif activity == 3:  # Designing creative things
        career_scores["Design & Creativity"] += 2

    elif activity == 4:  # Managing people and projects
        career_scores["Management & Business"] += 2

    if subject == 1:  # Computer Science
        career_scores["Software & Technology"] += 2
        career_scores["Data & AI"] += 1

    elif subject == 2:  # Mathematics
        career_scores["Data & AI"] += 2
        career_scores["Software & Technology"] += 1

    elif subject == 3:  # Arts
        career_scores["Design & Creativity"] += 2

    elif subject == 4:  # Business Studies
        career_scores["Management & Business"] += 2

    if enjoy == 1:  # Solving problems
        career_scores["Software & Technology"] += 2
        career_scores["Data & AI"] += 1

    elif enjoy == 2:  # Working with data
        career_scores["Data & AI"] += 2
        career_scores["Software & Technology"] += 1

    elif enjoy == 3:  # Creating designs
        career_scores["Design & Creativity"] += 2

    elif enjoy == 4:  # Leading teams
        career_scores["Management & Business"] += 2

    if environment == 1:  # Technology
        career_scores["Software & Technology"] += 2
        career_scores["Data & AI"] += 1

    elif environment == 2:  # Data and Research
        career_scores["Data & AI"] += 2
        career_scores["Software & Technology"] += 1

    elif environment == 3:  # Creative Projects
        career_scores["Design & Creativity"] += 2

    elif environment == 4:  # Business and Management
        career_scores["Management & Business"] += 2

    if interest == 1:  # Build a project
        career_scores["Software & Technology"] += 2
        career_scores["Data & AI"] += 1

    elif interest == 2:  # Solve puzzles and analyze trends
        career_scores["Data & AI"] += 2
        career_scores["Software & Technology"] += 1

    elif interest == 3:  # Create content or designs
        career_scores["Design & Creativity"] += 2

    elif interest == 4:  # Plan a startup or event
        career_scores["Management & Business"] += 2
        career_scores["Design & Creativity"] += 1

    best_category = max(career_scores, key=career_scores.get)
    return best_category, career_scores

personality = {
    "Software & Technology": {
        "title": "🚀 The Builder",
        "description": "You enjoy creating solutions, building products, and solving technical challenges."
    },
    "Data & AI": {
        "title": "📊 The Analyst",
        "description": "You love working with data, finding patterns, and making logical decisions."
    },
    "Design & Creativity": {
        "title": "🎨 The Creator",
        "description": "You thrive on creativity, aesthetics, and turning ideas into engaging experiences."
    },
    "Management & Business": {
        "title": "👑 The Leader",
        "description": "You enjoy organizing, planning, leading teams, and driving projects forward."
    }
}

career_paths = {
    "Software & Technology": [
        "Software Engineer",
        "Backend Developer",
        "Frontend Developer",
        "Full Stack Developer",
        "Mobile App Developer",
        "DevOps Engineer",
        "Cloud Engineer",
        "Cybersecurity Engineer"
    ],

    "Data & AI": [
        "AI Engineer",
        "Machine Learning Engineer",
        "Data Scientist",
        "Data Analyst",
        "Business Intelligence Analyst",
        "Research Engineer",
        "Computer Vision Engineer",
        "NLP Engineer"
    ],

    "Design & Creativity": [
        "UI/UX Designer",
        "Graphic Designer",
        "Product Designer",
        "Motion Designer",
        "Brand Designer",
        "Content Creator",
        "Video Editor",
        "Creative Director"
    ],

    "Management & Business": [
        "Product Manager",
        "Project Manager",
        "Business Analyst",
        "Operations Manager",
        "Entrepreneur",
        "Startup Founder",
        "Marketing Manager",
        "Consultant"
    ]
}
advice = {
    "Software & Technology":
        "Keep building projects, practice coding daily, and maintain a strong GitHub portfolio. Learning DSA and web development will make you internship-ready.",

    "Data & AI":
        "Strengthen your Python, statistics, and machine learning skills. Work on data analysis projects and participate in Kaggle competitions.",

    "Design & Creativity":
        "Build a visually appealing portfolio, master design tools like Figma, and create case studies to showcase your creativity.",

    "Management & Business":
        "Develop leadership and communication skills, learn project management fundamentals, and work on entrepreneurial or business-oriented projects."
}

roadmaps={
"Software & Technology": [
        "Python",
        "Git & GitHub",
        "Data Structures",
        "Databases",
        "Web Development",
        "Projects"
    ],

    "Data & AI": [
        "Python",
        "NumPy",
        "Pandas",
        "Machine Learning",
        "Deep Learning",
        "Generative AI"
    ],

    "Design & Creativity": [
        "Figma",
        "UI Principles",
        "UX Research",
        "Wireframing",
        "Prototyping",
        "Portfolio Building"
    ],

    "Management & Business": [
        "Communication",
        "Project Planning",
        "Leadership",
        "Finance Basics",
        "Marketing",
        "Strategy"
    ]

}
# Internship readiness suggestions
internship_readiness = {
    "Software & Technology": {
        "score": "High",
        "tips": [
            "Build at least 3 real-world projects",
            "Learn Git & GitHub thoroughly",
            "Practice Data Structures & Algorithms",
            "Deploy one full-stack application",
            "Create a professional GitHub portfolio"
        ]
    },

    "Data & AI": {
        "score": "High",
        "tips": [
            "Master Python fundamentals",
            "Learn NumPy, Pandas, and SQL",
            "Build end-to-end Machine Learning projects",
            "Create projects using Generative AI or LLMs",
            "Publish notebooks and code on GitHub"
        ]
    },

    "Design & Creativity": {
        "score": "Moderate to High",
        "tips": [
            "Build a strong Figma portfolio",
            "Create detailed UI/UX case studies",
            "Learn design systems and accessibility",
            "Collaborate on real products",
            "Show complete design processes, not just final screens"
        ]
    },

    "Management & Business": {
        "score": "Moderate",
        "tips": [
            "Develop communication and presentation skills",
            "Learn Agile and Scrum methodologies",
            "Build leadership experience through projects",
            "Understand product strategy and business models",
            "Gain practical experience through internships or clubs"
        ]
    }
}

# Approximate educational salary ranges (India)
salary_snapshot = {
    "Software & Technology": {
        "Software Engineer": "₹5–12 LPA",
        "Backend Developer": "₹6–14 LPA",
        "Full Stack Developer": "₹6–15 LPA",
        "Cloud Engineer": "₹7–16 LPA"
    },

    "Data & AI": {
        "Data Analyst": "₹5–10 LPA",
        "Data Scientist": "₹8–18 LPA",
        "Machine Learning Engineer": "₹8–20 LPA",
        "AI Engineer": "₹10–25 LPA"
    },

    "Design & Creativity": {
        "UI/UX Designer": "₹4–9 LPA",
        "Product Designer": "₹6–14 LPA",
        "Graphic Designer": "₹3–8 LPA",
        "Motion Designer": "₹4–10 LPA"
    },

    "Management & Business": {
        "Business Analyst": "₹5–10 LPA",
        "Product Manager": "₹10–20 LPA",
        "Operations Manager": "₹6–12 LPA",
        "Marketing Manager": "₹5–12 LPA"
    }
}

# Estimated learning duration
learning_duration = {
    "Software & Technology": {
        "Python Fundamentals": "1 month",
        "Git & GitHub": "1 week",
        "Data Structures": "2–3 months",
        "Web Development": "2 months",
        "Portfolio Projects": "Ongoing"
    },

    "Data & AI": {
        "Python": "1 month",
        "NumPy & Pandas": "3 weeks",
        "Machine Learning": "2 months",
        "Deep Learning": "2 months",
        "Generative AI": "1–2 months"
    },

    "Design & Creativity": {
        "Figma": "2 weeks",
        "UI Design": "1 month",
        "UX Research": "3 weeks",
        "Portfolio Building": "Ongoing",
        "Case Studies": "1 month"
    },

    "Management & Business": {
        "Communication Skills": "Ongoing",
        "Project Management": "1 month",
        "Agile & Scrum": "2 weeks",
        "Business Strategy": "1 month",
        "Leadership Development": "Ongoing"
    }
}
def show_result():
    print("\n================================\n")
    print("\n🚀 CAREER COMPASS 🚀")
    print("\n Discover Your Ideal Career Path\n")
    print("\n================================\n")
    print("\n⚠️ Note:")
    print("This recommendation is based on your responses and is intended for educational purposes only.")
    activity, subject, enjoy, environment, interest = get_user_info()
    best_category, career_scores = recommendation(
        activity, subject, enjoy, environment, interest
    )
    print("📝 Assessment Complete!")
    print("\n--------------------------------\n")
    print("🧠 Your Personality Type:")
    print(personality[best_category]["title"])
    print(personality[best_category]["description"])
    print("\n--------------------------------\n")
    print("\n🎉 Congratulations!")
    print(f"Based on your answers, {best_category} appears to be your strongest fit.")

    print("\n📊 Career Match Scores:\n")
    for category, score in career_scores.items():
        bar = "█" * score
        print(f"{category:<25} {bar} ({score})")

    print("\n--------------------------------\n")
    print("\n💼 Suggested Career Paths:\n")
    for career in career_paths[best_category]:
        print("-", career)
    print("\n--------------------------------\n")
    print(f"⭐ Readiness Level: {internship_readiness[best_category]['score']}")
    print("\nHow to improve:")
    for tip in internship_readiness[best_category]["tips"]:
        print("-", tip)
    print("\n--------------------------------\n")
    print("\nSalary Snapshot for the recommended career: \n")
    for role, salary in salary_snapshot[best_category].items():
        print(f"{role}: {salary}")
    print("\n--------------------------------\n")
    print("\n⏳ Estimated Learning Duration:\n")
    for skill, duration in learning_duration[best_category].items():
        print(f"{skill}: {duration}")
    print("\n--------------------------------\n")
    print("\n Recommended Roadmap: \n")
    for step in roadmaps[best_category]:
        print("-", step)
    print("\n================================\n")
    print("\n💡 Final Advice:")
    print(advice[best_category])
    print("\n🚀 Keep learning, keep building, and keep growing!")
    print("Your future career is shaped by consistent effort and real-world projects.")
    print("Designed and Developed by Avika Nigam ❤️")
    print("\n================================\n")

show_result()

while True:
    again = input("\nDo you want to try again? (yes/no): ").lower()
    if again == "yes":
        show_result()
    else:
        print("Thank you for using Career Compass! 👋")
        break

