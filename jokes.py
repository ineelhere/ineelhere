import streamlit as st
import requests

def jokes():
    st.header("A Random Programming Joke 😉")
    if st.button('Click here for a Joke'):
        st.write(requests.get("https://v2.jokeapi.dev/joke/Programming?format=txt").text)
    
    st.markdown("""
    ___
    **© [Indraneel Chakraborty](https://www.linkedin.com/in/indraneelchakraborty/) | 2021**
    </p> <h6 class="jumbotron-heading" ><br> <a href="https://www.linkedin.com/in/indraneelchakraborty/" target="_blank"><img src="https://static-exp1.licdn.com/sc/h/al2o9zrvru7aqj8e1x2rzsrca" alt="Linkedin" width="32" height="32" > </a> <a href="https://sites.google.com/view/indraneelchakraborty" target="_blank"><img width="32" height="32" src="https://lh3.googleusercontent.com/mjVS_Izc6fGAvuaT0v--gb2so5mZvAbI5EUMUB41cWB7tpy81trBCR8rIlj8NoKgPzDWGN-Hs97NlW0T9W57YJ5z9A8QQWwXUYa_Zg=h120" alt="Google Sites" > </a> <a href="https://twitter.com/ineelhere" target="_blank"> <img src="https://abs.twimg.com/favicons/twitter.ico" alt="Twitter" width="32" height="32"> </a> <a href="https://www.youtube.com/channel/UCbIMzl7rOj0FkamVf_aBM8w" target="_blank"> <img src="https://www.youtube.com/s/desktop/28b67e7f/img/favicon_48.png" alt="YouTube" width="32" height="32"> </a> <a href="https://github.com/ineelhere" target="_blank"><img width="32" height="32" src="https://github.com/fluidicon.png" alt="Github" > </a> </h6><br> <p> <a href="https://docs.google.com/forms/d/e/1FAIpQLSeZuuBTcglrHmKFfTwZ66HdHVYKge6kJ3cAtSCdF7e_8NMypg/viewform" class="btn btn-outline-success" target="_blank"><strong>Contact Me</strong></a> </p> </div> </section> </main>
    """, unsafe_allow_html=True)