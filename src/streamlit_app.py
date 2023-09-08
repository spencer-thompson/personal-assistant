from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import numpy as np

"""
# Welcome.
"""

st.write("")
# PAGES?
st.sidebar.markdown("# Main page 🎈")



map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(map_data)
# with st.echo(code_location='below'):
# this will give the output of the code below onto the page