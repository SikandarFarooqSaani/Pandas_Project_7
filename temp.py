import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

#Giving Title
st.title("Data Analysis")
st.subheader("Data Analysis using python and Streamlit")

st.write("Test message")


#upload dataset

upload = st.file_uploader("Upload your data in csv")

if upload is not None:
    df = pd.read_csv(upload, encoding='latin1')


#show dataset
if upload is not None:
    if st.checkbox("Preview Dataset"):
        if st.button("Head"):
            st.write(df.head())
        if st.button("Tail"):
            st.write(df.tail())
#show datatypes
if upload is not None:
    if st.checkbox("DataType of Each Column"):
        st.text("Data Types")
        st.write(df.dtypes)

#shape
if upload is not None:
    data_shape = st.radio("What dimension you want to see", ('Rows','Columns'))
    if data_shape == 'Rows':
        st.text("Number of Rows")
        st.write(df.shape[0])
    if data_shape == 'Columns':
        st.text("Number of Columns")
        st.write(df.shape[1])
    
#finding null Values
if upload is not None:
    test = df.isnull().values.any()
    if test == True:
        if st.checkbox("Null values in Dataset"):
            fig, ax = plt.subplots()
            sns.heatmap(df.isnull(), ax=ax)
            st.pyplot(fig)
            st.text("\n Full info")
            st.write(df.isnull().sum())
        else:
            st.success("Whoo no null Values in Dataset")
             
#finding duplicates 
if upload is not None:
    testt = df.duplicated().any()
    if testt == True:
        st.warning("Dataset contains Duplicates")
        dup = st.selectbox("Do you want to remove Duplicates", (" \n Select one","Yes","No"))
        if dup =="Yes":
            df = df.drop_duplicates()
            st.text("Duplicate Values are removed")
        if dup == "No":
            st.text("Gotcha")
    else:
        st.success("Whoo no Duplicate Values in Dataset")


#geting overall Statistics 
if upload is not None:
    if st.checkbox("Summary of the Dataset"):
        st.write(df.describe(include = 'all'))
    
#about Section
if st.button("About App"):
    st.text("Built with Streamlit")
    st.text("thanks to Data thinkers on Yoututbe")

#by
if st.checkbox("By"):
    st.success("Bye User ")