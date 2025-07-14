'''宇智波原神'''
import streamlit as st
from PIL import Image

page = st.sidebar.radio('宇智波原神', ['我的游戏推荐','我的的游戏理解','我的游戏攻略', '我的留言区'])


def page_1():
    '''我的推荐'''
    tab1, tab2, tab3, tab4 = st.tabs(["我的电影推荐", "我的游戏推荐", "我的书籍推荐", "我的习题集推荐"])
    with tab1:
        st.write('我的电影推荐')
        st.write('-----------------------------')
    with tab2:
        st.write('我的游戏推荐')
        with open('1.mp4','rb')as video_file:
            video = video_file.read()
        st.video(video)
        st.write('-----------------------------')
        
    with tab3:
        st.write('我的书籍推荐')
        st.write('-----------------------------')
    with tab4:
        st.write('我的习题集推荐')
        st.write('-----------------------------')


def page_2():
    pass


def page_3():
    '''我的智能词典'''
    pass


def page_4():
    '''我的留言区'''
    pass


if page == '我的兴趣推荐':
    page_1()
elif page == '我的图片处理工具':
    page_2()
elif page == '我的智能词典':
    page_3()
elif page == '我的留言区':
    page_4()
