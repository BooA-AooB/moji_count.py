import streamlit as st

title = st.text_input('数えたい文章を貼ろう！')
st.write('この文章の文字数は', len(title))
