import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

st.header('Gemini Research Tool')

if api_key:
    # FORCE the API to use version 'v1' instead of 'v1beta'
    genai.configure(api_key=api_key, transport='rest') 
    
    # We use the most current stable model name for 2026
    # If 'gemini-1.5-flash' still fails, try 'gemini-2.0-flash'
    model_name = 'gemini-3-flash-preview' 
    
    try:
        model = genai.GenerativeModel(model_name)
        
        user_input = st.text_input('Enter your prompt:')

        if st.button('Generate'):
            if user_input:
                with st.spinner("Talking to Gemini..."):
                    # Use a manual request to ensure we aren't hitting the beta endpoint
                    response = model.generate_content(user_input)
                    st.subheader("Results:")
                    st.write(response.text)
            else:
                st.warning("Please enter a prompt.")
    except Exception as e:
        st.error(f"Model Error: {e}")
else:
    st.error("API Key not found in .env file.")