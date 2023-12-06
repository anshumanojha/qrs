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

    with st.form("quiz_form"):
        current_question = 0

        # Use a button to submit the form instead of st.form_submit_button
        submit_button = st.form_submit_button("Submit Answer")

        if submit_button:
            question, correct_answer = generate_question()
            user_answer = st.text_input(f"What is the answer to {question}?", key=f"answer_{current_question}")

            if user_answer:
                user_answer = float(user_answer)
                if user_answer == correct_answer:
                    st.success("Correct!")
                    score += 1

                current_question += 1
                st.write(f"Your current score is: {score}/{current_question}")

    st.write(f"Your final score is: {score}/{num_questions}")

if __name__ == "__main__":
    main()
