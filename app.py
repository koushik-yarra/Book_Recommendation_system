import streamlit as st
import pickle
import numpy as np

# Load precomputed model
with open('book_recommendation_model.pkl', 'rb') as file:
    pt, sim_score = pickle.load(file)

# Recommendation function
def recommend(book_name):
    if book_name not in pt.index:
        return []
    index = np.where(pt.index == book_name)[0][0]
    similar_items = sorted(list(enumerate(sim_score[index])), key=lambda x: x[1], reverse=True)[1:6]
    return [pt.index[i[0]] for i in similar_items]

# Streamlit UI
st.title('📚 Book Recommendation System')

st.header('Get Book Recommendations')
selected_book = st.selectbox('Choose a book:', pt.index.tolist())

if st.button('Recommend'):
    recommendations = recommend(selected_book)
    if recommendations:
        st.write('You might like:')
        for book in recommendations:
            st.write(f'- {book}')
    else:
        st.write('No recommendations found.')