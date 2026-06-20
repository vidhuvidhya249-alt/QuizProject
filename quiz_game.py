questions = [
    {
        "question": "Which keyword is used to define a function in Python?",
        "choices": ["A. func", "B. define", "C. def", "D. function"],
        "answer": "C"
    },
    {
        "question": "Which data type stores True or False values?",
        "choices": ["A. int", "B. bool", "C. float", "D. str"],
        "answer": "B"
    },
    {
        "question": "Which symbol is used for comments in Python?",
        "choices": ["A. //", "B. /*", "C. #", "D. --"],
        "answer": "C"
    },
    {
        "question": "Which function is used to display output?",
        "choices": ["A. input()", "B. print()", "C. output()", "D. show()"],
        "answer": "B"
    },
    {
        "question": "What is the extension of a Python file?",
        "choices": ["A. .java", "B. .txt", "C. .python", "D. .py"],
        "answer": "D"
    }
]

score = 0
wrong = 0

print("===== Python Quiz Game =====")

for i, q in enumerate(questions, start=1):
    print(f"\nQuestion {i}: {q['question']}")

    for choice in q["choices"]:
        print(choice)

    user_answer = input("Enter your choice (A/B/C/D): ").upper()

    if user_answer == q["answer"]:
        print("Correct!")
        score += 1
    else:
        print(f"Wrong! Correct Answer: {q['answer']}")
        wrong += 1

# Feedback Section
print("\n===== Quiz Result =====")
print(f"Total Questions : {len(questions)}")
print(f"Correct Answers : {score}")
print(f"Wrong Answers   : {wrong}")

percentage = (score / len(questions)) * 100
print(f"Score Percentage: {percentage:.2f}%")

if percentage >= 80:
    print("Feedback: Excellent Python Knowledge!")
elif percentage >= 60:
    print("Feedback: Good Job! Keep Practicing.")
else:
    print("Feedback: Need More Practice.")
