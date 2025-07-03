# 🧠 Naive Bayes Classifier from Scratch (Categorical Features Only)

This project implements a Naive Bayes classifier **from scratch** using pure Python and Pandas. It is specifically designed for datasets with **categorical features** (like marital status, education, housing, and loan) to classify whether a customer will deposit or not.

---

## 📌 Project Overview

- ✅ Manual computation of class-conditional probabilities
- ✅ Laplace smoothing (add-one smoothing)
- ✅ Works on categorical data
- ✅ Designed for educational/demo purposes — zero use of scikit-learn!
- ✅ Includes probability-based decision logic and predictions on test data

---

## 🗃️ Dataset Info

This repository uses two CSV files:

- `Naive Bayes Dataset - Sheet1 (1).csv`: Contains training data with features and a target column `deposit` (either `yes` or `no`)
- `test.csv`: Contains new, unseen customer data without the `deposit` column (to predict)

---

## 📂 File Structure
├── Naive_Bayes_From_Scratch.ipynb # Main Jupyter notebook with complete code
├── Naive Bayes Dataset - Sheet1 (1).csv # Training dataset (categorical)
├── test.csv # Test dataset
└── README.md # You're here


---

## 🚀 How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/naive-bayes-scratch.git
   cd naive-bayes-scratch
Open the Jupyter notebook:

bash
jupyter notebook Naive_Bayes_From_Scratch.ipynb
Run all cells to:
  Load the training and test data
  Build frequency tables
  Compute Naive Bayes probabilities
  Predict outcomes (yes or no)

📊 Example Prediction Output

yaml
Test instance 1: Predicted -> yes
Test instance 2: Predicted -> no
Test instance 3: Predicted -> yes

📚 Concepts Covered
  Naive Bayes for classification
  Categorical feature handling
  Conditional probability
  Laplace smoothing
  No external ML libraries used

🧑‍💻 Author
Ahiad Mahi
Built for learning and demo purposes in AI/ML fundamentals.
Feel free to connect!

📄 License
This project is open-source and available under the MIT License.
