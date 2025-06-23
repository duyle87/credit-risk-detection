<<<<<<< HEAD
# Import necessary libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix

# Step 1: Load dataset from Kaggle using API


# Step 2: Explore and clean data
# Handle missing values, check for imbalance, drop irrelevant columns
cleaned_data = preprocess(data)

# Step 3: Feature engineering and selection
# Extract features and labels
features = cleaned_data.drop('Class', axis=1)  # 'Class' is 1 for fraud, 0 for normal
labels = cleaned_data['Class']

# Step 4: Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2, stratify=labels)

# Step 5: Scale features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Step 6: Train machine learning model
model = RandomForestClassifier()
model.fit(X_train_scaled, y_train)

# Step 7: Make predictions
predictions = model.predict(X_test_scaled)

# Step 8: Evaluate the model
print(confusion_matrix(y_test, predictions))
print(classification_report(y_test, predictions))

# Step 9: Use model to detect fraud in new transactions
def detect_fraud(new_transaction):
    processed = preprocess_transaction(new_transaction)
    scaled = scaler.transform(processed)
    prediction = model.predict(scaled)
    if prediction == 1:
        return "Fraud detected"
    else:
        return "Transaction normal"
=======
# Import necessary libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix

# Step 1: Load dataset
data = load_csv("credit_card_transactions.csv")

# Step 2: Explore and clean data
# Handle missing values, check for imbalance, drop irrelevant columns
cleaned_data = preprocess(data)

# Step 3: Feature engineering and selection
# Extract features and labels
features = cleaned_data.drop('Class', axis=1)  # 'Class' is 1 for fraud, 0 for normal
labels = cleaned_data['Class']

# Step 4: Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2, stratify=labels)

# Step 5: Scale features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Step 6: Train machine learning model
model = RandomForestClassifier()
model.fit(X_train_scaled, y_train)

# Step 7: Make predictions
predictions = model.predict(X_test_scaled)

# Step 8: Evaluate the model
print(confusion_matrix(y_test, predictions))
print(classification_report(y_test, predictions))

# Step 9: Use model to detect fraud in new transactions
def detect_fraud(new_transaction):
    processed = preprocess_transaction(new_transaction)
    scaled = scaler.transform(processed)
    prediction = model.predict(scaled)
    if prediction == 1:
        return "Fraud detected"
    else:
        return "Transaction normal"
>>>>>>> origin/main
