import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="beacon", layout="wide")
st.title("💡 beacon: Universal Inclusion Layer")

# Initialize Gemini
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
model = genai.GenerativeModel('gemini-2.5-flash')

# 1. Input Section
text_input = st.text_area("Paste complex content (text/links/descriptions) here:")

# 2. Accessibility Controls (The "User Persona" Toggle)
st.sidebar.header("Accessibility Settings")
visual_mode = st.sidebar.checkbox("Visual Mode (High Contrast/Big Buttons)")
cog_mode = st.sidebar.checkbox("Cognitive Mode (Plain Language)")
motor_mode = st.sidebar.checkbox("Motor Mode (Large Hit-Boxes)")

if st.button("Transform Content"):
    if not text_input:
        st.warning("Please paste some content.")
    else:
        # Build a prompt that uses our "ABC" logic
        prompt = f"""
        Act as an accessibility expert. Transform this content for a user with disabilities:
        - Cognitive Mode: {cog_mode} -> If ON, simplify to plain language and use bullet points.
        - Visual/Motor Mode: {visual_mode or motor_mode} -> If ON, format as a list of large, clear action items with descriptive text.
        
        Content to transform: {text_input}
        """
        response = model.generate_content(prompt)
        
        # Display output based on chosen mode
        if visual_mode or motor_mode:
            st.markdown(f"<div style='border: 5px solid #FFD700; padding: 20px; font-size: 20px;'>{response.text}</div>", unsafe_allow_html=True)
        else:
            st.markdown(response.text)
