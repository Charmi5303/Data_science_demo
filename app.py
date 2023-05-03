import pickle
import streamlit as st
import numpy as np

st.header('Book Recommender System Using Machine Learning')
model = pickle.load(open('model.pkl', 'rb'))
book_names = pickle.load(open('book_names.pkl', 'rb'))
final_rating = pickle.load(open('final_rating.pkl', 'rb'))
book_pivot = pickle.load(open('book_pivot.pkl', 'rb'))


def fetch_poster(suggestion):
    book_name = []
    ids_index = []
    poster_url = []

    for book_id in suggestion:
        book_name.append(book_pivot.index[book_id])

    for name in book_name[0]:
        ids = np.where(final_rating['title'] == name)[0][0]
        ids_index.append(ids)

    for idx in ids_index:
        url = final_rating.iloc[idx]['image_url']
        poster_url.append(url)

    return poster_url


def fetch_wikipedia_url(book_title):
    wikipedia_url = f"https://en.wikipedia.org/wiki/{book_title.replace(' ', '_')}"
    return wikipedia_url


def recommend_book(book_name):
    books_list = []
    book_id = np.where(book_pivot.index == book_name)[0][0]
    distance, suggestion = model.kneighbors(book_pivot.iloc[book_id, :].values.reshape(1, -1), n_neighbors=8)

    poster_url = fetch_poster(suggestion)
    wikipedia_urls = []

    for i in range(len(suggestion)):
        books = book_pivot.index[suggestion[i]]
        for j in books:
            books_list.append(j)
            wikipedia_url = fetch_wikipedia_url(j)
            wikipedia_urls.append(wikipedia_url)

    return books_list, poster_url, wikipedia_urls


selected_books = st.selectbox(
    "Type or select a book from the dropdown",
    book_names
)

if st.button('Show Recommendation'):
    recommended_books, poster_url, wikipedia_urls = recommend_book(selected_books)
    col1, col2, col3, col4, col5,col6,col7 = st.columns(7)
    with col1:
        st.text(recommended_books[1])
        st.image(poster_url[1])
        st.markdown(f"Click [here]({wikipedia_urls[1]}) to visit the Wikipedia page for {recommended_books[1]}")
    with col2:
        st.text(recommended_books[2])
        st.image(poster_url[2])
        st.markdown(f"Click [here]({wikipedia_urls[2]}) to visit the Wikipedia page for {recommended_books[2]}")
    with col3:
        st.text(recommended_books[3])
        st.image(poster_url[3])
        st.markdown(f"Click [here]({wikipedia_urls[3]}) to visit the Wikipedia page for {recommended_books[3]}")
    with col4:
        st.text(recommended_books[4])
        st.image(poster_url[4])
        st.markdown(f"Click [here]({wikipedia_urls[4]}) to visit the Wikipedia page for {recommended_books[4]}")
    with col5:
        st.text(recommended_books[5])
        st.image(poster_url[5])
        st.markdown(f"Click [here]({wikipedia_urls[5]}) to visit the Wikipedia page for {recommended_books[5]}")
    with col6:
        st.text(recommended_books[6])
        st.image(poster_url[6])
        st.markdown(f"Click [here]({wikipedia_urls[6]}) to visit the Wikipedia page for {recommended_books[6]}")
    with col7:
        st.text(recommended_books[7])
        st.image(poster_url[7])
        st.markdown(f"Click [here]({wikipedia_urls[7]}) to visit the Wikipedia page for {recommended_books[7]}")
