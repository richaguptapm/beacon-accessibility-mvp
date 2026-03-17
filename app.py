import streamlit as st
import google.generativeai as genai

# Setup
st.set_page_config(page_title="beacon", page_icon="💡")
st.title("💡 beacon: Universal Inclusion Layer")
st.write("Making the web accessible, one URL at a time.")

# Check Secrets
if "GOOGLE_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
else:
    st.error("API Key missing in secrets!")
    st.stop()

# Use the 'gemini-pro' model (most reliable for text tasks)
model = genai.GenerativeModel('gemini-pro')

url = st.text_input("Enter the URL:")

if st.button("Transform Content"):
    if not url:
        st.warning("Please enter a URL.")
    else:
        try:
            with st.spinner('beacon is transforming...'):
                prompt = f"Act as an accessibility expert. Provide a WCAG 3.0 compliant, plain-language summary for: {url}. Redact all PII."
                response = model.generate_content(prompt)
                st.markdown("### Transformed Content:")
                st.markdown(response.text)
        except Exception as e:
            st.error(f"Transformation failed: {e}")
