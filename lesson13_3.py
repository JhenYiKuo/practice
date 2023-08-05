import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

t = np.arange(0.0,1.0,0.05)
st.write(t)
y1 = np.sin(2 * np.pi * t)
y2 = np.cos(2 * np.pi * t)
st.write(y1)
st.write(y2)

#製圖
figure1 = plt.figure(figsize=(8,4))
axes = figure1.add_subplot()
axes.plot(y1) #只寫1個代表y軸
axes.plot(y2)
#plt.show()
st.write(figure1)

#終端機執行 streanlit run lesson13_3.py