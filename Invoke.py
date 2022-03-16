#!/usr/bin/env python
import subprocess
from getpass import getpass
import streamlit as st
import json
import os

with st.form("my_form"):
    st.write("SandBox Custom HTML")
    customHtml = st.text_area('Custom HTML')
    run = st.form_submit_button("Run")
st.markdown(customHtml, unsafe_allow_html=True)
