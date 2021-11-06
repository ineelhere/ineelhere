import streamlit as st
from streamlit_embedcode import github_gist

def codearea():
    st.markdown("""
    *Try writing your own codes in Google Colab notebooks 👉 *
    <a href="https://colab.research.google.com/" target="_blank"><img width="64" height="64" src="https://colab.research.google.com/img/colab_favicon_256px.png" alt="Github" > </a>
    
    """, unsafe_allow_html=True)

def first():
    st.subheader("First things first")
    st.markdown("""
    In order to code, you will need of course, the language itself.  First, let us get our programming languages installed and set up in our systems. To install and get started with python, simply follow the steps here -  \n
    Python documentation - [https://docs.python.org/3/](https://docs.python.org/3/)
    
    Now, we will need an **[Integrated development environment  (IDE)](https://en.wikipedia.org/wiki/Integrated_development_environment)** for writing and executing our codes
    There are numerous options available. Few of the commonly used are -
    * [Visual Studio Code ](https://code.visualstudio.com/)
    * [Atom Code Editor ] (https://atom.io/)
    * [PyCharm] (https://www.jetbrains.com/pycharm/)
    * [R Studio](https://www.rstudio.com/products/rstudio/download/) - recommended for coding in R but also supports python 😉
    * [Jupyter Notebook] (https://jupyter.org/)
    
    💡 Having issues with the above? Try **[Google Colab](https://colab.research.google.com/) **
    """,  unsafe_allow_html=True)


def all():
    st.subheader("**Let's code!**")
    st.markdown("""
    * Open a notebook in Google Colab - <a href="https://colab.research.google.com/" target="_blank"><img width="64" height="64" src="https://colab.research.google.com/img/colab_favicon_256px.png" alt="Github" > </a>
    * Follow along with the lines of codes listed below.
    * Simply copy pasting is not recommended, but if you are here for a quick revision, please feel free to do whatever that saves your time!
    * This whole notebook is [availabele here](https://github.com/ineelhere/pylearn/blob/master/codekitchen/ipynb_files/all_codes_py101.ipynb).
    
    """, unsafe_allow_html=True)
    github_gist('https://gist.github.com/ineelhere/16af99c0506f149f195ff0f3901577d1', width=800, height=500)
    st.write('![](https://imgs.xkcd.com/comics/python.png)')
    codearea()

