import streamlit as st
from google import genai

# Page ki setting
st.set_page_config(page_title="Viral Script Doctor 🚀", layout="centered")

st.title("🚀 Viral Script Doctor")
st.subheader("Apne boring idea ko Viral Content mein badle!")

# User se API Key aur Idea lena
# Ab hum user se key nahi mangenge, seedha system se uthayenge
api_key = st.secrets["GEMINI_API_KEY"]
user_idea = st.text_area("Aapka video topic kya hai? (Eg: How to grow potatoes at home)")

if st.button("Magic Karein! ✨"):
    if not api_key or not user_idea:
        st.error("Please dono cheezein bhariye!")
    else:
        try:
            client = genai.Client(api_key=api_key)
            
            # Ye hai wo unique prompt jo ise viral banayega
            prompt = f"""
            You are a Viral Content Strategist. The user has this idea: {user_idea}.
            Please provide:
            1. A 'Killer Hook' (First 3 seconds of the video).
            2. A viral Title idea.
            3. A Thumbnail concept that gets 20% CTR.
            4. 3 Keywords to rank on YouTube.
            Write the response in Hinglish.
            """
            
            response = client.models.generate_content(
                model="gemini-2.0-flash", 
                contents=prompt
            )
            
            st.success("Aapka Viral Plan Taiyaar Hai!")
            st.markdown(response.text)
            
        except Exception as e:
            st.error(f"Kuch galat hua: {e}")

st.divider()
st.info("Tip: Ise viral karne ke liye iska link apne WhatsApp status par lagayein!")
