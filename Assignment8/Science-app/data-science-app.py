import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

uploadedFile = st.file_uploader("Choose a csv file...", type=['csv','xlsx'],accept_multiple_files=False,key="fileUploader")

if uploadedFile is not None:

    data=pd.read_csv(uploadedFile)

    st.dataframe(data.head(10))
    col1 , col2  = st.columns([10,10])
    data['Date'] = data['Date'].str[-5:]
    data = data.rename(columns={"Goal Type": "Type"})
    data = data.rename(columns={"Final Game Result": "Result"})
    data = data.rename(columns={"Goal Method": "Method"})
    data = data.rename(columns={"Score Home Team - When Messi Scored": "Score_home"})
    data = data.rename(columns={"Score Away Team - When Messi Scored": "Score_away"})
    with st.sidebar:
        st.subheader("About this Website : ")
        st.write("This website shows Lionel Messi methods and which methods he used it and it shows how many goals Messi has scored away from home in different years")
        st.write("")
        st.sidebar.image("Science-app\messi.jpg",caption="Lionel Messi")
    with col1:
        st.subheader("Messi Score Away")
        df = data['Type'].value_counts().rename_axis('Type').to_frame('counts').reset_index()
        fig = plt.figure(figsize=(12,10))
        df = data.groupby(['Date'])['Score_away'].count().reset_index()
        fig = plt.figure(figsize=(10,8))
        plt.bar(df['Date'],df['Score_away'],color="purple")
        plt.xlabel("Date")
        plt.ylabel("Score away")
        st.pyplot(fig)

    with col2:
        st.subheader("Messi Method")
        df = data['Method'].value_counts().rename_axis('Method').to_frame('counts').reset_index()
        fig = plt.figure(figsize=(12,10))
        plt.bar(df['Method'],df['counts'],color="blue")
        plt.xlabel("Method")
        plt.ylabel("Count")
        st.pyplot(fig)




