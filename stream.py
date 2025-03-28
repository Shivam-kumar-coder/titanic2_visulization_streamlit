import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

df = sns.load_dataset('titanic')

st.title('Titanic Dataset Visualization')
sel = st.sidebar.radio('Display DataFrame', ('Yes', 'No'))

if sel =='Yes':
    st.table(df)
else:
    st.write('DataFrame not displayed.')

gender = st.sidebar.radio('Select Gender',('Male', 'Female'))

if gender == 'Male':
    male = df[df['sex'] == 'male']
    fig, ax = plt.subplots()
    ax = sns.countplot(x='class', hue='survived', data=male)
    st.pyplot(fig)

else:
    female = df[df['sex'] == 'female']
    fig, ax = plt.subplots()
    ax = sns.countplot(x='class', hue='survived', data=female)
    st.pyplot(fig)


city = st.sidebar.radio('Select City', ('Southampton', 'Cherbourg', 'Queenstown'))

if city == 'Southampton':
    st.subheader('Southampton - Survival Rate')
    south = df[df['embark_town'] == 'Southampton']
    fig, ax = plt.subplots()
    ax = sns.countplot(x = 'sex', hue = 'survived', data = south)
    st.pyplot(fig)

elif city == 'Cherbourg':
    st.subheader('Cherbourg - Survival Rate')
    south = df[df['embark_town'] == 'Cherbourg']
    fig, ax = plt.subplots()
    ax = sns.countplot(x = 'sex', hue = 'survived', data = south)
    st.pyplot(fig)

elif city == 'Queenstown':
    st.subheader('Queenstown - Survival Rate')
    south = df[df['embark_town'] == 'Queenstown']
    fig, ax = plt.subplots()
    ax = sns.countplot(x = 'sex', hue = 'survived', data = south)
    st.pyplot(fig)
# st.write(df['embark_town'].unique())
# st.sidebar.radio('Select City', ('New York', 'Los Angeles', 'Chicago'))

hide_menu = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
</style>
"""
st.markdown(hide_menu, unsafe_allow_html=True)

# complete
