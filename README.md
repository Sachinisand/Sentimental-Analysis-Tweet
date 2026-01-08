# 🔍 Twitter Sentiment Analysis

This project performs **sentiment analysis on Twitter text**, classifying tweets as **Positive** or **Negative** using machine learning and NLP techniques.

---

## 📘 Table of Contents
- [What is Sentiment Analysis](#what-is-sentiment-analysis)
- [Dataset](#dataset)
- [Problem Statement](#problem-statement)
- [Motivation](#motivation)
- [Technical Aspects](#technical-aspects)
- [Installation](#installation)
- [Run](#run)
- [Directory Tree](#directory-tree)
- [To Do](#to-do)
- [Bug / Feature Request](#bug--feature-request)
- [Technologies Used](#technologies-used)
- [Credits](#credits)

---

## 🧠 What is Sentiment Analysis

Sentiment analysis (opinion mining) is the process of identifying the emotional tone behind text.  
It uses **Natural Language Processing (NLP)** and **Machine Learning** to classify text as:

- Positive  
- Negative  

In this project, we focus on **binary classification**: Positive vs Negative tweets.

---

## 📊 Dataset

This project uses the **Twitter Entity Sentiment Analysis** dataset from Kaggle:

- **Source:** [Twitter Entity Sentiment Analysis – Kaggle](https://www.kaggle.com/datasets/jp797498e/twitter-entity-sentiment-analysis)
- The dataset contains tweets labeled with:
  - `id` – Unique identifier for each tweet  
  - `topic` – Entity or topic mentioned in the tweet  
  - `sentiment` – Sentiment label (e.g., Positive, Negative, Neutral, etc.)  
  - `text` – The tweet content  

For this project:

- Only **Positive** and **Negative** labels were used  
- Neutral and other labels were excluded  
- The data files are stored locally as:
```text
data/raw/twitter_training.csv
data/raw/twitter_validation.csv ```

## 🧹 Dataset Preparation
Before training the model, the following steps were applied:

- Loaded the CSV files **without headers** and manually assigned column names:  
  `['id', 'topic', 'sentiment', 'text']`
- Filtered rows to keep only **Positive** and **Negative** sentiments
- Mapped sentiment labels to numeric values:  
  - Positive → 1  
  - Negative → 0
- Replaced missing text values with empty strings
- Split the data into training and test sets

---

## 🎯 Problem Statement

Given the text of a tweet, predict whether its sentiment is:

- **Positive**
- **Negative**

This is useful for:

- Brand and reputation monitoring  
- Customer feedback analysis  
- Social media analytics  
- Market research  

---

## 💡 Motivation

I built this project to:

- Practice **NLP and text classification**
- Work with a real **Kaggle dataset**
- Build an **end-to-end ML pipeline** (from raw data to saved model)
- Create a **portfolio project** that recruiters can review on GitHub

---

## ⚙️ Technical Aspects

### **Data Processing**
- Loaded raw CSV files from `data/raw/`
- Assigned column names: `id`, `topic`, `sentiment`, `text`
- Filtered only Positive and Negative labels
- Created a numeric label column (1 = Positive, 0 = Negative)
- Handled missing text values with `fillna("")`

### **Feature Engineering**
- Used **TF‑IDF Vectorizer** with:
  - `max_features = 5000`
  - English stopwords removed

### **Model**
- **Logistic Regression** with:
  - `max_iter = 1000`

### **Evaluation**
- Train–test split  
- Classification report (precision, recall, F1-score, accuracy)  
- Confusion matrix heatmap using seaborn  

### **Model Saving**
- Trained model saved as: `models/sentiment_model.pkl`  
- TF‑IDF vectorizer saved as: `models/tfidf_vectorizer.pkl`

---
## 🛠 Installation

### Requirements
- Python 3.8+
- pip

### Install the required libraries

```bash
pip install pandas numpy scikit-learn matplotlib seaborn joblib

## ▶️ Run

### 1. Clone the repository
```bash
git clone https://github.com/Sachinisand/sentimental-analysis-tweet.git
cd sentimental-analysis-tweet


2. Create and activate a virtual environment
python -m venv venv
venv\Scripts\activate


3. Install the required libraries
pip install pandas numpy scikit-learn matplotlib seaborn joblib


4. Run the notebook
jupyter notebook notebooks/01_sentiment_model.ipynb



---

# ✅ **After the Run section, add the Directory Tree**

```markdown
## 📁 Directory Tree


sentimental-analysis-tweet/ │── data/ │   └── raw/ │       ├── twitter_training.csv │       └── twitter_validation.csv │── notebooks/ │   └── 01_sentiment_model.ipynb │── models/ │   ├── sentiment_model.pkl │   └── tfidf_vectorizer.pkl │── README.md



✅ Then add the To‑Do section
## 📝 To Do
- Add more advanced text cleaning (URLs, emojis, mentions, lemmatization)
- Try other models (SVM, Random Forest, XGBoost)
- Build a Streamlit app for interactive predictions
- Deploy the model on a cloud platform (AWS, Azure, Render)
- Add hyperparameter tuning



✅ Then add Bug / Feature Request
## 🐞 Bug / Feature Request
If you find a bug or want to request a feature, feel free to open an issue in this repository with:
- What you tried
- What you expected
- What actually happened



✅ Then add Technologies Used
## 🧰 Technologies Used
- Python
- pandas
- numpy
- scikit‑learn
- seaborn
- matplotlib
- joblib



✅ Finally add Credits
## 🙌 Credits
- Dataset: Twitter Entity Sentiment Analysis – Kaggle  
- Project created by **Sachini Hewahattage**  
  Master’s in Data Analytics | Machine Learning & NLP  







