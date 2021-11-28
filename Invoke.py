#!/usr/bin/env python
import subprocess
from getpass import getpass
import streamlit as st
import json
import os

with st.form("my_form"):
    st.write("SandBox Login SSO")
    username = st.text_input(label='Username', key='usr', max_chars=30)
    password = st.text_input(label='Password', key='pwd', max_chars=30)
    isAgree = st.checkbox("Yes, I agree.")
    
    # Every form must have a submit button.
    login = st.form_submit_button("Login SSO")
    if isAgree and login:
        with st.spinner('Authenticating...'):
            subprocess.call(["python", "selenium.py"])
        st.success('Authenticated')

with open("CoursePlan.json", "r") as file:
    jsonCourse = json.load(file)

for course in jsonCourse:
    with st.expander(label=course):
        st.write(jsonCourse[course])
