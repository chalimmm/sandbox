#!/usr/bin/env python
import subprocess
from getpass import getpass
import streamlit as st
import json
import os

with st.form("my_form"):
    st.write("SandBox Login SSO")
    username = st.text_input(label='Username', key='usr', max_chars=30)
    password = st.text_input(label='Password', type='password', key='pwd', max_chars=30)
    isAgree = st.checkbox("Yes, I agree.")
    
    # Every form must have a submit button.
    login = st.form_submit_button("Login SSO")
    if isAgree and login:
        st.markdown(
        """
        <a href="javascript:confirm('Simpan IRS?')">
        <button>Simpan</button>
        </a>
        """, unsafe_allow_html=True)
        with st.spinner('Authenticating...'):
            subprocess.call(["python", "Scraping.py", username, password])
        st.success('Authenticated')

with open("CoursePlan.json", "r") as file:
    jsonCourse = json.load(file)

for course in jsonCourse:
    with st.expander(label=course):
        st.write(jsonCourse[course])
