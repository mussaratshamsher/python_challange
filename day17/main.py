import io
import streamlit as st
import qrcode
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import base64
import urllib.parse
from tempfile import NamedTemporaryFile

# Function to generate QR code in memory (without saving to disk)
def generate_qr_code(data):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=6,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
  
    # Convert the image to BytesIO for in-memory use
    img_byte_arr = io.BytesIO()
    img.save(img_byte_arr, format='PNG')
    img_byte_arr.seek(0)
    return img_byte_arr

# Function to create a PDF with the QR code in memory
def create_pdf(img_byte_arr):
    # Create a temporary file to save the image
    with NamedTemporaryFile(delete=False, suffix=".png") as temp_file:
        img_byte_arr.seek(0)  # Make sure the pointer is at the start of the image
        temp_file.write(img_byte_arr.read())  # Save the image to the temporary file
        temp_file_path = temp_file.name  # Get the path to the temporary file

    # Now create the PDF and embed the image
    buffer = io.BytesIO()
    c = canvas.Canvas(buffer, pagesize=letter)
    
    # Draw the image in the PDF using the temporary file path
    c.drawImage(temp_file_path, 150, 500, width=300, height=300)  # Positioning QR code
    c.save()
    
    buffer.seek(0)
    return buffer

# Function to generate a downloadable link for the PDF
def get_pdf_download_link(pdf_buffer, filename="qrcode.pdf"):
    pdf_base64 = base64.b64encode(pdf_buffer.read()).decode('utf-8')
    href = f'<a href="data:application/pdf;base64,{pdf_base64}" download="{filename}">Click here to download the QR code as PDF</a>'
    return href

# Function to generate shareable social media links
def get_social_share_links(qr_data):
    # WhatsApp share link
    whatsapp_link = f"https://wa.me/?text={urllib.parse.quote(qr_data)}"
    # Facebook share link
    facebook_link = f"https://www.facebook.com/sharer/sharer.php?u={urllib.parse.quote(qr_data)}"
    # Twitter share link
    twitter_link = f"https://twitter.com/intent/tweet?text={urllib.parse.quote(qr_data)}"
    
    return whatsapp_link, facebook_link, twitter_link

# Streamlit app setup
st.set_page_config(page_icon="📱", page_title="QR Code Generator", layout="centered")

# Custom CSS for styling the background and button
# Apply custom CSS to the app
st.markdown("""
    <style>
    /* Gradient background for the whole app with animation */
    .stApp {
        background: linear-gradient(45deg, #4aacf1, #D3CCE3, #2c5781, #070a5d); /* Soft pastel colors */
        background-size: 400% 400%; 
        animation: gradientShift 10s ease infinite; /* Animation for smooth transition */
        min-height: 100vh; /* Ensure the background covers full height */
    }
    /* Keyframe animation for smooth background gradient shifting */
    @keyframes gradientShift {
        0% {
            background-position: 0% 50%;
        }
        50% {
            background-position: 100% 50%;
        }
        100% {
            background-position: 0% 50%;
        }
    }
    /* Custom button styling */
    .stButton>button {
        background: linear-gradient(145deg, #6e7dff, #5560ea); /* Default gradient background */
        color: white;
        font-size: 18px;
        font-weight: bold;
        border-radius: 25px; /* Rounded edges for a modern look */
        height: 50px;
        width: 100%;
        border: none;
        cursor: pointer;
        box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1); /* Subtle shadow effect */
        transition: all 0.3s ease; /* Smooth transition for hover effect */
    }
    /* Hover effect */
    .stButton>button:hover {
            color: white; important!
        background: linear-gradient(145deg, #5560ea, #6e7dff); /* Reversed gradient on hover */
        box-shadow: 4px 4px 20px rgba(0, 0, 0, 0.2); /* Enhanced shadow on hover */
        transform: translateY(-4px); /* Slightly lift the button on hover */
    }
    /* Active effect */
    .stButton>button:active {
          color: white; important!   
        transform: translateY(2px); /* Slightly depress the button when clicked */
        box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.1); /* Less shadow on click */
    }
        /* Style for download button */
    .stDownloadButton>button {
        background: linear-gradient(145deg, #6e7dff, #5560ea); /* Gradient background */
        color: white;
        font-size: 16px;
        font-weight: bold;
        border-radius: 50px; /* Rounded corners */
        height: 50px;
        width: 100%;
        border: none;
        cursor: pointer;
        box-shadow: 2px 2px 15px rgba(0, 0, 0, 0.1); /* Shadow effect */
        transition: all 0.3s ease; /* Smooth transition for hover effect */
        text-align: center;
    }

    /* Hover effect for download button */
    .stDownloadButton>button:hover {
        background: linear-gradient(145deg, #5560ea, #6e7dff); /* Reverse gradient */
        box-shadow: 4px 4px 20px rgba(0, 0, 0, 0.2); /* Enhanced shadow */
        transform: translateY(-5px); /* Lift button on hover */
    }

    /* Active effect for download button */
    .stDownloadButton>button:active {
        transform: translateY(2px); /* Depress button when clicked */
        box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.1); /* Subtle shadow on click */
    }             
    </style>
""", unsafe_allow_html=True)

# Streamlit app
st.title("📱🔗 QR Code Generator")

# Input text or URL for QR code
input_data = st.text_input("Enter the text, URL, or message:")

# When the button is clicked, generate the QR code
if st.button("Generate QR Code"):
    if input_data:
        # Generate QR code
        img = generate_qr_code(input_data)
        
         # Create a 2-column layout for the QR code and social media buttons
        col1, col2 = st.columns([1, 1])
        
        with col1:
            # Display the generated QR code
            st.image(img, caption="Your QR Code", use_column_width=True)
        
        with col2:
            # Create the shareable links for social media
            whatsapp_link, facebook_link, twitter_link = get_social_share_links(input_data)
            
            # Display the share buttons 
                 
            st.markdown(f'<a href="{whatsapp_link}" target="_blank"><button style="background-color:#1da1f2; color:white; font-size:16px; border-radius:8px; padding:10px; width: 100%;">Share on WhatsApp</button></a>', unsafe_allow_html=True)
            st.markdown(f'<a href="{facebook_link}" target="_blank"><button style="background-color:#1da1f2; color:white; font-size:16px; border-radius:8px; padding:10px; width: 100%;">Share on Facebook</button></a>', unsafe_allow_html=True)
            st.markdown(f'<a href="{twitter_link}" target="_blank"><button style="background-color:#1da1f2; color:white; font-size:16px; border-radius:8px; padding:10px; width: 100%;">Share on Twitter</button></a>', unsafe_allow_html=True)
           
            # Download button with custom styling
            st.markdown('<div class="stDownloadButton">', unsafe_allow_html=True)
            st.download_button(label="Download QR Code Image", data=img, file_name="qrcode.png", mime="image/png",use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)

                    # Create the PDF with the QR code in memory
        pdf_buffer = create_pdf(img)
        
        # Provide a download link for the PDF
        st.markdown(get_pdf_download_link(pdf_buffer), unsafe_allow_html=True)


    else:
        st.error("Please enter some text, URL, or message.")
