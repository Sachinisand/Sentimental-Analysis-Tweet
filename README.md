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

## 🧠 What is Sentiment Analysis?

Sentiment analysis (opinion mining) is the process of identifying the emotional tone behind text.  
It uses **Natural Language Processing (NLP)** and **Machine Learning** to classify text as:

- Positive  
- Negative  

In this project, we focus on **binary classification**: Positive vs Negative tweets.

---

## 📊 Dataset

The dataset contains four columns:

- `id` — Tweet ID  
- `topic` — Topic/category  
- `sentiment` — Positive or Negative  
- `text` — The tweet content  

Only **Positive** and **Negative** labels were used for training the model.

---

## 🎯 Problem Statement

Given a tweet’s text, predict whether its sentiment is:

- **Positive**  
- **Negative**

This is useful for:

- Brand monitoring  
- Customer feedback analysis  
- Social media analytics  

---

## 💡 Motivation

I built this project to:

- Practice **NLP and text classification**  
- Work with real-world style data  
- Build an **end-to-end ML pipeline**  
- Create a **portfolio project** that recruiters can review on GitHub  

---

## ⚙️ Technical Aspects

**Data Processing:**

- Loaded raw CSV files  
- Assigned column names manually (`id`, `topic`, `sentiment`, `text`)  
- Filtered only `Positive` and `Negative` labels  
- Mapped sentiment to numeric labels:  
  - `Positive` → 1  
  - `Negative` → 0  
- Handled missing text values

**Feature Engineering:**

- Used **TF‑IDF Vectorizer**  
  - `max_features = 5000`  
  - English stopwords removed  

**Model:**

- **Logistic Regression** with `max_iter = 1000`  

**Evaluation:**

- Train–test split  
- Classification report (precision, recall, F1-score, accuracy)  
- Confusion matrix heatmap  

**Model Saving:**

- Saved trained model as: `models/sentiment_model.pkl`  
- Saved TF‑IDF vectorizer as: `models/tfidf_vectorizer.pkl`  

---

## 🛠 Installation

### Requirements

- Python 3.8+
- pip

### Install dependencies

```bash
pip install -r requirements.txt
