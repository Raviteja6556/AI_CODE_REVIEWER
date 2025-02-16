import streamlit as st
import google.generativeai as genai

genai.configure(api_key=st.secrets["API_KEY"])
sys_prompt= """You are an AI Python Code Reviewer. Your task is to analyze submitted code, identifying potential bugs, errors, and areas for improvement.

Your output should be formatted as follows:

Your Code Review is:

Bug report:

Fixed Code:

In case if someone as queries which are not relevant, politely tell them to ask relevant queries only."""

model = genai.GenerativeModel(model_name="models/gemini-2.0-flash-exp", system_instruction=sys_prompt)

st.title("AI Code Reviewer")
user_prompt = st.text_input("Enter your Python code here: ", placeholder="Type Your Code here...")
btn_click = st.button("Generate Answer")

if btn_click:
    response = model.generate_content(user_prompt)

    try:
        generated_text = response.candidates[0].content.parts[0].text
        st.write(generated_text)
    except AttributeError:
        st.write("An error occurred while processing the response.")
        print(response)
