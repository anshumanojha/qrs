import streamlit as st
import qrcode
from PIL import Image
import io
import sys
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

pd.set_option('mode.use_inf_as_na', True)
print(sys.executable)

def generate_qr_code(linkedin_url):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=1,
        border=0,
    )
    qr.add_data(linkedin_url)
    qr.make(fit=True)
    
    img_byte_array = io.BytesIO()
    qr.make_image(fill_color="black", back_color="white").save(img_byte_array)
    return img_byte_array.getvalue()

def predict_next_month_revenue(monthly_data):
    # Prepare the input data
    X = np.arange(1, len(monthly_data) + 1).reshape(-1, 1)
    y = np.array(monthly_data).reshape(-1, 1)

    # Assuming a basic linear regression model for demonstration
    model = LinearRegression()
    model.fit(X, y)

    # Predict the next month
    next_month_data = np.array([len(monthly_data) + 1]).reshape(-1, 1)
    predicted_revenue = model.predict(next_month_data)[0][0]

    return predicted_revenue

def plot_revenue_graph(months, given_revenue, predicted_revenue):
    plt.figure(figsize=(10, 5))
    sns.lineplot(x=months, y=given_revenue, label="Given Revenue", marker="o")
    sns.lineplot(x=[months[-1], months[-1] + 1], y=[given_revenue[-1], predicted_revenue], label="Predicted Revenue", marker="o", linestyle="--")
    plt.title("Given and Predicted Revenue Over Time")
    plt.xlabel("Month")
    plt.ylabel("Revenue")
    plt.legend()
    return plt

def main():
    st.title("Data Analyst Resume and Future Revenue Prediction")

    # User Input: LinkedIn URL
    linkedin_url = st.text_input("Enter your LinkedIn URL:")
    
    if linkedin_url:
        # Display the entered LinkedIn URL
        st.write(f"LinkedIn URL: {linkedin_url}")

        # Generate and display the QR code
        qr_code_image = generate_qr_code(linkedin_url)
        st.image(Image.open(io.BytesIO(qr_code_image)), caption="Scan QR Code to visit LinkedIn profile", width=100)

    # Personal Information
    st.header("Personal Information")
    st.write("Name: John Doe")
    st.write("Email: john.doe@example.com")
    st.write("Phone: +1234567890")

    # Revenue Prediction
    st.header("Revenue Prediction")

    # User Input: Enter monthly revenue for different months
    monthly_data = []

    # Use st.beta_columns to create a side-by-side layout
    col1, col2, col3, col4 = st.beta_columns(4)

    for i in range(1, 13):  # Assuming predictions for 12 months
        # Use colX.number_input for each column
        with col1:
            revenue = st.number_input(f"Month {i}", value=0.0, step=0.01, format="%f", key=f"revenue_{i}")
            monthly_data.append(revenue)

    if len(monthly_data) >= 2:
        # Predict the next month's revenue
        predicted_revenue = predict_next_month_revenue(monthly_data)

        st.write("Predicted Revenue for the Next Month:")
        st.write(predicted_revenue)

        # Create a graph for given revenue and predicted revenue
        months = np.arange(1, len(monthly_data) + 2)
        given_revenue = monthly_data + [predicted_revenue]

        # Plot graphs
        st.pyplot(plot_revenue_graph(months, given_revenue, predicted_revenue))

if __name__ == "__main__":
    main()
