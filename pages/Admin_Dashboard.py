import streamlit as st
import pandas as pd
from google import genai

# =========================================================
# PAGE CONFIG
# =========================================================
st.set_page_config(
    page_title="AI LMS Admin Dashboard",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Adaptive LMS - Admin Dashboard")
st.markdown("AI-powered learning analytics and decision intelligence system")

# =========================================================
# LOAD GEMINI API KEY
# =========================================================
with open('pages/key.txt', 'r') as file:
    api_key = file.read().strip()

client = genai.Client(api_key=api_key)

# =========================================================
# PLATFORM METRICS
# =========================================================
st.markdown("## 📊 Platform Overview")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Learners", "10,540", "+12%")
col2.metric("Active Bootcamps", "14", "+2")
col3.metric("Completion Rate", "81%", "+5%")
col4.metric("Dropout Risk", "18%", "-3%")

# =========================================================
# BOOTCAMP ENROLLMENTS
# =========================================================
st.markdown("## 🚀 Bootcamp Enrollments")

bootcamp_df = pd.DataFrame({
    "Bootcamp": [
        "AI",
        "Data Analytics",
        "Automation with AI",
        "Agentic AI"
    ],
    "Enrollments": [4200, 3100, 1800, 1400]
})

st.bar_chart(bootcamp_df.set_index("Bootcamp"))

# =========================================================
# LEARNER GROWTH
# =========================================================
st.markdown("## 📈 Monthly Learner Growth")

learner_growth = pd.DataFrame({
    "Month": ["Jan", "Feb", "Mar", "Apr", "May"],
    "Students": [3000, 4200, 5200, 7600, 10540]
})

st.line_chart(learner_growth.set_index("Month"))

# =========================================================
# COMPLETION ANALYTICS
# =========================================================
st.markdown("## 🎯 Completion Analytics")

completion_df = pd.DataFrame({
    "Bootcamp": [
        "AI",
        "Analytics",
        "Automation",
        "Agentic AI"
    ],
    "Completion Rate": [72, 84, 91, 69]
})

st.dataframe(completion_df, use_container_width=True)

# =========================================================
# AT-RISK STUDENTS
# =========================================================
st.markdown("## ⚠️ At-Risk Learners")

risk_df = pd.DataFrame({
    "Student": [
        "Ali",
        "Sara",
        "Ahmed",
        "Fatima",
        "Usman"
    ],
    "Engagement %": [32, 81, 45, 28, 61],
    "Quiz Average": [40, 88, 52, 35, 67],
    "Dropout Risk": [
        "High",
        "Low",
        "Medium",
        "High",
        "Medium"
    ]
})

st.dataframe(risk_df, use_container_width=True)

# =========================================================
# SKILL GAP ANALYSIS
# =========================================================
st.markdown("## 🧠 Skill Gap Analysis")

skill_gap_df = pd.DataFrame({
    "Skill": [
        "Python",
        "SQL",
        "Machine Learning",
        "Statistics",
        "Deep Learning"
    ],
    "Weak Learners %": [62, 48, 71, 39, 65]
})

st.bar_chart(skill_gap_df.set_index("Skill"))

# =========================================================
# INSTRUCTOR ANALYTICS
# =========================================================
st.markdown("## 👨‍🏫 Instructor Performance")

instructor_df = pd.DataFrame({
    "Instructor": [
        "Dr. Ahmed",
        "Sara Khan",
        "Ali Raza",
        "Muneeb"
    ],
    "Course Rating": [4.8, 4.5, 4.1, 4.7],
    "Completion Rate": [91, 82, 69, 88],
    "Engagement Score": [94, 85, 71, 90]
})

st.dataframe(instructor_df, use_container_width=True)

# =========================================================
# DROPOUT PREDICTION
# =========================================================
st.markdown("## 📉 Predicted Dropout Trend")

dropout_df = pd.DataFrame({
    "Week": [1, 2, 3, 4, 5, 6],
    "Predicted Dropouts": [5, 8, 12, 18, 26, 31]
})

st.line_chart(dropout_df.set_index("Week"))

# =========================================================
# AI REPORT GENERATOR
# =========================================================
st.markdown("## 🧾 Generate AI Analytics Report")

if st.button("Generate AI Report"):

    with st.spinner("Generating AI insights..."):

        response = client.models.generate_content(
            model='gemini-2.0-flash',
            contents=f"""
            You are an AI learning analytics expert.

            Analyze the following LMS analytics data and generate:

            1. AI System Alerts
            2. Key Insights
            3. Major Risks
            4. Student Behavior Patterns
            5. Skill Gaps
            6. Recommendations
            7. Strategies to improve completion rate

            Enrollment Data:
            {bootcamp_df.to_string(index=False)}

            Completion Data:
            {completion_df.to_string(index=False)}

            At Risk Students:
            {risk_df.to_string(index=False)}

            Skill Gap Data:
            {skill_gap_df.to_string(index=False)}

            Instructor Analytics:
            {instructor_df.to_string(index=False)}
            """
        )

        st.markdown("## 🤖 AI Generated Report")

        st.write(response.text)