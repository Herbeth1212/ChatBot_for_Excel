import streamlit as st
import pandas as pd
from google import genai

st.title("Chat with Your Excel Data via Gemini 🤖")

uploaded_file = st.file_uploader("Upload your Excel file", type=["xlsx", "xls"])
if uploaded_file:
    df = pd.read_excel(uploaded_file)
    st.dataframe(df.head())

    query = st.text_input("Ask a question about your data:")
    if query:
        api_key = st.secrets["API"]
        client = genai.Client(api_key=api_key)

        # Send whole sheet (be careful with very large files)
        content = df.to_string(index=False)

        prompt = (
            "You are a data analyst. Here is the dataset:\n"
            f"{content}\n\nQuestion: {query}"
        )

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )
        st.write(response.text)
