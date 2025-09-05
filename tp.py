import streamlit as st
from youtube_comment_downloader import YoutubeCommentDownloader
from transformers import AutoTokenizer, AutoModelForSequenceClassification, TextClassificationPipeline
import matplotlib.pyplot as plt


@st.cache_resource
def load_model():
    
