import streamlit as st
import random
import altair as alt
import numpy as np
import pandas as pd

st.header('Homework 1')

st.markdown(
"**QUESTION 1**: In previous homeworks you created dataframes from random numbers.\n"
"Create a datframe where the x axis limit is 100 and the y values are random values.\n"
"Print the dataframe you create and use the following code block to help get you started"
)

st.code(
''' 
x_limit = 

# List of values from 0 to 100 each value being 1 greater than the last
x_axis = np.arange()

# Create a random array of data that we will use for our y values
y_data = []

df = pd.DataFrame({'x': x_axis,
                     'y': y_data})
st.write(df)''',language='python')

## **Answer 1**
x_limit = 100

# List of values from 0 to 100 each value being 1 greater than the last
x_axis = np.arange(0,x_limit,1)

# Create a random array of data that we will use for our y values
y_data = np.random.rand(x_limit)

df = pd.DataFrame({'x': x_axis,
                     'y': y_data})
st.write(df)


st.markdown(
"**QUESTION 2**: Using the dataframe you just created, create a basic scatterplot and Print it.\n"
"Use the following code block to help get you started."
)

st.code(
''' 
scatter = alt.Chart().mark_point().encode()

st.altair_chart(scatter, use_container_width=True)''',language='python')

## **Answer 2**
scatter = alt.Chart(df).mark_point().encode(x='x',y='y')

st.altair_chart(scatter, use_container_width=True)


st.markdown(
"**QUESTION 3**: Lets make some edits to the chart by reading the documentation on Altair.\n"
"https://docs.streamlit.io/library/api-reference/charts/st.altair_chart.  "
"Make 5 changes to the graph, document the 5 changes you made using st.markdown(), and print the new scatterplot.  \n"
"To make the bullet points and learn more about st.markdown() refer to the following discussion.\n"
"https://discuss.streamlit.io/t/how-to-indent-bullet-point-list-items/28594/3"
)

st.markdown("The five changes I made were.....")

## **Answer 3**
st.markdown("""
The 5 changes I made were:
- Added a Title
- Updated mark_point() to mark_circle()
- Added a tooltip - each point is displayed when hovered over
- Added color to be based on 'x' value
- Added size to be based on 'y' value
""")

# using css to indent 
st.markdown('''
<style>
[data-testid="stMarkdownContainer"] ul{
    list-style-position: inside;
}
</style>
''', unsafe_allow_html=True)

# updated scatter plot
scatter = alt.Chart(df,title='Scatterplot of two random variables').mark_circle().encode(  
    x='x', y='y', tooltip=['x','y'], color='x', size='y')

st.altair_chart(scatter , use_container_width=True)


st.markdown(
"**QUESTION 4**: Explore on your own!  Go visit https://altair-viz.github.io/gallery/index.html.\n "
"Pick a random visual, make two visual changes to it, document those changes, and plot the visual.  \n"
"You may need to pip install in our terminal for example pip install vega_datasets "
)

## **Answer 4**

st.markdown("""
The 2 changes I made were:
- Modified the width on both layered charts
- Modified the bar chart color to project
"""
)

# using css to indent 
st.markdown('''
<style>
[data-testid="stMarkdownContainer"] ul{
    list-style-position: inside;
}
</style>
''', unsafe_allow_html=True)


source = pd.DataFrame({
    'project': ['a', 'b', 'c', 'd', 'e', 'f', 'g'],
    'score': [25, 57, 23, 19, 8, 47, 8],
    'goal': [25, 47, 30, 27, 38, 19, 4]
})

bar = alt.Chart(source).mark_bar().encode(
    x='project',
    y='score',
    color='project'
).properties(
    width=alt.Step(20)  # controls width of bar.
)

tick = alt.Chart(source).mark_tick(
    color='red',
    thickness=1,
    size=20 * 0.9,  # controls width of tick.
).encode(
    x='project',
    y='goal'
)

st.altair_chart(bar + tick , use_container_width=True)




## Prof example
source = pd.read_json('imdb.json')
st.write(source)

imdbbar = alt.Chart(source).mark_bar(color='#07aae0').encode(
    alt.X("IMDB_Rating:Q", bin=True, title='IMDB Rating'),
    alt.Y('count()', title='Records')
)

st.altair_chart(imdbbar , use_container_width=True)

#streamlit run streamlit_cls2.py --global.dataFrameSerialization="legacy"
