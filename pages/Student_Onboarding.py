import streamlit as st
#import google.generativeai as genai
from google import genai
import json
import os
from dotenv import load_dotenv

load_dotenv()

# ── Configure Gemini ──


with open('pages/key.txt', 'r') as file:
    api_key = file.read().strip()

client = genai.Client(api_key=api_key)

# ─────────────────────────────
# PAGE CONFIG
# ─────────────────────────────

st.set_page_config(
    page_title="Onboarding | atomcamp",
    page_icon="🎓",
    layout="wide"
)

# ─────────────────────────────
# BACK BUTTON
# ─────────────────────────────

if st.button("← Back to Home"):
    st.switch_page("main.py")

# ─────────────────────────────
# HEADER
# ─────────────────────────────

st.markdown("""
<h2 style='color:#00C853;'>
🎓 Student Onboarding
</h2>

<p style='color:gray;'>
Help us understand you — Gemini AI will build your personalized learning path
</p>

<hr>
""", unsafe_allow_html=True)

# ─────────────────────────────
# GEMINI FUNCTION
# ─────────────────────────────

def get_ai_recommendation(name, background, goal, hours, experience):

    response = client.models.generate_content(
        model="gemini-2.5-flash",

        contents=f"""
You are an AI advisor for atomcamp — a Data Science and AI training platform in Pakistan.

atomcamp offers these bootcamps:

1. AI Bootcamp (3 months, PKR 75,000)
→ For STEM graduates
→ Covers ML, DL, NLP, CV, LLMs

2. Data Analytics Bootcamp (3 months, PKR 50,000)
→ For any background
→ Covers Excel, SQL, Python, Power BI

3. Automation with AI Bootcamp (6 weeks, PKR 30,000)
→ For working professionals
→ Covers n8n, Make, AI tools

4. Agentic AI Bootcamp (2 months, PKR 50,000)
→ For builders
→ Covers LangChain, AI agents, deployment

A student completed onboarding.

Analyze the profile and recommend the best bootcamp.

Student Profile:
- Name: {name}
- Background: {background}
- Goal: {goal}
- Study hours per week: {hours}
- Experience level: {experience}

Respond ONLY in valid JSON.

{{
    "recommended_bootcamp": "",
    "color": "",
    "duration": "",
    "price": "",
    "reason": "",
    "learning_path": [
        "",
        "",
        "",
        "",
        "",
        ""
    ],
    "first_action": "",
    "strength": "",
    "focus_area": ""
}}
"""
    )

    raw = response.text

    # remove markdown wrapping if Gemini adds it
    raw = raw.replace("```json", "").replace("```", "").strip()

    return json.loads(raw)

# ─────────────────────────────
# FORM
# ─────────────────────────────

with st.form("onboarding_form"):

    st.markdown("### 👤 Personal Information")

    col1, col2 = st.columns(2)

    with col1:
        name = st.text_input(
            "Full Name",
            placeholder="e.g. Ahmed Ali"
        )

    with col2:
        email = st.text_input(
            "Email",
            placeholder="e.g. ahmed@gmail.com"
        )

    st.markdown("---")

    st.markdown("### 🎯 Background & Goals")

    col3, col4 = st.columns(2)

    with col3:
        background = st.selectbox(
            "Your Background",
            [
                "STEM Graduate (CS, Engineering, Math)",
                "Non-Technical (Business, Arts, Social Sciences)",
                "Working Professional",
                "Fresh Graduate (Any Field)"
            ]
        )

    with col4:
        goal = st.selectbox(
            "What is your main goal?",
            [
                "Get a Data Science / AI job",
                "Freelancing with Data Skills",
                "Upskill for current job",
                "Research / Further Studies",
                "Build my own AI product"
            ]
        )

    hours = st.slider(
        "How many hours per week can you study?",
        min_value=2,
        max_value=40,
        value=10,
        step=2
    )

    st.markdown("---")

    st.markdown("### 📚 Prior Knowledge")

    experience = st.selectbox(
        "Your experience level",
        [
            "Complete Beginner — no coding or data background",
            "Basic Python — can write simple scripts",
            "Intermediate — worked with data or ML before",
            "Advanced — built ML models or AI projects"
        ]
    )

    st.markdown("---")

    submitted = st.form_submit_button(
        "🤖 Generate My AI Learning Path",
        use_container_width=True
    )

# ─────────────────────────────
# AFTER SUBMIT
# ─────────────────────────────

if submitted:

    if not name or not email:

        st.error("❌ Please fill in your name and email.")

    else:

        with st.spinner("🤖 Gemini is analyzing your profile..."):

            try:

                result = get_ai_recommendation(
                    name,
                    background,
                    goal,
                    hours,
                    experience
                )

                # save in session state

                st.session_state.student_name = name
                st.session_state.student_email = email
                st.session_state.background = background
                st.session_state.goal = goal
                st.session_state.hours = hours
                st.session_state.experience = experience
                st.session_state.bootcamp = result["recommended_bootcamp"]
                st.session_state.ai_result = result

                # ─────────────────────────────
                # RESULTS
                # ─────────────────────────────

                st.markdown("---")

                st.success(f"✅ Analysis complete for {name}!")

                # metrics

                c1, c2 = st.columns(2)

                c1.metric(
                    "Hours Per Week",
                    f"{hours} hrs"
                )

                c2.metric(
                    "Experience",
                    experience.split("—")[0].strip()
                )

                color = result.get("color", "#00C853")

                # recommendation card

                st.markdown(f"""
<div style='padding:25px;
            background-color:{color}22;
            border-left:6px solid {color};
            border-radius:10px;
            margin-top:15px'>

<h4 style='color:{color}; margin:0'>
🤖 Gemini Recommends
</h4>

<h2 style='margin:8px 0'>
{result["recommended_bootcamp"]}
</h2>

<p style='color:gray; margin:0'>
⏱ {result["duration"]}
&nbsp; | &nbsp;
💰 {result["price"]}
</p>

</div>
""", unsafe_allow_html=True)

                # reason

                st.markdown("### 💡 Why This Bootcamp?")

                st.info(result["reason"])

                # strengths + focus

                col_a, col_b = st.columns(2)

                with col_a:
                    st.success(
                        f"💪 Your Strength: {result['strength']}"
                    )

                with col_b:
                    st.warning(
                        f"🎯 Focus Area: {result['focus_area']}"
                    )

                # roadmap

                st.markdown("### 🗺️ Personalized Learning Path")

                for step in result["learning_path"]:

                    st.markdown(f"""
<div style='padding:12px 18px;
            margin:6px 0;
            background:#1e1e1e;
            border-radius:8px;
            border-left:4px solid {color}'>

✅ {step}

</div>
""", unsafe_allow_html=True)

                # first action

                st.markdown("### 🚀 Start Today")

                st.markdown(f"""
<div style='padding:15px;
            background:#00C85322;
            border-radius:8px;
            border-left:5px solid #00C853'>

<b>Your first action:</b>
{result["first_action"]}

</div>
""", unsafe_allow_html=True)

                st.markdown("<br>", unsafe_allow_html=True)

                # dashboard button

                if st.button(
                    "Continue to My Dashboard →",
                    use_container_width=True
                ):

                    st.switch_page(
                        "pages/student_dashboard_page2.py"
                    )

            except Exception as e:

                st.error(f"❌ Gemini Error: {e}")

                st.info(
                    "Check your Gemini API key or JSON formatting."
                )