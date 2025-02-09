# Importing necessary libraries
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import pandas as pd
import sklearn.datasets
import joblib
import os

# Load Breast Cancer dataset
breast_cancer_dataset = sklearn.datasets.load_breast_cancer()

# Convert to DataFrame
data_frame = pd.DataFrame(breast_cancer_dataset.data, columns=breast_cancer_dataset.feature_names)

# Add the 'label' column (0 = Malignant, 1 = Benign)
data_frame['label'] = breast_cancer_dataset.target

# Select only the 5 required features
selected_features = ['mean radius', 'mean texture', 'mean perimeter', 'mean area', 'mean smoothness']
X = data_frame[selected_features]
Y = data_frame['label']

# Split into train and test sets
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=2)

# Standardizing (Scaling) the selected features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Train RandomForest model
rf_model = RandomForestClassifier(n_estimators=200, max_depth=10, class_weight='balanced', random_state=42)
rf_model.fit(X_train_scaled, Y_train)

# Define the correct path where Django will look for the model
model_dir = r"C:\Users\user\Desktop\FinalProject\Bcancer\models"

# Ensure the directory exists
if not os.path.exists(model_dir):
    os.makedirs(model_dir)

# Save the trained model and scaler correctly
model_path = os.path.join(model_dir, "breast_cancer_model_5features.pkl")
scaler_path = os.path.join(model_dir, "scaler_5features.pkl")

joblib.dump(rf_model, model_path)  # ✅ Save the model correctly
joblib.dump(scaler, scaler_path)  # ✅ Save the scaler

print(f"✅ Model saved at: {model_path}")
print(f"✅ Scaler saved at: {scaler_path}")

# Evaluate model accuracy
Y_train_pred = rf_model.predict(X_train_scaled)
Y_test_pred = rf_model.predict(X_test_scaled)

print("\n🔹 Model Performance:")
print("Training Accuracy:", accuracy_score(Y_train, Y_train_pred))
print("Test Accuracy:", accuracy_score(Y_test, Y_test_pred))
print("Classification Report:\n", classification_report(Y_test, Y_test_pred))

# Sample prediction
# input_data = [[17.99, 10.38, 122.8, 1001, 0.1184]]  # Example values for the 5 features
#  input_scaled = scaler.transform(input_data)
# prediction = rf_model.predict(input_scaled)

# print("\n🔹 Sample Prediction:")
# print(prediction[0])
# print("Prediction:", "Malignant" if prediction[0] == 0 else "Benign")
