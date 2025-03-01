import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import csv
from sklearn.preprocessing import LabelEncoder


# Open the CSV file and read data into a list
data_dict = {'PassengerId': [], 'Survived': [], 'Pclass': [], 'Name': [], 'Sex': [], 'Age': [], 'SibSp': [], 'Parch': [], 'Ticket': [], 'Fare': [], 'Cabin': [], 'Embarked': []}

with open("Titanic-Dataset.csv", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)  # Reads CSV as dictionary
    for row in reader:
        data_dict['PassengerId'].append(int(row['PassengerId']))  # Convert to int
        data_dict['Survived'].append(int(row['Survived']))
        data_dict['Pclass'].append(int(row['Pclass']))
        data_dict['Name'].append(row['Name'])  # Name is already a string
        data_dict['Sex'].append(row['Sex'])  # Sex is already a string
        
        # Handle missing values for Age (convert to float, or None if empty)
        data_dict['Age'].append(float(row['Age']) if row['Age'] else None)

        data_dict['SibSp'].append(int(row['SibSp']))  #No. of siblings / spouses aboard the Titanic
        data_dict['Parch'].append(int(row['Parch']))  #No. of parents / children aboard the Titanic
        data_dict['Ticket'].append(row['Ticket'])  # Ticket is a string
        data_dict['Fare'].append(float(row['Fare']))  # Convert to float  (How much money they spend for service)
        
        # Handle missing values for Cabin
        data_dict['Cabin'].append(row['Cabin'] if row['Cabin'] else None)

        # Handle missing values for Embarked
        data_dict['Embarked'].append(row['Embarked'] if row['Embarked'] else None)

# Convert to DataFrame
df = pd.DataFrame(data_dict)

# Encode 'Sex' column (Male = 1, Female = 0)
label_encoder = LabelEncoder()
df['Sex'] = label_encoder.fit_transform(df['Sex'])

# Handle missing values in 'Age' (fill with median)
df['Age'].fillna(df['Age'].median(), inplace=True)


#Pclass is the class of the ticket 1st 2nd or 3rd
X = df[['Pclass', 'Sex', 'Age']]  # Features (Values that will be taken as an input to predict the value)
y = df['Survived']  # Target variable (Value that we want to predict)

model = DecisionTreeClassifier()  # Initialize Decision Tree
model.fit(X, y)  # Train the model

# Predict if a 1st class guy who is a women and 20 years old will survive titanic
new_person_df = pd.DataFrame([[1, 1, 20]], columns=['Pclass', 'Sex', 'Age'])
prediction = model.predict(new_person_df)

if prediction[0] == 0:
    print("Will survive a titanic crash: No")  # Output: 0 (No) or 1 (Yes)
else:
    print("Will survive a titanic crash: Yes")  # Output: 0 (No) or 1 (Yes)


