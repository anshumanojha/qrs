import streamlit as st
import random

def generate_question():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operator = random.choice(['+', '-', '*'])
    question = f"{num1} {operator} {num2}"
    answer = eval(question)
    return question, answer

def main():
    st.title("Math Quiz Game")
    st.sidebar.header("Settings")

    # Set difficulty level
    difficulty = st.sidebar.selectbox("Select Difficulty", ["Easy", "Medium", "Hard"])

    if difficulty == "Easy":
        num_questions = 5
    elif difficulty == "Medium":
        num_questions = 10
    else:
        num_questions = 15

    questions_and_answers = []  # To store all questions and correct answers
    score = 0

    for _ in range(num_questions):
        question, correct_answer = generate_question()
        questions_and_answers.append((question, correct_answer))

    for i, (question, _) in enumerate(questions_and_answers):
        user_answer = st.text_input(f"{i + 1}. What is the answer to {question}?")

    st.write("Your final score is:", score)

    # Button to submit answers and display correct answers
    if st.button("Submit Answers"):
        st.write("Correct Answers:")
        for i, (_, correct_answer) in enumerate(questions_and_answers):
            st.write(f"{i + 1}. {correct_answer}")

if __name__ == "__main__":
    main()
