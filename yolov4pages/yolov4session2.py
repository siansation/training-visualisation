from typing import final
import streamlit as st
import pandas as pd
import numpy as np

import boto3
import matplotlib.pyplot as plt
from multipage_session import *

def yolov4app():
    st.header("yolov4 training model (11/11/2021)")
    '''
    model = "yolov4"
    docs = "_training_log_resnet18.csv"
    path = "C:\\Users\\User\\Documents\\ml_visualize\yolov4pages\\newyolov4file3.csv"
    s3_client = boto3.client('s3', endpoint_url='http://127.0.0.1:9000',aws_access_key_id='minioadmin',
    aws_secret_access_key='minioadmin',region_name='us-east-1' )

    s3_client.download_file('logs', model+docs, path)
    
 
    '''
    path = r"C:\Users\User\Documents\ml_visualize\tlt_training\yolov4_2021-11-11-151043\yolov4_training_log_resnet18.csv"
    data  = pd.read_csv(path)
    

    st.write(data)
    
    
    if st.button("loss"):
        yAxis_name = "loss"
        col_list = [yAxis_name]
        df = pd.read_csv(path, usecols = col_list)
        df = df.dropna()
        fig, ax = plt.subplots()
        ax.plot(df)
        plt.title(yAxis_name +' against epochs')
        plt.xlabel('epochs')
        plt.ylabel(yAxis_name)
        plt.grid(True)
        ax.legend()
        plt.savefig(r"C:\Users\User\Documents\ml_visualize\11_11_2021\loss.jpg")
        st.pyplot(fig)
    if st.button("validation loss"):
        yAxis_name = "validation_loss"
        col_list = [yAxis_name]
        df = pd.read_csv(path, usecols = col_list)
        df = df.dropna()
        fig, ax = plt.subplots()
        ax.plot(df)
        plt.title(yAxis_name +' against epochs')
        plt.xlabel('epochs')
        plt.ylabel(yAxis_name)
        plt.grid(True)
        ax.legend()
        plt.savefig(r"C:\Users\User\Documents\ml_visualize\11_11_2021\validation_loss.jpg")
        st.pyplot(fig)
    if st.button("mAP"):
        yAxis_name = "mAP"
        col_list = [yAxis_name]
        df = pd.read_csv(path, usecols = col_list)
        df = df.dropna()
        fig, ax = plt.subplots()
        ax.plot(df)
        plt.title(yAxis_name +' against epochs')
        plt.xlabel('epochs')
        plt.ylabel(yAxis_name)
        plt.grid(True)
        ax.legend()
        plt.savefig(r"C:\Users\User\Documents\ml_visualize\11_11_2021\mAP.jpg")
        st.pyplot(fig)
    if st.button("Training Parameters"):
        uploaded_file = open(r"C:\Users\User\Documents\ml_visualize\tlt_training\yolov4_2021-11-11-151043\yolo_v4_drone_train_resnet18_kitti_test.txt","r")
        for line in uploaded_file:
            st.write(line)