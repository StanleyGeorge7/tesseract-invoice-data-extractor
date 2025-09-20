import streamlit as st
from PIL import Image
import pandas as pd

from ocr.utils import preprocess_image, extract_text
from ocr.parser import parse_invoice_header_safe, parse_line_items

st.set_page_config(page_title="Invoice OCR App", layout="wide")

st.sidebar.title("Upload Invoice")
uploaded_file = st.sidebar.file_uploader("", type=["png","jpg","jpeg"])


st.markdown(
    """
    <style>
    /* Sidebar background */
    [data-testid="stSidebar"] {
        background-color: #66676a;  /* Blue */
        color: white;
    }

    /* File uploader label */
    [data-testid="stSidebar"] .stFileUploader label {
        color: white;
    }

    /* Make Browse button text black */
    [data-testid="stSidebar"] button {
        color: black !important;
    }

    /* Full-width container padding for header */
    .st-emotion-cache-zy6yx3 {
        width: 100%;
        padding: 1.5rem 1rem 10rem;  /* top, sides, bottom */
        max-width: initial;
        min-width: auto;
    }

    </style>
    """, 
    unsafe_allow_html=True
)

st.markdown(
    "<h1 style='text-align: center; color: #000000;'>📄 Invoice Extractor</h1>", 
    unsafe_allow_html=True
)
st.markdown(
    "<p style='text-align: center; color: gray;'>Upload an invoice on the left to preview it and see the extracted data on the right.</p>", 
    unsafe_allow_html=True
)

# --- Main layout ---
col1, col2 = st.columns([1,1])

if uploaded_file:
    image = Image.open(uploaded_file)
    processed_img = preprocess_image(image)
    text = extract_text(processed_img)
    header_result = parse_invoice_header_safe(text)
    line_items_df = parse_line_items(text)

    with col1:
        st.subheader("Invoice Preview")
        st.image(image, use_container_width=True)

    with col2:
        st.subheader("🔍 Extracted Header")
        st.json(header_result)

        st.subheader("📊 Line Items")
        if not line_items_df.empty:
            st.dataframe(line_items_df)
        else:
            st.warning("⚠️ No line items detected.")
