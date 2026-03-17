import streamlit as st
import google.generativeai as genai

st.title("beacon: Universal Inclusion Layer")

# Debugging: Check if the key exists without showing it
if "GOOGLE_API_KEY" in st.secrets:
    st.success("Secrets loaded successfully!")
    api_key = st.secrets["GOOGLE_API_KEY"]
else:
    st.error("Error: GOOGLE_API_KEY not found in Streamlit Secrets. Check your settings!")
    st.stop()

# Configure the AI
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-flash')

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
