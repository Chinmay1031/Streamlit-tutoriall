import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

st.title("This is my Streamlit App")

# Sliders
x = np.linspace(0, np.pi*2, 100)
t = st.slider("t", 0.0, 10.0, 1.0)
x0 = st.slider("x0", 0.0, np.pi*2, 0.0)

# Function selector
func_name = st.selectbox("Function", ["sin", "cos", "tan"])
function_dict = {"sin": np.sin, "cos": np.cos, "tan": np.tan}
y = function_dict[func_name](x * t + x0)

# Tabs
tab1, tab2, tab3 = st.tabs(["Line Chart", "Matplotlib Plot", "Bar Chart"])

with tab1:
    st.subheader("Line Chart with Streamlit")
    st.line_chart(pd.DataFrame({f"{func_name}(x*t+x0)": y}))

with tab2:
    st.subheader("Matplotlib Plot")
    fig, ax = plt.subplots()
    ax.plot(x, y, label=f"{func_name}(x*t+x0)")
    ax.legend()
    st.pyplot(fig)

with tab3:
    st.subheader("Bar Chart")
    st.bar_chart(pd.DataFrame({f"{func_name}(x*t+x0)": y}))
