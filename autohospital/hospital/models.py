from django.db import models



        

class Doctor_model (models.Model):
    Gender_CHOICES=(
          ('Male','Male'),
          ('Female','Female'),
          ('Trans','Trans')
    )
    speciality_choices = (
        ('Cancer',"Cancer"),
        ('Nephrologist',"Nephrologist"),
        ('Diabetes & Endocrinology',"Diabetes & Endocrinology"),
        ('cardiovascular',"cardiovascular"),
        ('Normal_Physician',"Normal_Physician")
    )
    full_name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.IntegerField()
    password = models.CharField(max_length=200)
    slug = models.SlugField(max_length=250,default="")
    age = models.IntegerField()
    sex = models.CharField(max_length=7,choices=Gender_CHOICES,default="Male")
    is_patient = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    speciality = models.CharField(max_length=200,choices=speciality_choices,default="Normal_Physician")

   
       


       

class Patient_model (models.Model):
    Gender_CHOICES=(
          ('Male','Male'),
          ('Female','Female'),
          ('Trans','Trans')
     )
    full_name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.IntegerField()
    age = models.IntegerField()
    problems = models.TextField()
    password = models.CharField(max_length=200)
    slug = models.SlugField(max_length=250,default="")
    medicine_given = models.TextField()
    sex = models.CharField(max_length=7,choices=Gender_CHOICES,default="Male")
    Primary_Physician=models.CharField(max_length=200)
    Previous_treatment = models.TextField()
    is_patient = models.BooleanField(default=True)
    is_active = models.BooleanField(default=False)


class Appointment (models.Model):
    full_name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.IntegerField()
    age = models.IntegerField()
    query = models.TextField()
    date = models.DateField()
    is_active = models.BooleanField(default=False)

   



  