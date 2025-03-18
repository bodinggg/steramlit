import streamlit as st
import pandas as pd
import numpy as np

"""
table:普通的表格，用于静态数据的展示\n
dataframe:高级的表格，可以进行数据的操作，比如排序
"""
# 注释

df = pd.DataFrame(
    np.random.randn(10,2),
    columns = ('lat','lon'),
    index = ('col %d' %(i+1) for i in range(10))
)
st.write('table')
st.table(df)
st.write('折线图')
st.line_chart(df)
st.write('面积图')
st.area_chart(df)
st.write('柱状图')
st.bar_chart(df)
st.write('地图')
st.map(df)
"""
这时highlight_max,类似的有min，between
"""
st.dataframe(df.style.highlight_max(axis=0))

col1, col2 = st.columns(2)
col1.metric("Temperature", "36 °C","9%")
col2.metric("Wind","9 mph", "-8%")
