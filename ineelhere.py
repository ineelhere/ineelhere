import streamlit as st
from translate_text import *
from chemapp import *

st.sidebar.markdown("""
## `Hello World!`
### I'm Indraneel Chakraborty 👨‍💻

*Data Science enthusiast, creating data web-apps and solving problems with code (and a lot of googling, of course!)*
""", unsafe_allow_html=True)

st.sidebar.write("**Here are a few webapps I've created with streamlit in python**")
selections = ["Translate text using Python", 
            "Visualize protein structures", 
            "Realtime stats on the COVID19 situation in India"]

response = st.sidebar.radio('', selections)


if response == selections[0]:
    translate_text()
if response == selections[1]:
    chemapp()
if response == selections[2]:
    st.success("""
    This webapp is available here - **[https://share.streamlit.io/ineelhere/ifc19/2.0/ifc19_app.py](https://share.streamlit.io/ineelhere/ifc19/2.0/ifc19_app.py)**
        \nPlease click on the above URL to visit the webapp on a separate tab.
    """)
    st.markdown("""
    <iframe src="https://share.streamlit.io/ineelhere/ifc19/2.0/ifc19_app.py" height=800 width=100% ></iframe>

    """,unsafe_allow_html=True)

st.sidebar.markdown("""
___
</p> <h6 class="jumbotron-heading" align = 'center'><br> <a href="https://www.linkedin.com/in/indraneelchakraborty/" target="_blank"><img src="https://static-exp1.licdn.com/sc/h/al2o9zrvru7aqj8e1x2rzsrca" alt="Linkedin" width="32" height="32" > </a> <a href="https://sites.google.com/view/indraneelchakraborty" target="_blank"><img width="32" height="32" src="https://lh3.googleusercontent.com/mjVS_Izc6fGAvuaT0v--gb2so5mZvAbI5EUMUB41cWB7tpy81trBCR8rIlj8NoKgPzDWGN-Hs97NlW0T9W57YJ5z9A8QQWwXUYa_Zg=h120" alt="Google Sites" > </a> <a href="https://twitter.com/ineelhere" target="_blank"> <img src="https://abs.twimg.com/favicons/twitter.ico" alt="Twitter" width="32" height="32"> </a> <a href="https://www.youtube.com/channel/UCbIMzl7rOj0FkamVf_aBM8w" target="_blank"> <img src="https://www.youtube.com/s/desktop/28b67e7f/img/favicon_48.png" alt="YouTube" width="32" height="32"> </a> <a href="https://github.com/ineelhere" target="_blank"><img width="32" height="32" src="https://github.com/fluidicon.png" alt="Github" > </a> </h6><br> <p align=center > <a href="https://docs.google.com/forms/d/e/1FAIpQLSeZuuBTcglrHmKFfTwZ66HdHVYKge6kJ3cAtSCdF7e_8NMypg/viewform" class="btn btn-outline-success" target="_blank"><strong>Contact Me</strong></a> </p> </div> </section> </main>
""", unsafe_allow_html=True)

st.markdown("""
___
**Created by [Indraneel Chakraborty](https://www.linkedin.com/in/indraneelchakraborty/) | 2021**
""")
