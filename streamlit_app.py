import streamlit as st
import pyshorteners

# Streamlit 앱 설정
st.title('URL 단축기')

# 사용자 입력
url = st.text_input('긴 URL을 입력하세요:')

if url:
    # pyshorteners를 사용하여 URL 단축
    s = pyshorteners.Shortener()
    short_url = s.tinyurl.short(url)  # TinyURL을 사용하여 단축
    
    st.write('단축된 URL:')
    st.write(short_url)
