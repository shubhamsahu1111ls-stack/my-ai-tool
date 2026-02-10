import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Viral Script Doctor 🚀", layout="centered")

# Custom CSS for look
st.markdown("""
    <style>
    .stButton>button { width: 100%; border-radius: 10px; background-color: #FF4B4B; color: white; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

st.title("🚀 Viral Script Doctor")
st.write("Ab aapka har idea banega Viral!")

# Secrets se API Key lena
try:
    API_KEY = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=API_KEY)
    # Stable model selection
    model = genai.GenerativeModel('gemini-1.5-flash')
except Exception as e:
    st.error("Secrets setup check karein ya API Key sahi dalein!")

user_idea = st.text_area("Aapka video topic kya hai?", placeholder="e.g. 5 Secret facts about Spices")

if st.button("Magic Karein! ✨"):
    if user_idea:
        with st.spinner('AI Dimag laga raha hai...'):
            try:
                prompt = f"You are a Viral Content Strategist. For the idea '{user_idea}', provide 3 Killer Hooks, 1 Viral Title, and a Thumbnail idea in Hinglish (Hindi + English)."
                
                response = model.generate_content(prompt)
                
                st.success("Aapka Viral Plan Taiyaar Hai!")
                st.markdown(response.text)
                
            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.warning("Pehle kuch topic toh likhiye!")
