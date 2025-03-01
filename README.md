Titanic Survival Prediction using Decision Tree Classifier
This project uses the Titanic dataset to predict whether a passenger survived the Titanic disaster based on certain features using a Decision Tree Classifier.

Table of Contents
Project Description
Dataset
Requirements
How to Run
License
Project Description
This project implements a machine learning model using Decision Tree Classifier to predict the survival of passengers on the Titanic. The model is trained on the Titanic dataset, and the prediction is based on the following features:

Pclass: Ticket class (1st, 2nd, or 3rd class)
Sex: Gender (Male or Female)
Age: Age of the passenger
The model is trained to classify whether a passenger survived or not (Survived = 1 for survived, 0 for not survived).

How It Works
Data Preprocessing:
The CSV file is read, and missing values are handled for Age, Cabin, and Embarked.
The categorical variable Sex is encoded (Male = 1, Female = 0).
Missing values in Age are filled with the median value.
Model Training:
A Decision Tree Classifier model is used for training on the features Pclass, Sex, and Age.
Prediction:
The trained model is then used to predict the survival of a new passenger, based on their class, gender, and age.
Dataset
The dataset used in this project is the Titanic dataset. The dataset contains information about passengers aboard the Titanic and whether they survived the disaster.

Dataset Columns
PassengerId: Unique ID of the passenger
Survived: Whether the passenger survived (1 = Yes, 0 = No)
Pclass: Ticket class (1st, 2nd, 3rd)
Name: Name of the passenger
Sex: Gender of the passenger (Male/Female)
Age: Age of the passenger
SibSp: Number of siblings or spouses aboard
Parch: Number of parents or children aboard
Ticket: Ticket number
Fare: Fare paid for the ticket
Cabin: Cabin number (if available)
Embarked: Port of embarkation (C = Cherbourg; Q = Queenstown; S = Southampton)
The dataset should be in CSV format with the file name Titanic-Dataset.csv.

Requirements
You need to install the following Python libraries:

pandas: for handling data structures and reading CSV files
sklearn: for building the Decision Tree Classifier model
csv: for reading CSV files
You can install the required libraries using the following pip commands:

bash
Copy
Edit
pip install pandas
pip install scikit-learn
How to Run
Make sure you have the Titanic-Dataset.csv file in the same directory as the Python script.
Clone the repository or download the script.
Run the Python script to train the Decision Tree model and make predictions.
bash
Copy
Edit
python titanic_survival_prediction.py
The script will output whether a 1st-class female passenger aged 20 years will survive the Titanic crash.

Example output:

yaml
Copy
Edit
Will survive a Titanic crash: Yes
License
This project is licensed under the MIT License - see the LICENSE file for details.
