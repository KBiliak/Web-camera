import streamlit as st
from PIL import Image

with st.expander("Start camera"):

# start the camera
    camera_image = st.camera_input("Camera")


if camera_image:
    # create a pillow img inst
    img = Image.open(camera_image)

    # convert the pillow img to grayscale
    gray_img = img.convert("L")

    # render the greyscale img on the web page
    st.image(gray_img)