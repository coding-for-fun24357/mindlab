import streamlit as st

st.set_page_config(page_title="MindLab", page_icon="🧠")

st.title("🧠 MindLab")
st.subheader("A cognitive bias experiment game")

st.write(
    "MindLab measures decision patterns through short behavioral scenarios, "
    "then tests whether debiasing prompts change your choices."
)

if st.button("Start Experiment"):
    st.write("Round 1: Baseline decisions will go here.")
