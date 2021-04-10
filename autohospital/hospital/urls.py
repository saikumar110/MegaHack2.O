from django.urls import path,include
from . import views 

urlpatterns = [
   path("",views.homepage,name="homepage"),
   path("login/",views.login,name="login"),
   path("save_patient/",views.save_patient,name="save_patient"),
   path("covidbyName/",views.covidbyName,name="covidbyName"),
   path("covidbycountry/",views.covidbyCountry,name="covidbycountry"),
   path("appointment/",views.appointmnet,name="appointment"),
   path("appointment/",views.appointmnet,name="appointment"),
   path("facilities/",views.facilities,name="facilities"),
   path("about/",views.about,name="about"),
   path("cancer/",views.cancer,name="cancer"),
   path("heart/",views.heart,name="heart"),
   path("Malaria/",views.Malaria,name="Malaria"),
   path("Kidney/",views.Kidney,name="Kidney"),
   path("diabetes/",views.diabetes,name="diabetes"),
   path("liver/",views.liver,name="liver"),
   path("cancer_pre/",views.cancer_pre,name="cancer_pre"),
   path("Heart_pre/",views.Heart_pre,name="Heart_pre"),
   
  
   
]
