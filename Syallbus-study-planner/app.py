import streamlit as st
from study_planner import read_pdf, days_until, build_prompt, get_study_plan


st.title("Syllabus Study Planner")

uploaded_file = st.file_uploader("Upload your syllabus PDF", type="pdf")
exam_date = st.text_input("Exam date (YYYY-MM-DD)")

if st.button("Generate Plan"):
    try:
        pdf_text = read_pdf(uploaded_file)
    except ValueError as e:
        st.error(str(e))
        st.stop()

    try:
        days_left = days_until(exam_date)
    except ValueError as e:
        st.error(str(e))
        st.stop()

    prompt = build_prompt(pdf_text, days_left)

    try:
        st.write(get_study_plan(prompt))
    except RuntimeError as e:
        st.error(str(e))
        st.stop()
    