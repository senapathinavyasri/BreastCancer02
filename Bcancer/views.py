 


# import os
# import joblib
# import numpy as np
# import logging
# from django.conf import settings
# from django.shortcuts import render, redirect
# from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.decorators import login_required
# from django.contrib import messages
# from .forms import SignupForm, CancerPredictionForm
# from .models import Prediction

# #from .models import Appointment, Patient

# # Configure logging
# logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger(__name__)

# # Load model and scaler
# MODEL_PATH = os.path.join(settings.BASE_DIR, "Bcancer", "models", "breast_cancer_model_5features.pkl")
# SCALER_PATH = os.path.join(settings.BASE_DIR, "Bcancer", "models", "scaler_5features.pkl")

# model, scaler = None, None  

# try:
#     model = joblib.load(MODEL_PATH)
#     scaler = joblib.load(SCALER_PATH)
    
#     if not hasattr(model, "predict"):
#         raise ValueError("❌ Loaded model is NOT a valid classifier!")

#     logger.info("✅ Model and Scaler loaded successfully!")

# except Exception as e:
#     logger.error(f"❌ Error loading Model/Scaler: {e}")

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
#             return redirect('login')
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

# # Cancer Prediction (Requires Login)
# @login_required
# def predict_cancer(request):
#     if model is None or scaler is None:
#         logger.error("❌ Model or Scaler is not loaded correctly!")
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

#                 logger.info(f"✅ Extracted Features: {features}")
#                 scaled_features = scaler.transform(features)
#                 logger.info(f"✅ Scaled Features: {scaled_features}")

#                 prediction = model.predict(scaled_features)
#                 logger.info(f"✅ Prediction Result: {prediction}")

#                 result = "M" if prediction[0] == 0 else "B"
                
#                 return render(request, 'result.html', {'result': result})

#             except Exception as e:
#                 logger.error(f"❌ Prediction Error: {e}")
#                 messages.error(request, f"❌ Prediction Error: {e}")
#                 return render(request, 'error.html', {'message': f"❌ Prediction Error: {e}"})

#     else:
#         form = CancerPredictionForm()

#     return render(request, 'predict.html', {'form': form})


# def food_recommendations(request):
#     return render(request, 'food_recommendations.html')

# def exercise_recommendations(request):
#     return render(request, 'exercise_recommendations.html')

# def doctor_consultation(request):
#     return render(request, 'doctor_consultation.html')

# def prediction_analysis(request):
#     return render(request, 'prediction_analysis.html')


#########################################################################################################


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
from .models import Prediction




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
##################################################################################################
# Cancer Prediction (Requires Login)
# @login_required
# def predict_cancer(request):
#     if model is None or scaler is None:
#         logger.error("❌ Model or Scaler is not loaded correctly!")
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

#                 logger.info(f"✅ Extracted Features: {features}")
#                 scaled_features = scaler.transform(features)
#                 logger.info(f"✅ Scaled Features: {scaled_features}")

#                 prediction = model.predict(scaled_features)
#                 logger.info(f"✅ Prediction Result: {prediction}")

#                 result = "Malignant" if prediction[0] == 0 else "Benign"

#                 # Save prediction to database
#                 Prediction.objects.create(
#                     user=request.user,
#                     mean_radius=form.cleaned_data['mean_radius'],
#                     mean_texture=form.cleaned_data['mean_texture'],
#                     mean_perimeter=form.cleaned_data['mean_perimeter'],
#                     mean_area=form.cleaned_data['mean_area'],
#                     mean_smoothness=form.cleaned_data['mean_smoothness'],
#                     result=result
#                 )

#                 return render(request, 'result.html', {'result': result, 'form': form})

#             except Exception as e:
#                 logger.error(f"❌ Prediction Error: {e}")
#                 messages.error(request, f"❌ Prediction Error: {e}")
#                 return render(request, 'error.html', {'message': f"❌ Prediction Error: {e}"})

#     else:
#         form = CancerPredictionForm()

#     return render(request, 'predict.html', {'form': form})
#######################################################################################################



@login_required
def predict_cancer(request):
    if model is None or scaler is None:
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

                scaled_features = scaler.transform(features)
                prediction = model.predict(scaled_features)
                result = "Malignant" if prediction[0] == 0 else "Benign"

                # Save prediction
                Prediction.objects.create(
                    user=request.user,
                    mean_radius=form.cleaned_data['mean_radius'],
                    mean_texture=form.cleaned_data['mean_texture'],
                    mean_perimeter=form.cleaned_data['mean_perimeter'],
                    mean_area=form.cleaned_data['mean_area'],
                    mean_smoothness=form.cleaned_data['mean_smoothness'],
                    result=result
                )

                return render(request, 'result.html', {'result': result, 'form': form})

            except Exception as e:
                messages.error(request, f"❌ Prediction Error: {e}")
                return render(request, 'error.html', {'message': f"❌ Prediction Error: {e}"})

    else:
        form = CancerPredictionForm()

    return render(request, 'predict.html', {'form': form})


# View user predictions (Requires Login)
@login_required
def user_predictions(request):
    predictions = Prediction.objects.filter(user=request.user).order_by('-timestamp')
    return render(request, 'user_predictions.html', {'predictions': predictions})



# Other Views
def food_recommendations(request):
    return render(request, 'food_recommendations.html')

def exercise_recommendations(request):
    return render(request, 'exercise_recommendations.html')

def doctor_consultation(request):
    return render(request, 'doctor_consultation.html')

def prediction_analysis(request):
    return render(request, 'prediction_analysis.html')

def user_dashboard(request):
    # Fetch predictions and order by latest created date
    predictions = Prediction.objects.all().order_by('-created_at').values(
        'created_at', 'mean_radius', 'mean_texture', 'mean_perimeter', 
        'mean_area', 'mean_smoothness', 'result'
    )

    # Count occurrences of 'Benign' and 'Malignant' for the pie chart
    benign_count = Prediction.objects.filter(result="Benign").count()
    malignant_count = Prediction.objects.filter(result="Malignant").count()

    context = {
        'predictions': predictions,
        'benign_count': benign_count,
        'malignant_count': malignant_count
    }

    return render(request, 'dashboard.html', context)

# @login_required
# def user_dashboard(request):
#     predictions = Prediction.objects.filter(user=request.user).order_by('-created_at')  # Fetch user's predictions
#     return render(request, 'dashboard.html', {'predictions': predictions})



def prediction_dashboard(request):
    # Count the number of benign and malignant predictions
    benign_count = Prediction.objects.filter(result='Benign').count()
    malignant_count = Prediction.objects.filter(result='Malignant').count()

    # Fetch all predictions to display in the table
    predictions = Prediction.objects.all().order_by('-created_at')

    # Pass data to the template
    context = {
        'predictions': predictions,
        'benign_count': benign_count,
        'malignant_count': malignant_count
    }
    return render(request, 'your_template_name.html', context)
