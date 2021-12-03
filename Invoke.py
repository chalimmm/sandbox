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
    cmd = st.text_area('Custom HTML')
    st.markdown(cmd, unsafe_allow_html=True)
    selected = st.radio('Kelas', options=['Matkul 1', 'Matkul 2', 'Matkul 3'])
    
