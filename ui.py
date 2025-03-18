import streamlit as st
import pandas as pd
import numpy as np

"""
button:按钮\n
dowload_button:文件下载\n
file_uploader:文件上传\n
checkbox:复选框\n
radio:单选框\n
selectbox:下拉单选框\n
multiselect:下拉多选框\n
slider:滑动条\n
select: slider:选择条\n
text_input:文本输入框\n
text_area:文本展示框\n
number_input:数字输入框，支持加减按钮\n
date_input:日期选择框\n
time_input:时间选择框\n
color_picker:颜色选择器
"""
"""
这就是一个简单的button
"""
st.button(label='button', help='help')
"""
这是link_button，Ta指向了教程，好了，结束。
"""
st.link_button("go to the doc", 'https://docs.streamlit.io/develop/api-reference/widgets/st.link_button')
"""
有时间会更新进实际应用的简单实例。
"""