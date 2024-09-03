import streamlit as st
import pandas as pd
import numpy as np

# Set the title of the app
st.title('Simple Streamlit App')

# Create a dataframe with some example data
data = pd.DataFrame({
    'x': np.arange(0, 10),
    'y': np.random.randn(10)
})

# Display the dataframe
st.write("Here's a simple dataframe:")
st.write(data)

# Create a line chart
st.line_chart(data.set_index('x'))
