import streamlit as st
import py3Dmol
from streamlit.proto.Markdown_pb2 import Markdown

st.title("ChemView | ineelhere")
col1, col2 = st.columns(2)
pdbid = col1.text_input("Please provide the PDB ID here")
presentation = col2.selectbox("Please select presentation style", ['sphere', 'stick', 'line', 'cross', 'cartoon'])

if pdbid:
    lm = py3Dmol.view(query='pdb:'+pdbid,width=600,height=600)
    if presentation:
        lm.setStyle({presentation:{'color':'spectrum'}})
    else:
        st.warning("Select the presentation style from above")
    lm.render()
    t =lm.js()

    f = open('viz.html', 'w')
    f.write(t.startjs)
    f.write(t.endjs)
    f.close()

    st.components.v1.html(open('viz.html', 'r').read(), width=800, height=500)
else:
    st.warning("Enter the PDB ID above")

st.markdown("""
___
**Created by [Indraneel Chakraborty](https://www.linkedin.com/in/indraneelchakraborty/) | 2021**
""")
