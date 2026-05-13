import streamlit as st

st.set_page_config(
    page_title="atomcamp Smart LMS",
    page_icon="⚡",
    layout="wide"
)

# ── Initialize session state ──
if "role" not in st.session_state:
    st.session_state.role = None
if "student_name" not in st.session_state:
    st.session_state.student_name = None
if "onboarded" not in st.session_state:
    st.session_state.onboarded = False

# ── Header ──
st.markdown("""
    <h1 style='text-align:center; color:#00C853;'>⚡ atomcamp Smart LMS</h1>
    <p style='text-align:center; color:gray;'>Personalized AI-powered learning for every student</p>
    <hr>
""", unsafe_allow_html=True)

# ── Role Selection ──
st.markdown("### 👋 Welcome! Who are you?")

col1, col2, col3,col4 = st.columns(4)

# ─────────────────────────────
# STUDENT
# ─────────────────────────────
with col1:

    st.markdown("""
        <div style='padding:20px;
            border:2px solid #00C853;
            border-radius:12px;
            text-align:center'>
            <h2>🎓</h2>
            <h4>Student</h4>
            <p style='color:gray;'>
            Access your personalized learning path
            </p>

        </div>
    """, unsafe_allow_html=True)

    if st.button(
        "Enter as Student",
        use_container_width=True,
        key="student_btn"
    ):

        st.session_state.role = "student"
        st.switch_page("pages/Student_Onboarding.py")


# ─────────────────────────────
# INSTRUCTOR
# ─────────────────────────────
with col2:

    st.markdown("""
        <div style='padding:20px;
            border:2px solid #2196F3;
            border-radius:12px;
            text-align:center'>
            <h2>👨‍🏫</h2>
            <h4>Instructor</h4>
            <p style='color:gray;'>
            Monitor student progress and alerts
            </p>
        </div>
    """, unsafe_allow_html=True)

    if st.button(
        "Enter as Instructor",
        use_container_width=True,
        key="instructor_btn"
    ):

        st.session_state.role = "instructor"
        st.switch_page("pages/Instructor_Dashboard.py")


# ─────────────────────────────
# ADMIN
# ─────────────────────────────
with col3:

    st.markdown("""
        <div style='padding:20px;
            border:2px solid #FF5722;
            border-radius:12px;
            text-align:center'>
            <h2>🛠️</h2>
            <h4>Admin</h4>
            <p style='color:gray;'>
            Platform-wide analytics and control
            </p>
        </div>
    """, unsafe_allow_html=True)

    if st.button(
        "Enter as Admin",
        use_container_width=True,
        key="admin_btn"
    ):

        st.session_state.role = "admin"
        st.switch_page("pages/Admin_Dashboard.py")
with col4:
    st.markdown("""
        <div style='padding:20px;
            border:2px solid #FF5722;
            border-radius:12px;
            text-align:center'>
            <h2>🎓</h2>
            <h4>Student Dashboard</h4>
            <p style='color:gray;'>
            Access your personalized learning path
            </p>
        </div>
    """, unsafe_allow_html=True)

    if st.button(
        "View Student Dashboard",
        use_container_width=True,
        key="std_dash_btn"
    ):
        st.session_state.role = 'student'
        st.switch_page("pages/Student_Dashboard.py")
# ── Stats Section ──
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("### 📊 atomcamp at a Glance")

s1, s2, s3, s4 = st.columns(4)
s1.metric("People Trained", "10,000+")
s2.metric("Job Placement", "80%")
s3.metric("Corporate Clients", "70+")
s4.metric("Women Participation", "45%")