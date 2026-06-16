import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="ScopeAI Pro", page_icon="📚")

genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
model = genai.GenerativeModel('gemini-1.5-flash')

st.title("📚 ScopeAI Pro - NCERT Book Solver")
st.caption("Class 6-12 ke liye NCERT ke hisaab se answer")

class_selected = st.selectbox("Class Choose Karo:", 
    ["Class 6", "Class 7", "Class 8", "Class 9", "Class 10", "Class 11", "Class 12"])

subject = st.text_input("Subject:", "Science")
question = st.text_area("Apna NCERT Question Yahan Likho:", height=100)

if st.button("🚀 Answer Nikalo"):
    if question:
        with st.spinner("NCERT book ke hisaab se answer bana raha hun..."):
            prompt = f"""You are an NCERT expert teacher for {class_selected} {subject}.
            Answer this question strictly as per NCERT book syllabus.
            Use simple Hindi-English mix language. Give examples from NCERT.
            Question: {question}"""
            
            response = model.generate_content(prompt)
            st.success(f"Answer for {class_selected} - {subject}:")
            st.write(response.text)
    else:
        st.warning("Bhai pehle question to daal!")

st.markdown("---")
st.write("Made with ❤️ by Aarush | Powered by Gemini AI")
