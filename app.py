import streamlit as st
import google.generativeai as genai

# Page Configuration
st.set_page_config(page_title="Viral Script Doctor 🚀", layout="centered")

# UI Design
st.markdown("""
    <style>
    .stButton>button { width: 100%; border-radius: 10px; background-color: #FF4B4B; color: white; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

st.title("🚀 Viral Script Doctor")
st.write("Ab aapka har idea banega Viral!")

# Setup API Key & Model
try:
    # 1. API Key fetch karna
    API_KEY = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=API_KEY)
    
    # 2. Stable model call (Humne yahan model name simple rakha hai)
    # Isse v1beta ka error khatam ho jayega
    model = genai.GenerativeModel('gemini-1.5-flash')
    
except Exception as e:
    st.error("Secrets setup mein problem hai. Please check karein!")

user_idea = st.text_area("Aapka video topic kya hai?", placeholder="e.g. 5 Secret facts about Spices")

if st.button("Magic Karein! ✨"):
    if user_idea:
        with st.spinner('AI Dimag laga raha hai...'):
            try:
                # Prompt for Viral Content
                prompt = f"You are a Viral Content Strategist. For the idea '{user_idea}', provide 3 Killer Hooks, 1 Viral Title, and a Thumbnail idea in Hinglish."
                
                # Request generating content
                response = model.generate_content(prompt)
                
                st.success("Aapka Viral Plan Taiyaar Hai!")
                st.markdown(response.text)
                
            except Exception as e:
                # Agar quota ya koi aur error aaye toh yahan dikhega
                st.error(f"Error: {e}")
    else:
        st.warning("Pehle kuch topic toh likhiye!")
    
