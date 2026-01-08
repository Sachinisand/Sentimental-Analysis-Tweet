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
data/raw/twitter_validation.csv
