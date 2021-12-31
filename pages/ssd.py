import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from multipage import *
from ssdpages import ssdsession1, ssdsession2
from multipage_session import *

def app():
    ssdapp = MultiApp()

    st.header("ssd")


    ssdapp.add_app("9/12/2021", ssdsession1.ssdapp)
    ssdapp.add_app("28/12/2021", ssdsession2.ssdapp)


    ssdapp.run()