from django.shortcuts import render
from django.http import HttpResponse
import pickle
import pathlib
import joblib
from .models import Appointment,Doctor_model,Patient_model
from .covid import getLatestCountryDataByName,getLatestCountryData
# Create your views here.


def homepage(request):

    return render (request,'index.html')


def login(request):
    doc=None
    try:
        doc =Doctor_model.objects.get(full_name=request.POST.get('logname'),password=request.POST.get('password'))
    except:
        pass
        
    
     
    if doc:
        
        #  Doctor_model.objects.get(full_name=request.POST.get('logname'),password=request.POST.get('password')):

        doc =Doctor_model.objects.get(full_name=request.POST.get('logname'),password=request.POST.get('password'))
        """     Getting Counts    """
        patients_count = Patient_model.objects.all().count()
        appointmnet_count =Appointment.objects.all().count()
        recov_pat = Patient_model.objects.filter(is_active=True).count()

        """    Getting Objects      """
        patients = Patient_model.objects.all()
        appointmnets = Appointment.objects.all

        """   Data Dict   """

        data = {

                "patients_count":patients_count,
                "appointmnet_count":appointmnet_count,
                "patients":patients,
                "appointmnets":appointmnets,
                "recov_pat":recov_pat,
                "doc":doc,}

        
        return render (request,'dashboard.html',data)
    else:
            print(request.POST.get('logname'))
            pat = Patient_model.objects.get(full_name=request.POST.get('logname'))
            if pat:
                pat_data = Patient_model.objects.filter(full_name=request.POST.get('logname'),password=request.POST.get('password'))
                data = {
                    "doc":pat,
                    "patients":pat_data,
                    "appointmnet_count":len(pat_data),
                }
                return render (request,'dashboard.html',data)
            else:
                return HttpResponse("patin")
            

def save_patient(request):
    pat = Patient_model(full_name=request.GET['name'],email=request.GET['email'],phone=request.GET['phone'],
    age=request.GET['Age'],problems=request.GET['problems'],password=request.GET['password'],medicine_given=request.GET['medicine'],sex=request.GET['sex'],
    Primary_Physician=request.GET['Primary']
    )
    pat.save()
    return HttpResponse("Patient Data Added")


def covidbyName(request):

    return HttpResponse(getLatestCountryDataByName('India'))

def covidbyCountry(request):

    return HttpResponse(getLatestCountryData())

def appointmnet(request):
   
    name = request.GET['name']
    email =request.GET['email']
    age =request.GET['age']
    number=request.GET['number']
    query = request.GET['query']
    date = request.GET['date']

    """  create object """
    appoint = Appointment(full_name=name,email=email,age=age,query=query,date=date,phone=number)
    appoint.save()
    return HttpResponse("got data")
    
""" ----------------------------------------Special Facilities--------------------------------------- """



def cancer(request):

    return render (request,'models/index.html')

def cancer_pre(request):
    

    data=[1,request.GET['Area'],request.GET['Radius'],request.GET['Perimeter'],request.GET['Concavity']]
    print(data)
    filename = "cancer_model.pkl"

    loaded_model = joblib.load(r"C:\Users\Dell\Desktop\MegaHack\autohospital\hospital\templates\models\cancer_model.pkl") # loading the model file from the storage
    # predictions using the loaded model file
    prediction=loaded_model.predict([data])
    if prediction[0] ==1:
        return HttpResponse("There are High Chances Of Getting Cancer")
    else:
        return HttpResponse("There are low Chances Of Getting Cancer")


def heart(request):

    return render (request,'models/Heart.html')

def Heart_pre(request):

    data=[request.GET['Cp'],request.GET['trestbps'],request.GET['chol'],request.GET['fbs'],request.GET['thalach'],request.GET['exang'],request.GET['restecg']]
    print(data)
    filename = "cancer_model.pkl"

    loaded_model = joblib.load(r"C:\Users\Dell\Desktop\MegaHack\autohospital\hospital\templates\models\cancer_model.pkl") # loading the model file from the storage
    # predictions using the loaded model file
    prediction=loaded_model.predict([data])
    if prediction[0] ==1:
        return HttpResponse("There are High Chances Of Getting Cancer")
    else:
        return HttpResponse("There are low Chances Of Getting Cancer")

    return render (request,'models/Heart.html')

def Malaria(request):

    return render (request,'models/Malaria.html')

def Kidney(request):

    return render (request,'models/kidney.html')

def diabetes(request):

    return render (request,'models/diabetes.html')


def liver(request):

    return render (request,'models/liver.html')






""" --------------Serving Pagesx--------------- """

def facilities(request):

    return render(request,'facilities.html')

def about(request):


    return render(request,'about.html')