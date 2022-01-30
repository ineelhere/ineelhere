import streamlit as st
import py3Dmol

from streamlit.proto.Markdown_pb2 import Markdown

def chemapp():

    st.title("Chem-ineel-view | ineelhere")
    
    options = ["PubChem Compound CID",
        "RCSB Protein Data Bank (PDB) ID"]
    
    selection = st.radio("What type of chemical identifier would you like to provide?", options)
    
    if selection==options[0]:
        col1, col2 = st.columns(2)

        pc_cid = col1.text_input("Please provide the PubChem Compound CID here")
        presentation = col2.selectbox("Please select presentation style", ['stick', 'line', 'cross', 'cartoon', 'sphere' ])

        if pc_cid:
            lm = py3Dmol.view(query='cid:'+pc_cid,width=680, height=500)
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
            st.warning("Enter the PubChem Compound CID above.  \nClick [here](https://pubchem.ncbi.nlm.nih.gov/) to visit the PubChem website")       


    if selection==options[1]:
        col1, col2 = st.columns(2)

        pdbid = col1.text_input("Please provide the Protein Data Bank (PDB) ID here")
        presentation = col2.selectbox("Please select presentation style", ['stick', 'line', 'cross', 'cartoon', 'sphere'])

        if pdbid:
            lm = py3Dmol.view(query='pdb:'+pdbid,width=680, height=500)
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
            st.warning("Enter the Protein Data Bank (PDB) ID above.  \nClick [here](https://www.rcsb.org/) to visit the PDB website")

    st.markdown("""
    ___
    **© [Indraneel Chakraborty](https://www.linkedin.com/in/indraneelchakraborty/) | 2021**
    </p> <h6 class="jumbotron-heading" ><br> <a href="https://www.linkedin.com/in/indraneelchakraborty/" target="_blank"><img src="https://img.icons8.com/color/48/000000/linkedin.png"/> </a>  <a href="https://twitter.com/ineelhere" target="_blank"> <img src="https://abs.twimg.com/favicons/twitter.ico" alt="Twitter" width="32" height="32"> </a> <a href="https://www.youtube.com/channel/UCbIMzl7rOj0FkamVf_aBM8w" target="_blank"> <img src="https://www.youtube.com/s/desktop/28b67e7f/img/favicon_48.png" alt="YouTube" width="32" height="32"> </a> <a href="https://github.com/ineelhere" target="_blank"><img width="32" height="32" src="https://github.com/fluidicon.png" alt="Github" > </a> </h6><br> <p> <a href="https://docs.google.com/forms/d/e/1FAIpQLSeZuuBTcglrHmKFfTwZ66HdHVYKge6kJ3cAtSCdF7e_8NMypg/viewform" class="btn btn-outline-success" target="_blank"><strong>Contact Me</strong></a> </p> </div> </section> </main>
    """, unsafe_allow_html=True)

