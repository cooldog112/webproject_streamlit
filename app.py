import streamlit as st
import sqlite3
import pandas as pd


def login_user(id, pwd):
    cur.execute(f"SELECT * FROM users WHERE id = '{id}' and pwd = '{pwd}'")
    return cur.fetchone()


con = sqlite3.connect('database.db')
cur = con.cursor()
menu = st.sidebar.selectbox('MENU', options=['로그인', '회원가입', '회원목록'])

if menu == '로그인':
    st.subheader('로그인')
    st.sidebar.subheader('로그인')
    login_id = st.sidebar.text_input('아이디', placeholder='아이디를 입력하세요')
    login_pwd = st.sidebar.text_input('패스워드',
                                      placeholder='패스워드를 입력하세요',
                                      type='password')
    login_btn = st.sidebar.button('로그인')

    if login_btn:
        user_info = login_user(login_id, login_pwd)
        if user_info:
            st.sidebar.write(user_info[2])
            st.sidebar.write(user_info[3])
            st.sidebar.write(user_info[4])
        else:
            st.sidebar.write('로그인에 실패했습니다.')

if menu == '회원가입':
    with st.form('my_form', clear_on_submit=True):
        st.info('다음 양식을 모두 입력 후 제출합니다.')
        in_id = st.text_input('아이디', max_chars=12)
        in_name = st.text_input('성명', max_chars=10)
        in_pwd = st.text_input('비밀번호', type='password')
        in_pwd_chk = st.text_input('비밀번호 확인', type='password')
        in_birthday = st.date_input('생년월일')
        in_gender = st.radio('성별', options=['남', '여'], horizontal=True)

        submitted = st.form_submit_button('제출')
        if submitted:
            cur.execute(f"INSERT INTO users(id, pwd, name, birthday, gender) VALUES ("
                        f"'{in_id}', '{in_pwd}', '{in_name}','{in_birthday}', '{in_gender}')")
            con.commit()

if menu == '회원목록':
    st.subheader('회원목록')
    df = pd.read_sql("SELECT * FROM users", con)
    st.dataframe(df)



