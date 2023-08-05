import numpy as np
import matplotlib.pyplot as plt
import streamlit as st


#介面
value = st.slider('三角函數',min_value=0,max_value=16)

t = np.arange(0.0,5,0.05)
y1 = np.sin(np.random.randn() * np.pi * t)
y2 = np.cos(np.random.randn() * np.pi * t)

#製圖
figure1 = plt.figure(figsize=(8,4))
axes1 = figure1.add_subplot()
axes1.plot(y1) #只寫1個代表y軸
axes1.plot(y2)
#plt.show()
st.write(figure1)

#終端機執行 streamlit run lesson13_3.py