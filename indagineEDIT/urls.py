from django.urls import path, include
from rest_framework import routers
from indagineEDIT.api import views

router = routers.SimpleRouter()
router.register('data', views.DataView, 'data')

urlpatterns = [
	path('api/', include(router.urls)),
	path('api/gender/', views.GenderView.as_view(), name="gender"),
	path('api/alcohol/', views.AlcoholView.as_view(), name="alcohol"),
	path('api/drunk/', views.DrunkView.as_view(), name="drunk"),
	path('api/drugs/', views.DrugsView.as_view(), name="drugs"),
	path('api/accidents-lifestyle/', views.AccidentsLifeStyleView.as_view(), name="accidents lifestyle"),
	path('api/lifestyle/', views.LifeStyleView.as_view(), name="lifestyle"),
	path('api/bmi/', views.BMIView.as_view(), name="bmi"),
	path('api/smoke/', views.SmokeView.as_view(), name="smoke"),
	path('api/drove-with-drunk/', views.DroveWithDrunkView.as_view(), name="drove-with-drunk")
]
