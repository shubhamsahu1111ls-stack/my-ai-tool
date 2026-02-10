import streamlit as st
import requests
import json

st.set_page_config(page_title="Viral Script Doctor 🚀", layout="centered")

st.title("🚀 Viral Script Doctor")
st.write("Ab aapka har idea banega Viral!")

# Secrets se API Key lena
try:
    API_KEY = st.secrets["GEMINI_API_KEY"]
except:
    st.error("API Key nahi mili! Check Streamlit Secrets.")

user_idea = st.text_area("Aapka video topic kya hai?", placeholder="e.g. 5 Secret facts about Spices")

if st.button("Magic Karein! ✨"):
    if user_idea:
        with st.spinner('AI Dimag laga raha hai...'):
            # Direct API URL (Stable Version)
            url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={API_KEY}"
            
            headers = {'Content-Type': 'application/json'}
            
            data = {
                "contents": [{
                    "parts": [{"text": f"You are a Viral Content Strategist. For the idea '{user_idea}', provide 3 Killer Hooks, 1 Viral Title, and a Thumbnail idea in Hinglish."}]
                }]
            }

            try:
                response = requests.post(url, headers=headers, data=json.dumps(data))
                result = response.json()
                
                # Result ko display karna
                if 'candidates' in result:
                    output_text = result['candidates'][0]['content']['parts'][0]['text']
                    st.success("Aapka Viral Plan Taiyaar Hai!")
                    st.markdown(output_text)
                else:
                    st.error(f"Google Response Error: {result}")
                    
            except Exception as e:
                st.error(f"Connection Error: {e}")
    else:
        st.warning("Pehle kuch topic toh likhiye!")
