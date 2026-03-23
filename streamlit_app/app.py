import streamlit as st

st.set_page_config(
    page_title="MBT Business OS",
    page_icon="💼",
    layout="wide"
)

if "screen" not in st.session_state:
    st.session_state.screen = "start"

def go(screen):
    st.session_state.screen = screen

def start_screen():
    st.title("MBT Business OS")
    st.subheader("Start Here")

    st.write("In 90 seconds, we’ll map your wealth posture and highlight key gaps.")

    if st.button("Start My 90-Second Diagnostic", type="primary"):
        go("diagnostic")

def diagnostic_screen():
    st.title("90-Second Diagnostic")
    st.write("Placeholder — we will add questions next.")

    if st.button("⬅ Back"):
        go("start")

if st.session_state.screen == "start":
    start_screen()
elif st.session_state.screen == "diagnostic":
    diagnostic_screen()
