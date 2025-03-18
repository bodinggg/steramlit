
import streamlit as st
import pandas as pd 

"""
st.title():文章大标题'\\n'<-此处有个换行用的\n
st.header():一级标题
st.subheader():二级标题
st.text():文本
st.code():代码，同时可设置代码的语言，显示的时候会高亮
st.latex():latex公式
st.caption():小字体文本
"""


st.write("""
# My first app
Hello *world!*
""")

st.markdown('streamlit run xxx.py')
st.title('this is title')
st.header('header')
st.subheader('subheader')

code = """
import streamlit as st
#we can write code!
"""
# use this "code"
st.code(code, language='python')


