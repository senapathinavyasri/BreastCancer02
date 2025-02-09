# import os
# import joblib
# import numpy as np
# from django.conf import settings
# from django.shortcuts import render, redirect
# from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.decorators import login_required
# from django.contrib import messages
# from .forms import SignupForm, CancerPredictionForm

# # Load model and scaler
# MODEL_PATH = os.path.join(settings.BASE_DIR, "Bcancer", "models", "breast_cancer_model_5features.pkl")
# SCALER_PATH = os.path.join(settings.BASE_DIR, "Bcancer", "models", "scaler_5features.pkl")

# model, scaler = None, None  

# try:
#     model = joblib.load(MODEL_PATH)
#     scaler = joblib.load(SCALER_PATH)
    
#     if not hasattr(model, "predict"):
#         raise ValueError("❌ Loaded model is NOT a valid classifier!")

#     print("✅ Model and Scaler loaded successfully!")

# except Exception as e:
#     print(f"❌ Error loading Model/Scaler: {e}")

# # Home page
# def home(request):
#     return render(request, 'home.html')

# # User Signup
# def signup(request):
#     if request.method == "POST":
#         form = SignupForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, "Account created successfully! Please log in.")
#             return redirect('login')  # Redirects to login page after signup
#         else:
#             messages.error(request, "Signup failed! Please correct the errors.")

#     else:
#         form = SignupForm()
    
#     return render(request, 'signup.html', {'form': form})

# # User Login
# def login_view(request):
#     if request.method == "POST":
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = authenticate(request, username=username, password=password)

#         if user is not None:
#             login(request, user)
#             messages.success(request, "Login successful!")
#             return redirect('predict_cancer')
#         else:
#             messages.error(request, "Invalid username or password!")

#     return render(request, 'login.html')

# # User Logout
# def logout_view(request):
#     logout(request)
#     messages.success(request, "Logged out successfully!")
#     return redirect('home')

# @login_required

# import logging

# # Define the logger
# logger = logging.getLogger(__name__)

# def predict_cancer(request):
#     if model is None or scaler is None:
#         return render(request, 'error.html', {'message': '❌ Model or Scaler is not loaded correctly!'})

#     if request.method == "POST":
#         form = CancerPredictionForm(request.POST)
#         if form.is_valid():
#             try:
#                 features = np.array([
#                     form.cleaned_data['mean_radius'],
#                     form.cleaned_data['mean_texture'],
#                     form.cleaned_data['mean_perimeter'],
#                     form.cleaned_data['mean_area'],
#                     form.cleaned_data['mean_smoothness']
#                 ]).reshape(1, -1)

#                 logger.info(f"Features before scaling: {features}")  # Debugging
#                 scaled_features = scaler.transform(features)
#                 logger.info(f"Scaled features: {scaled_features}")  # Debugging
                
#                 prediction = model.predict(scaled_features)
#                 logger.info(f"Raw model output: {prediction}")  # Debugging

#                 result = "Malignant (Cancer Detected)" if prediction[0] == 0 else "Benign (No Cancer)"
#                 return render(request, 'result.html', {'result': result})

#             except Exception as e:
#                 logger.error(f"Prediction error: {e}")
#                 messages.error(request, f"❌ Prediction error: {e}")
#                 return render(request, 'error.html', {'message': f"❌ Prediction error: {e}"})

#     else:
#         form = CancerPredictionForm()

#     return render(request, 'predict.html', {'form': form})


import os
import joblib
import numpy as np
import logging
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import SignupForm, CancerPredictionForm

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load model and scaler
MODEL_PATH = os.path.join(settings.BASE_DIR, "Bcancer", "models", "breast_cancer_model_5features.pkl")
SCALER_PATH = os.path.join(settings.BASE_DIR, "Bcancer", "models", "scaler_5features.pkl")

model, scaler = None, None  

try:
    model = joblib.load(MODEL_PATH)
    scaler = joblib.load(SCALER_PATH)
    
    if not hasattr(model, "predict"):
        raise ValueError("❌ Loaded model is NOT a valid classifier!")

    logger.info("✅ Model and Scaler loaded successfully!")

except Exception as e:
    logger.error(f"❌ Error loading Model/Scaler: {e}")

# Home page
def home(request):
    return render(request, 'home.html')

# User Signup
def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully! Please log in.")
            return redirect('login')
        else:
            messages.error(request, "Signup failed! Please correct the errors.")
    
    else:
        form = SignupForm()
    
    return render(request, 'signup.html', {'form': form})

# User Login
def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Login successful!")
            return redirect('predict_cancer')
        else:
            messages.error(request, "Invalid username or password!")

    return render(request, 'login.html')

# User Logout
def logout_view(request):
    logout(request)
    messages.success(request, "Logged out successfully!")
    return redirect('home')

# Cancer Prediction (Requires Login)
@login_required
def predict_cancer(request):
    if model is None or scaler is None:
        logger.error("❌ Model or Scaler is not loaded correctly!")
        return render(request, 'error.html', {'message': '❌ Model or Scaler is not loaded correctly!'})

    if request.method == "POST":
        form = CancerPredictionForm(request.POST)
        if form.is_valid():
            try:
                features = np.array([
                    form.cleaned_data['mean_radius'],
                    form.cleaned_data['mean_texture'],
                    form.cleaned_data['mean_perimeter'],
                    form.cleaned_data['mean_area'],
                    form.cleaned_data['mean_smoothness']
                ]).reshape(1, -1)

                logger.info(f"✅ Extracted Features: {features}")
                scaled_features = scaler.transform(features)
                logger.info(f"✅ Scaled Features: {scaled_features}")

                prediction = model.predict(scaled_features)
                logger.info(f"✅ Prediction Result: {prediction}")

                result = "M" if prediction[0] == 0 else "B"
                
                return render(request, 'result.html', {'result': result})

            except Exception as e:
                logger.error(f"❌ Prediction Error: {e}")
                messages.error(request, f"❌ Prediction Error: {e}")
                return render(request, 'error.html', {'message': f"❌ Prediction Error: {e}"})

    else:
        form = CancerPredictionForm()

    return render(request, 'predict.html', {'form': form})
