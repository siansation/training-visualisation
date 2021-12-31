import streamlit as st
import pandas as pd
import numpy as np


def yolov4app():
    st.header("yolov4 training model 1")
    data = pd.read_csv(r"C:\Users\User\Downloads\yolov4_training_log_resnet18.csv")
    st.write(data)

    if st.button("loss"):
        col_list = ["loss"]
        df = pd.read_csv(r"C:\Users\User\Downloads\yolov4_training_log_resnet18.csv", usecols = col_list)
        df = df.dropna()
        st.line_chart(df)
    if st.button("validation loss"):
        col_list2 = ["validation_loss"]
        df = pd.read_csv(r"C:\Users\User\Downloads\yolov4_training_log_resnet18.csv", usecols = col_list2)
        df = df.dropna()
        st.line_chart(df)
    if st.button("mAP"):
        map = ["mAP"]
        df2 = pd.read_csv(r"C:\Users\User\Downloads\yolov4_training_log_resnet18.csv", usecols = map)
        df2 = df2.dropna()
        st.line_chart(df2)