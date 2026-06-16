import streamlit as st

st.set_page_config(page_title="ScopeAI Pro", page_icon="📚")

st.title("📚 ScopeAI Pro - NCERT Book Solver")
st.subheader("For Class 6-12 Students")

st.write("Welcome to ScopeAI! Yeh app NCERT ki books ke questions solve karne mein help karti hai.")

class_selected = st.selectbox("Class Choose Karo:", ["Class 6", "Class 7", "Class 8", "Class 9", "Class 10", "Class 11", "Class 12"])
subject = st.text_input("Subject ka naam daalo:", "Science")
question = st.text_area("Apna Question Yahan Likho:")

if st.button("Solve Karo"):
    if question:
        st.success(f"Answer for {class_selected} - {subject}:")
        st.write("Yeh ek demo answer hai. App live hone ke baad yahan AI se real answer aayega.")
        st.info("NCERT ke hisaab se detailed explanation yahan dikhega.")
    else:
        st.warning("Pehle question to likho bhai!")

st.markdown("---")
st.write("Made with ❤️ by Aarush")
