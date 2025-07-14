'''宇智波原神'''
import streamlit as st
from PIL import Image

page = st.sidebar.radio('宇智波原神', ['我的游戏推荐','我的的游戏理解','我的游戏攻略','小剧场','我的留言区'])

def page_1():
    st.write('我的游戏推荐')
    st.write('本人推荐原神和火影')
    st.write('------------------------------')


def page_2():
    st.write('游戏理解')
    st.write('丝柯克十分值得抽')
    with open('9.mp4','rb')as video_file:
        video = video_file.read()
    st.video(video)
def page_3():
    st.write('游戏攻略')
    with open('7.mp4','rb')as video_file:
        video = video_file.read()
    st.video(video)
    with open('8.mp4','rb')as video_file:
        video = video_file.read()
    st.video(video)
def page_4():
    st.write('            原神野史')
    with open('2.mp4','rb')as video_file:
        video = video_file.read()
    st.video(video)
    with open('3.mp4','rb')as video_file:
        video = video_file.read()
    st.video(video)
    with open('4.mp4','rb')as video_file:
        video = video_file.read()
    st.video(video)
    with open('5.mp4','rb')as video_file:
        video = video_file.read()
    st.video(video)
    st.write('             丝柯克翻唱')
    with open('1.mp4','rb')as video_file:
            video = video_file.read()
    st.video(video)
    with open('6.mp4','rb')as video_file:
        video = video_file.read()
    st.video(video)
def page_5():
    def page_4():
    st.write('我的留言区')
    # 从文件中加载内容，并处理成列表
    with open('leave_messages.txt', 'r', encoding='utf-8') as f:
        messages_list = f.read().split('\n')
    for i in range(len(messages_list)):
        messages_list[i] = messages_list[i].split('#')
    for i in messages_list:
        if i[1] == '阿短':
            with st.chat_message('🌞'):
                st.write(i[1],':',i[2])
        elif i[1] == '编程猫':
            with st.chat_message('🍥'):
                st.write(i[1],':',i[2])
    name = st.selectbox('我是……', ['阿短', '编程猫'])
    new_message = st.text_input('想要说的话……')
    # 从文件中加载内容，并处理成列表
    with open('leave_messages.txt', 'r', encoding='utf-8') as f:
        messages_list = f.read().split('\n')
    for i in range(len(messages_list)):
        messages_list[i] = messages_list[i].split('#')
    for i in messages_list:
        if i[1] == '阿短':
            with st.chat_message('🌞'):
                st.write(i[1],':',i[2])
        elif i[1] == '编程猫':
            with st.chat_message('🍥'):
                st.write(i[1],':',i[2])
    name = st.selectbox('我是……', ['阿短', '编程猫'])
    new_message = st.text_input('想要说的话……')
    
if page == '我的游戏推荐':
    page_1()
elif page == '我的的游戏理解':
    page_2()
elif page == '我的游戏攻略':
    page_3()
elif page=='小剧场':
    page_4()
elif page == '我的留言区':
    page_5()