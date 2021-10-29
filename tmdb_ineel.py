import pickle
import streamlit as st
import requests

def tmdb_ineel():
    def fetch_poster(movie_id):
        url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
        data = requests.get(url)
        data = data.json()
        poster_path = data['poster_path']
        full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
        return full_path

    def recommend(movie):
        index = movies[movies['title'] == movie].index[0]
        distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
        recommended_movie_names = []
        recommended_movie_posters = []
        for i in distances[0:6]:
            # fetch the movie poster
            movie_id = movies.iloc[i[0]].movie_id
            recommended_movie_posters.append(fetch_poster(movie_id))
            recommended_movie_names.append(movies.iloc[i[0]].title)

        return recommended_movie_names,recommended_movie_posters


    st.header('TMDB Movie Recommender System | ineelhere')
    st.info("""
    * Data Source: [https://www.kaggle.com/tmdb/tmdb-movie-metadata](https://www.kaggle.com/tmdb/tmdb-movie-metadata)
    * Reference: [https://youtu.be/1xtrIEwY_zY](https://youtu.be/1xtrIEwY_zY)
    * Developer: [Indraneel Chakraborty](https://www.linkedin.com/in/indraneelchakraborty/)
    """)
    movies = pickle.load(open('model/movie_list.pkl','rb'))
    similarity = pickle.load(open('model/similarity.pkl','rb'))

    movie_list = movies['title'].values
    selected_movie = st.selectbox(
        "Type or select a movie from the dropdown",
        movie_list
    )

    recommended_movie_names,recommended_movie_posters = recommend(selected_movie)
    col1, col2, col3 = st.columns(3)
    acol1, acol2, acol3 = st.columns(3)

    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])

    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
    with acol1:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    with acol2:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])
    with acol3:
        st.text(recommended_movie_names[5])
        st.image(recommended_movie_posters[5])


