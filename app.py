import pickle
import streamlit as st
import requests

def fetch_poster(book):
    full_path = poster[poster['book_title'] == book]['imageURLM'].values[0]
    return full_path

def recommend(book):
    qindex = searchable[searchable.index == book]['count'][0]
    distance, indices = model.kneighbors(pivot.iloc[qindex,:].values.reshape(1,-1), n_neighbors=6)
    recommended_book_names = []
    recommended_book_posters = []
    for i in range(0, len(distance.flatten())):
        if i != 0:
            recommended_book_names.append(pivot.index[indices.flatten()[i]])

    for i in recommended_book_names:
        recommended_book_posters.append(fetch_poster(i))

    return recommended_book_names,recommended_book_posters


st.header('Book Recommender System')
searchable = pickle.load(open('booklist.pkl','rb'))
model = pickle.load(open('model.pkl','rb'))
pivot = pickle.load(open('pivot.pkl','rb'))
poster = pickle.load(open('poster.pkl','rb'))

booklist = searchable.index.values
selected_book = st.selectbox(
    "Type or select a book from the dropdown",
    booklist
)

if st.button('Show Recommendation'):
    recommended_book_names,recommended_book_posters = recommend(selected_book)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_book_names[0])
        st.image(recommended_book_posters[0])
    with col2:
        st.text(recommended_book_names[1])
        st.image(recommended_book_posters[1])

    with col3:
        st.text(recommended_book_names[2])
        st.image(recommended_book_posters[2])
    with col4:
        st.text(recommended_book_names[3])
        st.image(recommended_book_posters[3])
    with col5:
        st.text(recommended_book_names[4])
        st.image(recommended_book_posters[4])
