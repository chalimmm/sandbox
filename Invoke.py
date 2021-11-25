#!/usr/bin/env python
import subprocess
from getpass import getpass
import streamlit as st
import json


os.system('sudo apt install google-chrome-stable')
os.system('sudo apt-get install firefox')
install_driver = "sbase install chromedriver latest".split()
proc = subprocess.run(
    install_driver,
    stdout=subprocess.PIPE,
    encoding="ascii",
)

with st.form("my_form"):
    st.write("SandBox Login SSO")
    username = st.text_input(label='Username', key='usr', max_chars=30)
    password = st.text_input(label='Password', key='pwd', max_chars=30)
    isAgree = st.checkbox("Yes, I agree.")
    
    # Every form must have a submit button.
    login = st.form_submit_button("Login SSO")
    if isAgree and login:
        with st.spinner('Authenticating...'):
            subprocess.call(["pytest", "SiakNg.py", "--var1="+username, "--var2="+password, "--headless"])
        with st.spinner('Collecting Data...'):
            subprocess.call(["python", "BeautifulSoup.py"])
        st.success('Authenticated')

with open("CoursePlan.json", "r") as file:
    jsonCourse = json.load(file)

for course in jsonCourse:
    with st.expander(label=course):
        st.write(jsonCourse[course])
