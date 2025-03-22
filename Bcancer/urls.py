

from django.urls import path
# from Bcancer.views import signup, login_view, logout_view, home, predict_cancer
from Bcancer.views import *

# urlpatterns = [
#     path('signup/', signup, name='signup'),  # Correct function name
#     path('login/', login_view, name='login'),
#     path('logout/', logout_view, name='logout'),
#     path('', home, name='home'),  # Set home page correctly
#     path('predict/', predict_cancer, name='predict_cancer'),
# ]

from django.contrib import admin
from django.urls import path
from Bcancer.views import signup, login_view, logout_view, home, predict_cancer, food_recommendations, exercise_recommendations, doctor_consultation,prediction_analysis
from .views import predict_cancer, user_dashboard

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('signup/', signup, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('predict/', predict_cancer, name='predict_cancer'),
    path('food-recommendations/', food_recommendations, name='food_recommendations'),
    path('exercise-recommendations/', exercise_recommendations, name='exercise_recommendations'),
    path('doctor-consultation/', doctor_consultation, name='doctor_consultation'),
    path('prediction-analysis/', prediction_analysis, name='prediction_analysis'),
    path("predict/", predict_cancer, name="predict_cancer"),
    path('dashboard/', user_dashboard, name="dashboard"),

    #path("dashboard/", user_dashboard, name="dashboard"), 
    #path('doctor/dashboard/', doctor_dashboard, name='doctor_dashboard'),
]