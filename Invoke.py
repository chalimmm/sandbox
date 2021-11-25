#!/usr/bin/env python
import subprocess
from getpass import getpass
import streamlit as st
import json

with st.form("my_form"):
    st.write("SandBox Login SSO")
    username = st.text_input(label='Username', key='usr', max_chars=30)
    password = st.text_input(label='Password', key='pwd', max_chars=30)
    isAgree = st.checkbox("Yes, I agree.")
    
    # Every form must have a submit button.
    login = st.form_submit_button("Login SSO")
    if isAgree and login:
        with st.spinner('Authenticating...'):
            install_browser = "apt install google-chrome-stable".split()
            proc = subprocess.run(
                install_browser,
                stdout=subprocess.PIPE,
                encoding="ascii",
            )
            subprocess.call(["pytest", "SiakNg.py", "--var1="+username, "--var2="+password, "--headless"])
        with st.spinner('Collecting Data...'):
            subprocess.call(["python", "BeautifulSoup.py"])
        st.success('Authenticated')

with open("CoursePlan.json", "r") as file:
    jsonCourse = json.load(file)

for course in jsonCourse:
    with st.expander(label=course):
        st.write(jsonCourse[course])
