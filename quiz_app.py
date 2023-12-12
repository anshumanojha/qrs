import streamlit as st
import qrcode
from PIL import Image
import io
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

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
    # Replace NaN and Inf values with zeros
    monthly_data = np.nan_to_num(monthly_data)

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

    # User Input: Enter all revenues in a single text box
    revenue_input = st.text_input("Enter monthly revenues (comma-separated):", key="revenue_input")
    
    given_monthly_data = []

    if revenue_input:
        # Split the input values by comma and convert to float
        given_monthly_data = [float(value.strip()) for value in revenue_input.split(',')]

        # Display the entered revenues for each month
        for i, revenue in enumerate(given_monthly_data, start=1):
            st.write(f"Month {i} Revenue: {revenue}")

        if len(given_monthly_data) >= 2:
            # Predict the next month's revenue
            predicted_revenue = predict_next_month_revenue(given_monthly_data)

            st.write("Predicted Revenue for the Next Month:")
            st.write(predicted_revenue)

            # Plotting a time graph for entered and predicted revenues
            months = np.arange(1, len(given_monthly_data) + 2)
            all_revenues = given_monthly_data + [predicted_revenue]

            plt.figure(figsize=(10, 5))
            plt.plot(months, all_revenues, marker='o', label='Given and Predicted Revenue')
            plt.title("Given and Predicted Revenue Over Time")
            plt.xlabel("Month")
            plt.ylabel("Revenue")
            plt.legend()
            st.pyplot(plt)

if __name__ == "__main__":
    main()
