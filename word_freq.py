import streamlit as st
import pandas as pd
import plotly.express as px

def word_freq():
    st.title("Word Frequencies | ineelhere")
    text = st.text_area("Please type/paste a sentence")
    if text:
        words = []
        words = text.split()
        wfreq=[words.count(w) for w in words]
        x = (dict(zip(words,wfreq)))
        df = pd.DataFrame(x.items(), columns=['Word', 'Frequency']).sort_values(by="Frequency", ascending=False).reset_index(drop=True)
        st.write(f"There are **`{len(df)}`** unique words in the sentence provided.  \nHere is the list of words along with their frequencies")
        slider_ph = st.empty()
        value = slider_ph.slider("Move the slider to view data for the number of most repeated word(s)", 1, len(df), 1, 1)
        df = df.head(value)
        st.dataframe(df)
        def convert_df(df):
            return df.to_csv(index=False).encode('utf-8')

        csv = convert_df(df)

        st.download_button(
            "Press to Download",
            csv,
            "frequencies_ineelhere.csv",
            "text/csv",
            key='browser-data')
        
        
        fig = px.bar(df, x='Word', y='Frequency',  title='Words and their frequencies')
        fig.update_layout(hovermode='x')
        st.plotly_chart(fig, use_container_width=True)
