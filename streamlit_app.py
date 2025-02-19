from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

st.markdown("<style>h1 {color: #0D5257; font-size:21px} p {color:#555} label p {color:#0D5257;} p a, .css-5rimss a {color:#F98B3C !important} .e1vs0wn30, .e115fcil2 {width:50%; float:left} button svg {fill:#F98B3C !important}</style>", unsafe_allow_html=True)
# st.image("https://didigital.co.za/maia.jpg")

"""
# Sales Demo by Decision Inc.

If you have any questions, reach out to our [sales team](mailto:salesau@decisioninc.com.au)
"""


with st.echo(code_location='below'):
    total_points = st.slider("Number of points in spiral", 1, 5000, 2000)
    num_turns = st.slider("Number of turns in spiral", 1, 100, 9)

    Point = namedtuple('Point', 'x y')
    data = []

    points_per_turn = total_points / num_turns

    for curr_point_num in range(total_points):
        curr_turn, i = divmod(curr_point_num, points_per_turn)
        angle = (curr_turn + 1) * 2 * math.pi * i / points_per_turn
        radius = curr_point_num / total_points
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        data.append(Point(x, y))

    st.altair_chart(alt.Chart(pd.DataFrame(data), height=500, width=500)
        .mark_circle(color='#0068c9', opacity=0.5)
        .encode(x='x:Q', y='y:Q'))
