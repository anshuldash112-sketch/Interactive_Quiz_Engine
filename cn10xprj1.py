QUESTIONS = [
    {
        "question": "Which built-in data type in Python stores key-value pairs?",
        "A": "list", "B": "tuple", "C": "dict", "D": "set",
        "answer": "C",
    },
    {
        "question": "What does the len() function return for 'hello'?",
        "A": "4", "B": "5", "C": "6", "D": "Error",
        "answer": "B",
    },
    {
        "question": "Which keyword is used to define a function in Python?",
        "A": "func", "B": "function", "C": "define", "D": "def",
        "answer": "D",
    },
    {
        "question": "Which collection is ordered and mutable?",
        "A": "tuple", "B": "list", "C": "string", "D": "int",
        "answer": "B",
    },
    {
        "question": "What is the output of bool(0)?",
        "A": "True", "B": "False", "C": "None", "D": "0",
        "answer": "B",
    },
    {
        "question": "Which operator performs floor division in Python?",
        "A": "/", "B": "%", "C": "//", "D": "**",
        "answer": "C",
    },
    {
        "question": "How do you start a comment in Python?",
        "A": "//", "B": "/*", "C": "#", "D": "--",
        "answer": "C",
    },
    {
        "question": "Which method removes and returns the last item of a list by default?",
        "A": "pop()", "B": "remove()", "C": "discard()", "D": "trim()",
        "answer": "A",
    },
]
score = 0
total = len(QUESTIONS)

print("Welcome to the Python Quiz!")

for i in range(total):
    item = QUESTIONS[i]
    print()
    print("Question", i + 1, "of", total, ":", item["question"])
    print("  A.", item["A"])
    print("  B.", item["B"])
    print("  C.", item["C"])
    print("  D.", item["D"])
 
    while True:
        choice = input("Enter A, B, C, or D: ").strip().upper()
        if choice in ["A", "B", "C", "D"]:
            break
        print("Invalid choice! Please type A, B, C, or D.")

    if choice == item["answer"]:
        print("Correct!")
        score = score + 1
    else:
        print("Wrong! The right answer was", item["answer"])

percentage = (score / total) * 100
print()
print("Quiz Over!")
print("Your Score:", score, "/", total)
print("Percentage:", round(percentage, 1), "%")