import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Instructor Dashboard",
    page_icon="👨‍🏫",
    layout="wide"
)

# ─────────────────────────────
# HEADER
# ─────────────────────────────

st.markdown("""
<h1 style='color:#2196F3;'>
👨‍🏫 Instructor Dashboard
</h1>

<p style='color:gray;'>
AI-powered learner monitoring and intervention system
</p>

<hr>
""", unsafe_allow_html=True)

# ─────────────────────────────
# SAMPLE DATA
# ─────────────────────────────

students = pd.DataFrame({

    "Student": [
        "Ali",
        "Sara",
        "Ahmed",
        "Fatima",
        "Usman",
        "Ayesha",
        "Bilal"
    ],

    "Course": [
        "AI Bootcamp",
        "Data Analytics",
        "AI Bootcamp",
        "Agentic AI",
        "Automation AI",
        "AI Bootcamp",
        "Data Analytics"
    ],

    "Progress": [
        30,
        85,
        60,
        20,
        75,
        45,
        90
    ],

    "Attendance": [
        40,
        95,
        70,
        30,
        88,
        50,
        98
    ],

    "Assignment Score": [
        35,
        92,
        65,
        25,
        80,
        55,
        96
    ]
})

# ─────────────────────────────
# AI RISK DETECTION
# ─────────────────────────────

def detect_risk(row):

    if (
        row["Progress"] < 40
        or row["Attendance"] < 50
        or row["Assignment Score"] < 40
    ):
        return "High"

    elif (
        row["Progress"] < 70
        or row["Attendance"] < 75
    ):
        return "Medium"

    else:
        return "Low"

students["Risk"] = students.apply(detect_risk, axis=1)

# ─────────────────────────────
# METRICS
# ─────────────────────────────

total_students = len(students)

high_risk = len(
    students[students["Risk"] == "High"]
)

avg_progress = int(
    students["Progress"].mean()
)

completion_prediction = 100 - int(
    (high_risk / total_students) * 100
)

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Total Students",
    total_students
)

col2.metric(
    "High Risk Students",
    high_risk
)

col3.metric(
    "Average Progress",
    f"{avg_progress}%"
)

col4.metric(
    "Predicted Completion",
    f"{completion_prediction}%"
)

st.markdown("---")

# ─────────────────────────────
# STUDENT TABLE
# ─────────────────────────────

st.markdown("## 📊 AI Student Analytics")

st.dataframe(
    students,
    use_container_width=True
)

# ─────────────────────────────
# AI ALERTS
# ─────────────────────────────

st.markdown("## 🚨 AI Alerts")

high_risk_students = students[
    students["Risk"] == "High"
]

for _, row in high_risk_students.iterrows():

    st.error(f"""
⚠️ {row['Student']} is at HIGH RISK.

Reasons:
- Low progress ({row['Progress']}%)
- Attendance issue ({row['Attendance']}%)
- Weak assignment performance ({row['Assignment Score']}%)

AI Recommendation:
Schedule a mentor session and assign beginner-friendly exercises.
""")

# ─────────────────────────────
# AI INSIGHTS
# ─────────────────────────────

st.markdown("## 🤖 AI Insights")

st.info("""
Students with attendance below 50% are 3x more likely to drop out.

AI Bootcamp learners are struggling most with consistency during Weeks 3–5.

Recommended intervention:
- Add mentor check-ins
- Shorten assignments
- Send automated reminders
""")




# gemini

from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

with open('pages/key.txt', 'r') as file:
    api_key = file.read().strip()

#api_key = 'AIzaSyCytt_Sj6XtZvsJ9-hMfontvlFUeZjE9-g'

#print(api_key)


client = genai.Client(api_key=api_key)

# ─────────────────────────────
# AI INTERVENTION SYSTEM
# ─────────────────────────────

st.markdown("## 🤖 AI Intervention Assistant")

student_selected = st.selectbox(
    "Select Student",
    students["Student"]
)

selected_row = students[
    students["Student"] == student_selected
].iloc[0]

if st.button(
    "Generate AI Intervention Plan",
    use_container_width=True
):

    with st.spinner("Gemini is analyzing learner behavior..."):

        response = client.models.generate_content(model='gemini-3.1-flash-lite-preview',
                    contents="""
                              You are an AI academic advisor for atomcamp.

Analyze this learner:

Student: {selected_row['Student']}
Course: {selected_row['Course']}
Progress: {selected_row['Progress']}%
Attendance: {selected_row['Attendance']}%
Assignment Score: {selected_row['Assignment Score']}%
Risk Level: {selected_row['Risk']}

Generate:

1. Why this student is struggling
2. Personalized intervention plan
3. Recommended learning strategy
4. Mentor recommendation
5. Motivation advice

Keep response concise and practical.
"""
)
        st.success("AI Analysis Generated")
        st.markdown(response.text)

# ─────────────────────────────
# ENGAGEMENT CHART
# ─────────────────────────────

st.markdown("## 📈 Weekly Engagement Trend")

engagement_df = pd.DataFrame({

    "Week": [1, 2, 3, 4, 5, 6],

    "Engagement": [
        95,
        89,
        81,
        74,
        68,
        60
    ]
})

st.line_chart(
    engagement_df.set_index("Week")
)

# ─────────────────────────────
# COURSE PERFORMANCE
# ─────────────────────────────

st.markdown("## 📚 Course Performance")

course_df = students.groupby("Course")[
    "Progress"
].mean()

st.bar_chart(course_df)

# ─────────────────────────────
# SMART ACTIONS
# ─────────────────────────────

st.markdown("## ⚡ Smart Instructor Actions")

colA, colB, colC = st.columns(3)

with colA:

    if st.button(
        "Send AI Motivation Messages",
        use_container_width=True
    ):
        st.success(
            "Motivational messages sent to at-risk students."
        )

with colB:

    if st.button(
        "Generate Weak Topic Report",
        use_container_width=True
    ):
        st.success(
            "AI generated report for weak-performing topics."
        )

with colC:

    if st.button(
        "Schedule Mentor Sessions",
        use_container_width=True
    ):
        st.success(
            "Mentor sessions scheduled automatically."
        )