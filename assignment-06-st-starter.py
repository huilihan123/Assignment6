# import packages
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('seaborn')

# show the title

st.title('Titanic App by Huili Han')
# read csv and show the dataframe

df_training = pd.read_csv('train.csv')

# create a figure with three subplots, size should be (15, 5)
# show the box plot for ticket price with different classes
# you need to set the x labels and y labels
# a sample diagram is shown below

st.write(df_training)

fig, ax = plt.subplots(1, 3)

df4 = df_training[df_training['Pclass']==1]
df4.Fare.plot.box(ax=ax[0],figsize = (15, 5) )

df5 = df_training[df_training['Pclass']==2]
df5.Fare.plot.box(ax=ax[1],figsize = (15, 5))

df6 = df_training[df_training['Pclass']==3]
df6.Fare.plot.box(ax=ax[2],figsize = (15, 5))

st.pyplot(fig)