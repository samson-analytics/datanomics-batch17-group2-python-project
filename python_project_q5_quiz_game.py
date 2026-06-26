# 5)	Create a basic quiz game that:
# •	Contains a list of 5–10 questions stored in a dictionary (or list of dictionaries [{}, {}] ).
# •	Ask the user each question and records their answers.
# •	At the end, displays:
# o	 The user's score (e.g., 7/10)
# o	Correct answers for any questions they got wrong

questions = [
    {"question": "What is 2 + 2?", "answer": "4"},
    {"question": "What is the capital of Italy?", "answer": "Rome"},
    {"question": "What color is the sky?", "answer": "Blue"},
    {"question": "What is 5 + 3?", "answer": "8"},
    {"question": "What language are we learning?", "answer": "Python"}
]

score = 0
wrong_answers = []

for question in questions:
    user_answer = input(question["question"] + " ")

    if user_answer.lower() == question["answer"].lower():
        print("Correct")
        score += 1
    else:
        print("Wrong. The correct answer is", question["answer"])
        wrong_answers.append(question)

print("\nFinal Score:", score, "/", len(questions))

print("\nCorrect answers for questions you got wrong:")
for question in wrong_answers:
    print(question["question"])
    print("Correct answer:", question["answer"])