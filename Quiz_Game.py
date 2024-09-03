questions=[
    {
        "prompt":"Who was the first chairman of ISRO?",
        "options":["A. Dr. Vikram Sarabhai","B. Dr. A.P.J. Abdul Kalam","C. Dr. K. Sivan","D.  Dr. Satish Dhawan"],
        "answer":"A"
    },
    {
        "prompt":"What is the full form of GSLV?",
        "options":["A. Geostationary Satellite Launch Vehicle","B. Global Satellite Launch Vehicle","C. General Satellite Launch Vehicle","D. Geosynchronous Satellite Launch Vehicle"],
        "answer":"D"
    },
    {
        "prompt":"What is the name of the mission aimed at sending Indian astronauts to space?",
        "options":["A. Chandrayaan-3","B. Mangalyaan-2","C. Gaganyaan","D. Shukrayaan"],
        "answer":"C"
    },
    {
        "prompt":"What is the purpose of the GSAT series of satellites?",
        "options":["A. Earth observation","B. Communication","C. Navigation","D. Weather forecasting"],
        "answer":"B"
    }
]

def run_quiz(questions):
    score=0
    for question in questions:
        print(question["prompt"])
        for option in question["options"]:
            print(option)
        ans=input("Enter your answer (A,B,C or D):").upper()
        if ans==question["answer"]:
            print("Correct Answer !!!")
            score += 1
        else:
            print("Wrong !!! The correct answer is ", question['answer'])

    print(f"you get {score} as you did {len(questions)} questions correct")

run_quiz(questions)
