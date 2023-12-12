import streamlit as st
import qrcode
from PIL import Image
import io  # Required for converting PilImage to bytes
import sys

print(sys.executable)

def main():
    st.title("Data Analyst Resume")

    # Personal Information
    st.header("Personal Information")
    st.write("Name: John Doe")
    st.write("Email: john.doe@example.com")
    st.write("Phone: +1234567890")

    # LinkedIn QR Code
    linkedin_url = "https://www.linkedin.com/in/johndoe/"
    st.write("LinkedIn: [LinkedIn Profile](https://www.linkedin.com/in/johndoe/)")
    
    # Generate QR Code for LinkedIn
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(linkedin_url)
    qr.make(fit=True)

    # Convert PilImage to bytes
    img_byte_array = io.BytesIO()
    qr.make_image(fill_color="black", back_color="white").save(img_byte_array)
    img_byte_array = img_byte_array.getvalue()

    # Display the QR code using st.image
    st.image(Image.open(io.BytesIO(img_byte_array)), caption="Scan QR Code to visit LinkedIn profile", use_column_width=True)

    # Skills, Tools, Projects, Education, Work Experience (unchanged)

if __name__ == "__main__":
    main()
