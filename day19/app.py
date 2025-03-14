import streamlit as st
from PIL import Image
import numpy as np

# Define the ASCII characters in increasing order of brightness
ASCII_CHARS = ['@', '#', 'S', '%', '?', '*', '+', ';', ':', ',', '.']

# Function to resize image
def resize_image(image, new_width=100):
    width, height = image.size
    ratio = height / width
    new_height = int(new_width * ratio)
    return image.resize((new_width, new_height))

# Function to convert image to grayscale
def grayscale_image(image):
    return image.convert("L")  # L mode for grayscale

# Function to map pixel value to ASCII character
def pixel_to_ascii(pixel_value):
    return ASCII_CHARS[pixel_value // 25]  # Divide by 25 to map pixel value (0-255) to range of 0-10

# Function to convert image to ASCII
def image_to_ascii(image):
    image = resize_image(image)
    image = grayscale_image(image)
    
    pixels = np.array(image)  # Convert to numpy array
    ascii_art = ""
    
    for pixel_value in pixels:
        for value in pixel_value:
            ascii_art += pixel_to_ascii(value)
        ascii_art += '\n'
    
    return ascii_art

# Streamlit UI
def main():
    st.title("Image to ASCII Art Generator")
    st.write("Upload an image, and get its ASCII art representation!")

    # Upload image file
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])
    
    if uploaded_file is not None:
        # Open the uploaded image
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)

        # Convert image to ASCII art
        ascii_art = image_to_ascii(image)
        
        # Display the ASCII art in the app
        st.text_area("ASCII Art", ascii_art, height=400)

         # Provide an option to download the ASCII art as a .txt file
        ascii_bytes = ascii_art.encode()  # Convert ASCII art to bytes
        st.download_button(
            label="Download ASCII Art",
            data=ascii_bytes,
            file_name="ascii_art.txt",
            mime="text/plain"
        )

if __name__ == "__main__":
    main()
