from django.shortcuts import render, redirect
from django import forms
from django.http import HttpResponse
from django.contrib.auth.models import User, auth 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.messages import constants as messages
from .models import Riddle, Submit, serial
from django.core.files.storage import FileSystemStorage
from os.path import isfile, join
from os import listdir

def serial_start(request):
    ser = serial()
    ser.save()
    return (redirect, "/accounts/refresh")


def login(request):
    if request.method == "POST":
        # print(request.method)
        team_id = request.POST['username']
        password = request.POST['password']
        # print(team_id)

        user = auth.authenticate(username = team_id, password = password)

        if user is not None:
            auth.login(request,user)
            if team_id == 'aswin':
                return redirect('/admin_use/show')
            else:
                return redirect('/accounts/puzzle')
        else:
            #messages.info(request,'invalid credentials')
            return render(request, "login.html")
    else:
        return render(request, "login.html")

mypath = "./static/puzzles"

def file_names():
    return [f for f in listdir(mypath) if isfile(join(mypath, f))]


def register(request):
    if request.user.is_superuser:
        if request.method == "POST":
            print(request.method)
            team_id = request.POST['username']
            password1 = request.POST['password1']
            password2 = request.POST['password2']
            leader = request.POST['Leader_name']
            #print(team_id, password2,password1)
            if password1 == password2:
                user = User.objects.create_user(username = team_id, password= password1)
                user.save()
                print('user created')
                files = file_names()
                k = len(files)
                for i in range(k):
                    isOpen = False
                    if i<10:
                        isOpen = True
                    Riddle.objects.create(lead = leader, num = i+1, img = files[i], team = team_id, numAttemp = 0, isSolved = 0, isOpen = isOpen, score = 0,sub = 0, mag_c=3)
                return redirect('/accounts/login')
            else:
                # print("pass not matched") 
                return redirect('/')
        else:
            return render(request, "registration.html")
    else:
        return redirect('/')

def logout(request):
    auth.logout(request)
    return redirect('/')

def str2int(val):
    # Using list comprehension 
    output = [int(x) if x.isdigit() else x  
          for z in val for x in str(z)]
    return output

def refresh(request):
    return redirect('/accounts/puzzle')

def puzzle(request):
    if request.user.username:
        if request.method == 'POST' and request.FILES['myfile']:
            myfile = request.FILES['myfile']
            fs = FileSystemStorage()
            ser = serial.objects.get(pk = 1)
            name = str(ser.serial) + '_' + request.user.username+'_'+request.POST['riddle']+'.'+myfile.name.split('.')[-1]
            ser.serial += 1
            ser.save()
            fs.save(name, myfile)
            nam = Submit()
            nam.u_show = name
            nam.r_num = request.POST['riddle']
            nam.r_team = request.user.username
            nam.save()
            rid_n = request.POST['riddle']
            puz = Riddle.objects.get(team=request.user.username, isOpen = True, num = rid_n)
            puz.sub +=1
            puz.save()
            return redirect('/accounts/refresh')
        
        team = request.user.username
        riddles = list(Riddle.objects.filter(team=request.user.username, isOpen = True))
        j = Riddle.objects.get(team=request.user.username, num = 1)
        j = j.mag_c
        score = 0
        sol = 0
        for rid in riddles:
            score += rid.score
            sol += rid.isSolved
        return render(request, "index.html", {'riddles' : riddles, 'team': team , 'score' : score, 'sol' : sol, 'j' : j} )
    else:
        return redirect('/')

import random

def magic_card(request):
    # riddles = list(Riddle.objects.filter(team=request.user.username))
    a = Riddle.objects.get(team=request.user.username, num = 1)
    if a.mag_c > 0:
        # for rid in riddles:
        #     rid.mag_c -= 1
        #     rid.save()
        a.mag_c -= 1
        a.save()
        rid = list(Riddle.objects.filter(team = request.user.username, isOpen = False))
        l = len(rid)
        a = [i+1 for i in range(l)]
        rid = rid[random.choice(a)]
        rid.isOpen = True
        rid.save()
    return redirect("/accounts/puzzle")
