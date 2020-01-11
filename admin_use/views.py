from django.shortcuts import render, redirect
from django.http import HttpResponse
from os import listdir
from os.path import isfile, join
import os, shutil
import random
from accounts.models import Riddle
from .models import record

# Create your views here.

mypath = "./media/"
destpath = "./static/submit/"

def mov_file(name):
    source = mypath + name
    destination = destpath + name
    shutil.move(source, destination)

def file_names(my_path):
    return [f for f in listdir(my_path) if isfile(join(my_path, f))]

def refresh(request):
    return redirect('/admin_use/show')

def show(request):
    if request.user.is_superuser:
        fil = file_names(mypath)
        for f in fil:
            mov_file(f)
        if request.method == "POST":
            riddle = request.POST["num"]
            team = request.POST["team"]
            file = request.POST["file"]
            if request.POST["ans"] == 'yes':
                rid = Riddle.objects.get(team = team, num = riddle)
                if rid.numAttemp == 0:
                    rid.score += 10
                elif rid.numAttemp == 1:
                    rid.score += 7
                elif rid.numAttemp == 2:
                    rid.score += 5
                rid.isSolved = True
                rid.numAttemp += 1
                att = rid.numAttemp
                leader = rid.lead
                rid.save()
                l = len(list(Riddle.objects.filter(team = team, isOpen = False)))
                a = [i+1 for i in range(l)]
                rid = list(Riddle.objects.filter(team = team, isOpen = False))[random.choice(a)]
                rid.isOpen = True

                record.objects.create(team = team, attemp = att, puzz = riddle, leader = leader)
                
            else:
                rid = Riddle.objects.get(team = team, num = riddle)
                rid.numAttemp += 1
                rid.save()
            rid.save()
            os.remove(destpath + file)
            return redirect('/admin_use/refresh')
        arr = []
        class card:
            num : int
            team : str
            img : str
        files = file_names(destpath)
        for f in files:
            rid = card()
            rid.num = (f.split('.')[0]).split('_')[-1]
            rid.team = (f.split('.')[0]).split('_')[1]
            rid.img = f
            arr.append(rid)
        print(arr)
        solved = list(record.objects.filter())
        return render(request,'show.html', {'arr': arr, 'solved' : solved})

    else:
        return HttpResponse("<h1>Aap chu**ya ho</h1>")















'''
def mov_file(name):
    source = mypath + name
    destination = mypath + name
    shutil.move(source, destination)
    #os.remove(mypath + name)
    #os.rename('/Users/billy/d1/xfile.txt', '/Users/billy/d2/xfile.txt')


'''