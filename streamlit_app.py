import streamlit as st
from youtube_comment_downloader import YoutubeCommentDownloader
from transformers import AutoTokenizer, AutoModelForSequenceClassification, TextClassificationPipeline
import matplotlib.pyplot as plt

# -------------------------------
# Load Hugging Face sentiment model
# -------------------------------
@st.cache_resource
def load_sentiment_model():
    model_name = "cardiffnlp/twitter-roberta-base-sentiment-latest"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSequenceClassification.from_pretrained(model_name)
    return TextClassificationPipeline(model=model, tokenizer=tokenizer)

sent_pipe = load_sentiment_model()
 
st.title("🎥 YouTube Comment Sentiment Analyzer (RoBERTa Powered)")
st.write("Paste a YouTube video URL below and fetch comments with sentiment analysi s.")

video_url = st.text_input("Enter YouTube Video URL:")
num_comments = st.slider("Number of comments to fetch", 10, 200, 50)

if video_url:
    st.info(f"Fetching up to {num_comments} comments... Please wait ⏳")

    try:
        downloader = YoutubeCommentDownloader()
        comments = downloader.get_comments_from_url(video_url, sort_by=0)  # 0=Popular, 1=Recent

        all_comments = []
        for c in comments:
            if "text" in c:
                all_comments.append(c["text"])


                
            if len(all_comments) >= num_comments:
                break

        if all_comments:
            # Sentiment predictions
            pred_labels = []
            for c in all_comments:
                out = sent_pipe(c, truncation=True, max_length=256)[0]
                label = out["label"].lower()
                pred_labels.append(label)

            # Count results
            pos = sum(1 for x in pred_labels if "positive" in x)
            neu = sum(1 for x in pred_labels if "neutral" in x)
            neg = sum(1 for x in pred_labels if "negative" in x)

            st.subheader("📊 Sentiment Summary")
            st.write(f"✅ Positive: {pos}")
            st.write(f"😐 Neutral: {neu}")
            st.write(f"❌ Negative: {neg}")

            # -------------------------------
            # Chart: Bar Plot
            # -------------------------------
            st.subheader("📊 Sentiment Distribution (Bar Chart)")
            fig, ax = plt.subplots()
            ax.bar(["Positive", "Neutral", "Negative"], [pos, neu, neg])
            ax.set_ylabel("Number of Comments")
            st.pyplot(fig)

            # -------------------------------
            # Chart: Pie Chart
            # -------------------------------
            st.subheader("🥧 Sentiment Distribution (Pie Chart)")
            fig2, ax2 = plt.subplots()
            ax2.pie([pos, neu, neg], labels=["Positive", "Neutral", "Negative"], autopct='%1.1f%%', startangle=90)
            ax2.axis("equal")
            st.pyplot(fig2)

            # -------------------------------
            # Show comments with labels
            # -------------------------------
            st.subheader("💬 Comments with Sentiment")
            for text, label in zip(all_comments, pred_labels):
                if "positive" in label:
                    emoji = "✅ Positive"
                elif "negative" in label:
                    emoji = "❌ Negative"
                else:
                    emoji = "😐 Neutral"
                st.write(f"{text} → {emoji}")

        else:
            st.warning("No comments found for this video.")

    except Exception as e:
        st.error(f"Error fetching comments: {e}")