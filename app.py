import streamlit as st
import google.generativeai as genai
import os

# Set your API Key here. 
# In a professional product, we hide this. For your MVP, paste it directly:
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])

model = genai.GenerativeModel('gemini-2.5-flash')

st.title("beacon: Universal Inclusion Layer")
st.write("Making the web accessible, one URL at a time.")

url = st.text_input("Enter the URL you want to make accessible:")

if st.button("Transform Content"):
    if not url:
        st.warning("Please enter a URL first.")
    else:
        st.write("Analyzing content and applying WCAG 3.0 transformations...")
        prompt = f"""
        Act as an accessibility expert. Analyze the content from this URL: {url}. 
        Provide an accessible version following WCAG 3.0 guidelines:
        1. Simplify the language into plain English.
        2. Break the content into easy-to-read bullet points.
        3. Identify any missing 'Alt-text' for images.
        4. CRITICAL: Redact all sensitive personal data (names, IDs, emails) as [REDACTED].
        """
        response = model.generate_content(prompt)
        st.markdown("### Transformed Content:")
        st.markdown(response.text)
        st.success("beacon transformation complete.")
