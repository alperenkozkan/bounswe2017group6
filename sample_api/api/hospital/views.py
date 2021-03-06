from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import *
import json

# Create your views here.
@csrf_exempt
def doctor(request):
    if request.method == 'GET':
        return JsonResponse({"asd":"asd"})

@csrf_exempt
def doctor_single(request, doctor_id):
    if request.method == "GET":
        print(request)
        doctor = Doctor.objects.filter(id=int(doctor_id))
        if doctor.exists():
            doctor = doctor.first()
        return JsonResponse({"name":doctor.name, "lastname":doctor.lastname, "age":doctor.age})

    elif request.method == "POST":
        pass
    
    elif request.method=="DELETE":
        doctor = Doctor.objects.filter(id=int(doctor_id))
        if doctor.exists():
            doctor.delete()
            return JsonResponse({"status":"OK", "message":""})
        else:
            return JsonResponse({"status":"FAIL", "message":"doctor does not exist"})

@csrf_exempt
def patient_single(request, patient_id):
    if request.method == "GET":
        print(request)
        patient = Patient.objects.filter(id=int(patient_id))
        if patient.exists():
            patient = patient.first()
        else:
            return JsonResponse({"status":"FAIL", "message":"patient does not exist"})
        return JsonResponse({"name":patient.name, "lastname":patient.lastname, "age":patient.age})

    elif request.method == "PUT":
        data = json.loads(request.body.decode("utf-8"))
        patient = Patient.objects.filter(id=int(patient_id))
        if patient.exists():
            patient = patient.first()
        else:
            return JsonResponse({"status":"FAIL", "message":"patient does not exist"})
        try:
            if "age" in data:
                patient.age = data["age"]
            if "name" in data:
                patient.name = data["name"]
            if "lastname" in data:
                patient.lastname = data["lastname"]
            patient.save()
        except:
            return JsonResponse({"status":"FAIL", "message":"missing field"})
        return JsonResponse({"status":"OK", "message":""})
    elif request.method=="DELETE":
        patient = Patient.objects.filter(id=int(patient_id))
        if patient.exists():
            patient.delete()
            return JsonResponse({"status":"OK", "message":""})
        else:
            return JsonResponse({"status":"FAIL", "message":"patient does not exist"})

@csrf_exempt
def department(request):
	print(request)

@csrf_exempt
def department_single(request, department_id):
	if request.method == "GET":
		print(request)
		department = Department.objects.filter(id = int(department_id))
		if department.exists():
			department = department.first()
		return JsonResponse({"name": department.name})
	
	elif request.method == "PUT":
		data = json.loads(request.body.decode("utf-8"))
		department = Department.objects.filter(id = int(department_id))
		if department.exists():
			department = department.first()
		else:
			return JsonResponse({"status":"FAIL", "message":"department does not exist"})
		try:
			if "name" in data:
				department.name = data["name"]
			department.save()
		except:
			return JsonResponse({"status": "FAIL", "message": "missing field"})
		return JsonResponse({"status":"OK", "message":""})

	elif request.method == "DELETE":
						department = Department.objects.filter(id = int(department_id))
						if department.exists():
								return JsonResponse({"status":"OK", "message":""})
						else:
								return JsonResponse({"status":"FAIL", "message":"department does not exist"})
														 

@csrf_exempt
def patient(request):
    print("patient")
    if request.method == "GET":
        pass
    elif request.method == "POST":
        print("post patient")
        try:
            data = json.loads(request.body.decode("utf-8"))
            patient = Patient.objects.create(name=data["name"], lastname=data["lastname"], age=data["age"])
            patient.save()
            return JsonResponse({"status":"OK", "message":""})
        except Exception as e:
            print("wrong format!!!!!\n\n\n\n")
            return JsonResponse({"status":"FAIL", "message":"wrong data format"})
