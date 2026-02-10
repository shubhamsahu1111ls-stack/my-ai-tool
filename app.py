import streamlit as st
from google import genai

st.set_page_config(page_title="Viral Script Doctor 🚀", layout="centered")

# Design
st.markdown("""
    <style>
    .stButton>button { width: 100%; border-radius: 10px; background-color: #FF4B4B; color: white; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

st.title("🚀 Viral Script Doctor")
st.write("Apne idea ko 10M views layak banayein!")

# Secrets se API Key lena
try:
    api_key = st.secrets["GEMINI_API_KEY"]
    client = genai.Client(api_key=api_key)
except Exception:
    st.error("Pehle Streamlit Secrets mein API Key set karein!")

user_idea = st.text_area("Aapka video topic kya hai?", placeholder="e.g. Asli Kitchen King masala ki pehchan")

if st.button("Magic Karein! ✨"):
    if user_idea:
        with st.spinner('AI Dimag laga raha hai...'):
            try:
                prompt = f"You are a Viral Content Strategist. For the idea '{user_idea}', provide 3 Killer Hooks, 1 Viral Title, and a Thumbnail idea in Hinglish."
                
                # FIX: Model ka naam bina 'models/' ke likhein
                response = client.models.generate_content(
                    model="gemini-1.5-flash", 
                    contents=prompt
                )
                
                st.success("Aapka Viral Plan Taiyaar Hai!")
                st.markdown(response.text)
                
            except Exception as e:
                # Agar abhi bhi error aaye toh user ko sahi jaankari mile
                st.error(f"Error: {e}")
    else:
        st.warning("Pehle kuch topic toh likhiye!")
                
