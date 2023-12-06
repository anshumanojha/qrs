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

    score = 0
    current_question = 0

    while current_question < num_questions:
        question, correct_answer = generate_question()

        user_answer = st.text_input(f"What is the answer to {question}?", key=f"answer_{current_question}")
        submitted = False  # Variable to track whether the answer is submitted

        if st.button("Submit Answer"):
            submitted = True  # Set submitted to True when the button is pressed
            if user_answer:
                user_answer = float(user_answer)
                if user_answer == correct_answer:
                    st.success("Correct!")
                    score += 1
                else:
                    st.error(f"Wrong! The correct answer is {correct_answer}")
            else:
                st.warning("Please enter an answer.")

        if submitted:  # Show the result only if the answer is submitted
            st.write(f"Your current score is: {score}/{current_question + 1}")

            # Button to move to the next question
            if current_question < num_questions - 1:
                if st.button("Next Question"):
                    current_question += 1
            else:
                st.write(f"Your final score is: {score}/{num_questions}")

if __name__ == "__main__":
    main()
