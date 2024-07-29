import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
import joblib

# Load the data
data = pd.read_csv('cleaned_loan_data.csv')

# Define feature columns and target column
features = ['Married', 'Dependents', 'Education', 'Self_Employed', 'TotalIncome',
            'LoanAmount', 'Loan_Amount_Term', 'Credit_History', 'Property_Area']
target = 'Loan_Status'

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(data[features], data[target], test_size=0.2, random_state=42)

# Define preprocessing steps
preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), ['TotalIncome', 'LoanAmount', 'Loan_Amount_Term']),
        ('cat', OneHotEncoder(), ['Married', 'Dependents', 'Education', 'Self_Employed', 'Credit_History', 'Property_Area'])
    ]
)

# Define the model pipeline
model_pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('classifier', RandomForestClassifier(random_state=42))
])

# Train the model
model_pipeline.fit(X_train, y_train)

# Step 3: Make predictions and evaluate the model
y_pred = model_pipeline.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.2f}")

print("Classification Report:")
print(classification_report(y_test, y_pred))

# Cross-validation with KFold
kfold = KFold(n_splits=5, shuffle=True, random_state=42)
cv_scores = cross_val_score(model_pipeline, X, y, cv=kfold, scoring='accuracy')

print(f"Cross-validation scores: {cv_scores}")
print(f"Mean cross-validation score: {cv_scores.mean():.2f}")

# Save the preprocessor and model
joblib.dump(preprocessor, 'loan_preprocessor.pkl')
joblib.dump(model_pipeline, 'best_rf_model.pkl')
