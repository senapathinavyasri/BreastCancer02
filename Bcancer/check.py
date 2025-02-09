import joblib
model = joblib.load("C:/Users/user/Desktop/FinalProject/Bcancer/models/breast_cancer_model_5features.pkl")
scaler = joblib.load("C:/Users/user/Desktop/FinalProject/Bcancer/models/scaler.pkl")

print("Model type:", type(model))
print("Scaler type:", type(scaler))
