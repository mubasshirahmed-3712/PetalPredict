# 🌸 PetalPredict
> Predicting Iris Flower Species with Machine Learning + Flask

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-Framework-black?logo=flask)](https://flask.palletsprojects.com/)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-orange?logo=scikit-learn)](https://scikit-learn.org/)
[![Status](https://img.shields.io/badge/Status-Completed-success)]()

---

## 📌 Overview
**PetalPredict** is a mini end-to-end ML project that demonstrates how to deploy a **classification model** with Flask.  
It uses the **classic Iris dataset** to predict flower species based on Sepal and Petal measurements.  

🌼 **Iris-setosa** | 🌸 **Iris-versicolor** | 🌺 **Iris-virginica**

---

## 📂 Dataset
- Source: **Iris dataset (Fisher, 1936)**  
- Features:
  - `Sepal_Length`, `Sepal_Width`
  - `Petal_Length`, `Petal_Width`
- Target:
  - `Class` → Iris-setosa, Iris-versicolor, Iris-virginica

---

## 🧭 Workflow
1. **Notebook** (`petal_predict.ipynb`)
   - EDA (pairplots, class distribution)
   - RandomForest model with scaling pipeline
   - Evaluation (accuracy, confusion matrix)
   - Save trained pipeline → `app/models/best_model.pkl`
2. **Flask App** (`app/app.py`)
   - Form inputs: sepal/petal length & width
   - Model prediction with flower emoji 🌸🌼🌺
3. **UI**
   - Animated gradient background
   - Clean input form + result card
   - Footer branding

---

## 🎨 App UI
| Input Form |
|------------|
| ![UI Overview](results/UI_Overview.gif) | 

---

## 📂 Project Structure
```
08_PetalPredict/
├─ app/
│  ├─ models/
│  │  └─ best_model.pkl
│  ├─ static/
│  │  └─ styles.css
│  ├─ templates/
│  │  └─ index.html
│  └─ app.py
├─ data/
│  └─ iris.csv
├─ notebook/
│  └─ petal_predict.ipynb
├─ results/
│  └─ UI_Overview.gif
└─ requirements.txt
```

---

## ⚙️ Getting Started

### 🔹 Clone the repo
```bash
git clone https://github.com/mubasshirahmed-3712/PetalPredict.git
cd PetalPredict
```

### 🔹 Install dependencies
```bash
pip install -r requirements.txt
```

### 🔹 Run the app
```bash
cd app
python app.py
```

Open browser → `http://127.0.0.1:5000`

---

## 🚀 Future Enhancements
- Add more ML models (SVM, KNN, Logistic Regression) with comparison  
- Deploy on **Render / Railway / Streamlit Cloud**  
- Add probability visualization (confidence bar chart)  

---

## 👤 Author
**Mubasshir Ahmed**  
📌 Full Stack Data Science Enthusiast | ML & AI Projects  
