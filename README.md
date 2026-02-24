# Prosperity-Prognosticator-app
# Prosperity Prognosticator: Machine Learning for Startup Success Prediction

## Project Overview
The Prosperity Prognosticator project predicts whether a startup will succeed or fail using Machine Learning techniques. This model analyzes various startup features such as funding, category, and financial indicators to forecast success probability.

## Problem Statement
Startup failure rates are high due to multiple uncertain factors. This project aims to build a Machine Learning model that predicts startup success using historical data.

## Objectives
- Perform data preprocessing and feature engineering
- Train Machine Learning models for prediction
- Evaluate model performance
- Deploy the model using a Flask web application

## Technologies Used
- Python
- Pandas
- NumPy
- Scikit-learn
- Flask

## Machine Learning Algorithm
- Random Forest Classifier

## Dataset
The dataset is collected from Kaggle and contains startup-related attributes such as:
- Funding Amount
- Startup Category
- Number of Investors
- Revenue
- Market Size
- Status (Success/Failure)

## Project Structure
Prosperity-Prognosticator/
│
├── model.py
├── app.py
├── startup_data.csv
├── requirements.txt
├── templates/
│   └── index.html
├── Project_Report.pdf
├── Project_Presentation.pptx
└── README.md


## How to Run the Project

### Step 1: Install Dependencies
pip install -r requirements.txt

### Step 2: Train Model
python model.py

### Step 3: Run Flask App
python app.py

## Output
The system predicts whether a startup will be:
- Successful
- Failed

## Future Enhancements
- Deploy using cloud platforms
- Add more datasets for higher accuracy
- Improve UI using advanced frameworks

## Author
B.Tech Final Year Project – Machine Learning Domain
