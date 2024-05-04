import streamlit as st
import cv2
from PIL import Image
import numpy as np

st.title("Image Blur")

upload_img = st.file_uploader("Choose an image",type=["jpg", "png", "jpeg"])

if upload_img is not None:
    img = Image.open(upload_img)
    st.image(img,caption="Image uploaded")

    img_array = np.array(img)
    img = cv2.cvtColor(img_array,cv2.COLOR_RGB2BGR)

    blur_amount = st.slider("How much do you want the image to be blur:",min_value=1,max_value=199,value=9,step=2)

    blur_img = cv2.blur(img,(blur_amount,blur_amount))
    blur2rgb = cv2.cvtColor(blur_img,cv2.COLOR_BGR2RGB)

    blur2pil = Image.fromarray(blur2rgb)

    st.image(blur2pil,caption="Blur Image")

