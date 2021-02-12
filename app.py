import streamlit as st

from summarizer import Summarizer

st.title('Test')

doc = st.text_area("Document")

ratio = st.number_input('Output length', .01, 1.0, .01)

if st.button('Summarize'):
    model = Summarizer()
    ans = model(doc, ratio=ratio)
    st.write(ans)