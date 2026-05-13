import streamlit as st
import pandas as pd
import random
from google import genai
# ─────────────────────────────────────────
st.markdown("## 📚 Recommended Resources")

resources = pd.DataFrame({
    "Topic": ["Python", "SQL", "Machine Learning"],
    "Recommended Hours": [5, 3, 8],
    "Difficulty": ["Easy", "Medium", "Hard"]
})

st.dataframe(resources, use_container_width=True)

# ─────────────────────────────────────────
# Adaptive Quiz
# ─────────────────────────────────────────
st.markdown("## 🧠 Adaptive Quiz")

q = st.radio(
    "What does Pandas mainly help with?",
    [
        "Game Development",
        "Data Analysis",
        "Computer Networking",
        "Cybersecurity"
    ]
)

if st.button("Submit Quiz"):

    if q == "Data Analysis":
        st.success("✅ Correct! Difficulty level increased.")
    else:
        st.error("❌ Incorrect. Beginner content recommended.")

# ─────────────────────────────────────────
# Progress Charts
# ─────────────────────────────────────────
st.markdown("## 📈 Weekly Learning Progress")

progress_df = pd.DataFrame({
    "Week": [1, 2, 3, 4, 5],
    "Completion": [10, 20, 35, 45, 60]
})

st.line_chart(progress_df.set_index("Week"))

# ─────────────────────────────────────────
# AI Mentor Chatbot
# ─────────────────────────────────────────
with open('pages/key.txt', 'r') as file:
    api_key = file.read().strip()
client = genai.Client(api_key=api_key)

st.markdown("## 🤖 AI Mentor")

user_question = st.chat_input("Ask your AI mentor anything...")

if user_question:

    st.chat_message("user").write(user_question)

    with st.spinner("AI Mentor is thinking..."):

        response = client.models.generate_content(model='gemini-3.1-flash-lite-preview',
            contents=f"""
            You are an AI learning mentor for an adaptive LMS platform.

            Your role:
            - Help students learn effectively
            - Give concise and practical guidance
            - Recommend learning strategies
            - Motivate learners
            - Explain concepts simply

            Student Question:
            {user_question}
            """
        )
        st.chat_message("assistant").write(response.text)