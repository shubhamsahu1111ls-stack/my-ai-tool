import streamlit as st
import requests
import json

st.set_page_config(page_title="Viral Script Doctor 🚀", layout="centered")

st.title("🚀 Viral Script Doctor (Llama Edition)")
st.write("Ab bina kisi error ke banaiye viral content!")

# Secrets se Groq API Key lena
try:
    API_KEY = st.secrets["GROQ_API_KEY"]
except:
    st.error("Groq API Key nahi mili! Check Streamlit Secrets.")

user_idea = st.text_area("Aapka video topic kya hai?", placeholder="e.g. 5 Secret facts about Spices")

if st.button("Magic Karein! ✨"):
    if user_idea:
        with st.spinner('Llama AI Dimag laga raha hai...'):
            # Groq API URL
            url = "https://api.groq.com/openai/v1/chat/completions"
            
            headers = {
                "Authorization": f"Bearer {API_KEY}",
                "Content-Type": "application/json"
            }
            
            data = {
                "model": "llama-3.3-70b-versatile",
                "messages": [
                    {"role": "system", "content": "You are a Viral Content Strategist. Provide 3 Killer Hooks, 1 Viral Title, and a Thumbnail idea in Hinglish."},
                    {"role": "user", "content": user_idea}
                ]
            }

            try:
                response = requests.post(url, headers=headers, data=json.dumps(data))
                result = response.json()
                
                if 'choices' in result:
                    output_text = result['choices'][0]['message']['content']
                    st.success("Aapka Viral Plan Taiyaar Hai!")
                    st.markdown(output_text)
                else:
                    st.error(f"API Error: {result}")
                    
            except Exception as e:
                st.error(f"Connection Error: {e}")
    else:
        st.warning("Pehle kuch topic toh likhiye!")
            
