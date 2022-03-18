import streamlit as st
from translate_text import *
from chemapp import *
from portfolio import *
from word_freq import *
from tmdb_ineel import *
from jokes import *
from python101 import *
from random_quotes import *

st.balloons()
st.snow()

st.sidebar.markdown("""
## `Hello World!`
### I'm Indraneel Chakraborty 👨‍💻

*DevOps Enthusiast solving problems with code (and lots of googling, of course!)*
""", unsafe_allow_html=True)

st.sidebar.write("**Here are a few webapps I've created with streamlit in python**")
selections = ["About me 🙂", 
            "Coding with python 101",
            "TMDB Movie Recommendation System",
            "Find frequencies of all words present in a sentence" ,
            "Visualize chemical structures", 
            "Realtime stats on the COVID19 situation in India",
            "Random Programming Jokes",
            "Random Quotes",
            "Indian Memes (just for fun)"]

response = st.sidebar.radio('', selections)

if response == selections[0]:
    portfolio()
if response == selections[1]:
    st.markdown('<img src="https://media3.giphy.com/headers/tiktok/SRLJgKV9HbQK.gif" width="600"><br>', unsafe_allow_html=True)
    st.header("**Coding with python 101**")
    st.balloons()
    first()
    all()
    st.markdown("""
    ___
    **© [Indraneel Chakraborty](https://www.linkedin.com/in/indraneelchakraborty/) | 2021**
    </p> <h6 class="jumbotron-heading" ><br> <a href="https://www.linkedin.com/in/indraneelchakraborty/" target="_blank"><img src="https://img.icons8.com/color/48/000000/linkedin.png"/> </a>  <a href="https://twitter.com/ineelhere" target="_blank"> <img src="https://abs.twimg.com/favicons/twitter.ico" alt="Twitter" width="32" height="32"> </a> <a href="https://www.youtube.com/channel/UCbIMzl7rOj0FkamVf_aBM8w" target="_blank"> <img src="https://www.youtube.com/s/desktop/28b67e7f/img/favicon_48.png" alt="YouTube" width="32" height="32"> </a> <a href="https://github.com/ineelhere" target="_blank"><img width="32" height="32" src="https://github.com/fluidicon.png" alt="Github" > </a> </h6><br> <p> <a href="https://docs.google.com/forms/d/e/1FAIpQLSeZuuBTcglrHmKFfTwZ66HdHVYKge6kJ3cAtSCdF7e_8NMypg/viewform" class="btn btn-outline-success" target="_blank"><strong>Contact Me</strong></a> </p> </div> </section> </main>
    """, unsafe_allow_html=True)
if response == selections[2]:
    tmdb_ineel()
if response == selections[3]:
    word_freq()    
if response == selections[4]:
    chemapp()
if response == selections[5]:
    st.success("""
    This webapp is available here - **[https://share.streamlit.io/ineelhere/ifc19/2.0/ifc19_app.py](https://share.streamlit.io/ineelhere/ifc19/2.0/ifc19_app.py)**
        \nPlease click on the above URL to visit the webapp on a separate tab.
    """)
    st.markdown("""
    <iframe src="https://share.streamlit.io/ineelhere/ifc19/2.0/ifc19_app.py" height=800 width=100% ></iframe>

    """,unsafe_allow_html=True)
if response == selections[6]:
    jokes()
if response == selections[7]:
    quotes()
if response == selections[8]:
    st.success("""
    This webapp is available here - **[https://share.streamlit.io/ineelhere/meme/main/memescheme.py](https://share.streamlit.io/ineelhere/meme/main/memescheme.py)**
        \nPlease click on the above URL to visit the webapp on a separate tab.
    """)
    st.markdown("""
    <iframe src="https://share.streamlit.io/ineelhere/meme/main/memescheme.py" height=800 width=100% ></iframe>

    """,unsafe_allow_html=True)

st.sidebar.markdown("""
___
*More apps on the way!*
</p> <h6 class="jumbotron-heading" align = 'center'><br> <a href="https://www.linkedin.com/in/indraneelchakraborty/" target="_blank"><img src="https://img.icons8.com/fluency/48/000000/linkedin.png"/> </a>  <a href="https://twitter.com/ineelhere" target="_blank"> <img src="https://abs.twimg.com/favicons/twitter.ico" alt="Twitter" width="32" height="32"> </a> <a href="https://www.youtube.com/channel/UCbIMzl7rOj0FkamVf_aBM8w" target="_blank"> <img src="https://www.youtube.com/s/desktop/28b67e7f/img/favicon_48.png" alt="YouTube" width="32" height="32"> </a> <a href="https://github.com/ineelhere" target="_blank"><img width="32" height="32" src="https://github.com/fluidicon.png" alt="Github" > </a> </h6><br> <p align=center > <a href="https://docs.google.com/forms/d/e/1FAIpQLSeZuuBTcglrHmKFfTwZ66HdHVYKge6kJ3cAtSCdF7e_8NMypg/viewform" class="btn btn-outline-success" target="_blank"><strong>Contact Me</strong></a> </p> </div> </section> </main>
""", unsafe_allow_html=True)


