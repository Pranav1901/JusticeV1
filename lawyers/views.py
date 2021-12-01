from django.shortcuts import redirect, render
from django.http.response import JsonResponse
from rest_framework import serializers
from .models import LawyerSpecilization, Lawyers
from rest_framework.decorators import action, api_view
from rest_framework.response import Response
from .serialzers import allSerailizer, allSerailizerread,allSpecilizationSerailizer
from .forms import LawyerForm, SpecializationForm

#-----------------LIST VIEWS--------------------
@api_view(['GET'])
def all(request):
    lawyers = Lawyers.objects.all()
    serializers = allSerailizer(lawyers,many=True)
    return Response(serializers.data)

@api_view(['GET'])
def allS(request):
    specilization = LawyerSpecilization.objects.all()
    serializers = allSpecilizationSerailizer(specilization,many=True)
    return Response(serializers.data)

#-----------------FILTER VIEWS--------------------
@api_view(['GET','POST'])
def location(request, pk):
    lawyers = Lawyers.objects.filter(Location=pk)
    serialzers = allSerailizer(lawyers,many=True)
    return Response(serialzers.data)
@api_view(['GET','POST'])
def casetype(request,pk):
    lawyers = Lawyers.objects.filter(specilization=pk)
    serializers = allSerailizer(lawyers,many=True)
    return Response(serializers.data)

@api_view(['GET'])
def ncasetype(request,pk):
   #  print(pk)
    lawyer = LawyerSpecilization.objects.filter(SpecilizationType=pk)
    serializers = allSerailizerread(lawyer,many=True)
   # print(lawyer[0])
    return Response(serializers.data)
#-----------------SPECIFIC  VIEW--------------------
@api_view(['GET'])
def lawyer(request,pk):
    lawyer = Lawyers.objects.get(id=pk)
    serializers = allSerailizer(lawyer,many=False)
    return Response(serializers.data)

@api_view(['GET'])
def specialization(request,pk):
    specialization = LawyerSpecilization.objects.get(id=pk)
    serializers = allSpecilizationSerailizer(specialization,many=False)
    return Response(serializers.data)



#-----------------DELETE-------------------------
def deletelawyer(request,pk):
    lawyer = Lawyers.objects.get(id=pk)
    lawyer.delete()
    return redirect('/lawyers/all')

def deleteSpecilization(request,pk):
    specilization = LawyerSpecilization.objects.get(id=pk)
    specilization.delete()
    return redirect('/lawyers/allS')


#-----------------ADD --------------------
def addlawyer(request):
    action ='create'
    form = LawyerForm()
    if request.method == 'POST':
        print(request.POST)
        form =LawyerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/lawyers/all')
    context ={'action':action,'form':form}
    return render(request,'form.html',context)

def addSpecialization(request):
    action = 'create'
    form = SpecializationForm()
    if request.method == 'POST':
        form = SpecializationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/lawyers/allS')
    context = {'action':action,'form':form}
    return  render(request,'form.html',context)

#-----------------UPDATE--------------------
def updateLawyer(request,pk):
    action = 'update'
    lawyer = Lawyers.objects.get(id=pk)
    form = LawyerForm(instance=lawyer)

    if request.method =='POST':
        form = LawyerForm(request.POST,instance=lawyer)
        if form.is_valid():
            form.save()
            return redirect('/lawyers/lawyer/ ' + str(lawyer.id))

    context = {'action':action, 'form':form}
    return render(request, 'form.html',context)

def updateSpecialization(request,pk):
    action = 'update'
    specialization = LawyerSpecilization.objects.get(id=pk)
    form = SpecializationForm(instance=specialization)

    if request.method =='POST':
         form = SpecializationForm(request.POST,instance=specialization)
         if form.is_valid():
             form.save()
             return redirect('/lawyers/specialization/' + str(specialization.id))

    context = {'action':action, 'form':form}
    return render(request, 'form.html',context)

