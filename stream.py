import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

df = sns.load_dataset('titanic')

st.title('Titanic Dataset Visualization')
sel = st.sidebar.radio('Display DataFrame', ('Yes', 'No'),index=1)

if sel =='Yes':
    st.table(df)
else:
    st.write('DataFrame not displayed.')
plot_type = st.sidebar.radio('MAle % Female survival Multi Plots',('bar','line','hist','box','kde'))

if plot_type == 'bar':
    st.write('Bar plot')
    fig, ax = plt.subplots()
    df.groupby(['class', 'sex'])['survived'].mean().unstack().plot(kind='bar',ax=ax)
    st.pyplot(fig)


elif plot_type == 'line':
    st.write('Line plot')
    fig, ax = plt.subplots()
    df.groupby(['class', 'sex'])['survived'].mean().unstack().plot(kind='line',ax=ax)
    st.pyplot(fig)

elif plot_type == 'hist':
    st.write('Hist plot')
    fig, ax = plt.subplots()
    df.groupby(['class', 'sex'])['survived'].mean().unstack().plot(kind='hist',ax=ax)
    st.pyplot(fig)

elif plot_type == 'box':
    st.write('Box plot')
    fig, ax = plt.subplots()
    df.groupby(['class', 'sex'])['survived'].mean().unstack().plot(kind='box',ax=ax)
    st.pyplot(fig)

else:
    st.write('Kde plot')
    fig, ax = plt.subplots()
    df.groupby(['class', 'sex'])['survived'].mean().unstack().plot(kind='kde',ax=ax)
    st.pyplot(fig)

gender = st.sidebar.radio('Gender Based survival ',('Male', 'Female'))

if gender == 'Male':
    male = df[df['sex'] == 'male']
    st.write("Male Survival")
    fig, ax = plt.subplots()
    ax = sns.countplot(x='class', hue='survived', data=male)
    st.pyplot(fig)

else:
    female = df[df['sex'] == 'female']
    st.write("Female Survival ")
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
