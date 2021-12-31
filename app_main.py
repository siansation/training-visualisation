import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from multipage import *
from pages import ssd , yolov4 
from ssdpages import ssdsession1, ssdsession2
from yolov4pages import yolov4session1, yolov4session2
from multipage_session import *

app = MultiAppp()

st.header("Visualising model training data")

# Add all your application here
app.add_app("yolov4", yolov4.app)
app.add_app("ssd", ssd.app)

# The main app
app.run()
