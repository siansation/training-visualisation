import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from multipage import *
from yolov4pages import yolov4session1, yolov4session2
from multipage_session import *

def app():
    yolov4app = MultiApp()

    st.header("yolov4")

    yolov4app.add_app("11/11/2021", yolov4session2.yolov4app)
    yolov4app.add_app("12/12/2021", yolov4session1.yolov4app)
    



    yolov4app.run()