# from asyncio.windows_events import NULL
# from multiprocessing.context import assert_spawning
# from tkinter import Entry
from django.shortcuts import render,redirect,reverse
from django.contrib import messages
from accounts.models import Profile,Tag,Rate,AvgRating
from django.core.paginator import Paginator

from django.http import JsonResponse,HttpResponse
import json
from .forms import rateForm

# Create your views here.
def index(request):
        return render(request,'index.html')

def dept(request,department):
    data=Profile.objects.filter(department=department)
    page=Paginator(data,6)
    
    page_list=request.GET.get('page')
    
    
    page=page.get_page(page_list)
    
    return render(request,'dept.html',{"page":page,'department':department})    

def team(request):
    return render(request,'team.html') 

def contact(request):
    return render(request,'contact.html') 

def temp(request):
    if request.method=="POST":
        name=request.POST.get("product")
        
        info=Profile.objects.filter(name__icontains= name)
        page=Paginator(info,6)
    
        page_list=request.GET.get('page')
    
    
        page=page.get_page(page_list)
        
        
        if info.count()==0:
            messages.warning(request,"no profile exists")
        tags=Tag.objects.all()
        profileID=0
        for i in info:
            profileID=i.id   
           
        avgTags=list(AvgRating.objects.filter(profile_id=profileID).values_list('avgAssignmentsRating','avgAttendanceRating','avgClarityRating','avgTimingRating'))
        colTags= list(zip(*avgTags))
        tagInfo=zip(tags,colTags)
        
        # return redirect('profile',pk=profileID)
        return render(request,'dept.html',{"page":page,"department":"Search results"})      
    return render(request,"search.html")
    
def profile(request,pk):
    lists=["get ready to do work","skip class you won't pass","clarity","timely teacher","Control freak","Tough Grader","Beware of questioning","Lecture heavy","Notes provided","Extra activities"]
    info=Profile.objects.filter(id=pk)
    tags=Tag.objects.all()
   
 
        


    avgTags=list(AvgRating.objects.filter(profile_id=pk).values_list('avgAssignmentsRating','avgAttendanceRating','avgClarityRating','avgTimingRating','avgControlRating','avgGraderRating','avgQuestioningRating','avgLectureRating','avgNotesRating','avgActivitiesRating'))
    colTags= list(zip(*avgTags))
    tagInfo=zip(tags,colTags)
    print('form is not valid')
    if request.method=="POST":
        print('form is valid')
        form=rateForm(request.POST)
        if form.is_valid():
            
            data=Rate()
            data.GetreadytodoworkRating=form.cleaned_data['GetreadytodoworkRating']
            data.SkipclassyouwillnotpassRating=form.cleaned_data['SkipclassyouwillnotpassRating']
            data.ClarityRating=form.cleaned_data['ClarityRating']
            data.TimelyteacherRating=form.cleaned_data['TimelyteacherRating']
            data.ControlfreakRating=form.cleaned_data['ControlfreakRating']
            data.ToughGraderRating=form.cleaned_data['ToughGraderRating']
            data.BewareofquestioningRating=form.cleaned_data['BewareofquestioningRating']
            data.LectureheavyRating=form.cleaned_data['LectureheavyRating']
            data.NotesprovidedRating=form.cleaned_data['NotesprovidedRating']
            data.ExtraactivitiesRating=form.cleaned_data['ExtraactivitiesRating']
            data.profile_id=pk
            
            
            if data.GetreadytodoworkRating == None or data.SkipclassyouwillnotpassRating == None or data.ClarityRating == None or data.TimelyteacherRating == None or data.ControlfreakRating == None or data.ToughGraderRating == None or data.BewareofquestioningRating == None or data.LectureheavyRating == None or data.NotesprovidedRating == None or data.ExtraactivitiesRating == None:
                messages.warning(request,"Rate every tag")
                
                
            else:
                
                data.save()
                
                

                
                

            

                ratings=[data.GetreadytodoworkRating,data.SkipclassyouwillnotpassRating,data.ClarityRating,data.TimelyteacherRating,data.ControlfreakRating,data.ToughGraderRating,data.BewareofquestioningRating,data.LectureheavyRating,data.NotesprovidedRating,data.ExtraactivitiesRating]
                

                records=Rate.objects.filter(profile_id=pk).count()

                is_record=True
                try:
                    entry=AvgRating.objects.get(profile_id=pk)
                    
                except:
                    is_record=False

                if is_record:
                    avgRatings=[entry.avgAssignmentsRating,entry.avgAttendanceRating,entry.avgClarityRating,entry.avgTimingRating,entry.avgControlRating,entry.avgGraderRating,entry.avgQuestioningRating,entry.avgLectureRating,entry.avgNotesRating,entry.avgActivitiesRating]
                else:
                    avgRatings=[0,0,0,0,0,0,0,0,0,0]   
                
                
                newAvg=[]
                
                for value,avgOld in zip(ratings,avgRatings):
                    avgNew=avgOld+(value-avgOld)/records 
                    newAvg.append(round(avgNew,1))
                
                avg_mainRating=sum(newAvg)/10;
                profile=Profile.objects.get(id=pk)
                profile.mainRating=round(avg_mainRating,1)
                profile.save()
                    
                avgdata=AvgRating(avgAssignmentsRating=newAvg[0],avgAttendanceRating=newAvg[1],avgClarityRating=newAvg[2],avgTimingRating=newAvg[3],avgControlRating=newAvg[4],avgGraderRating=newAvg[5],avgQuestioningRating=newAvg[6],avgLectureRating=newAvg[7],avgNotesRating=newAvg[8],avgActivitiesRating=newAvg[9],profile_id=pk)

                avgdata.save()
                
                return redirect(random,pk)
      
        
    return render(request,'profile.html',{'pk':pk,'info':info,"tags":tags,"tagInfo":tagInfo,}) 

def get_names(request):
    payload=list()
    
    if "term" in request.GET:
        
        objs=Profile.objects.filter(name__icontains=request.GET.get('term'))
        if objs:
            for obj in objs:
                payload.append(obj.name)
        else:
            payload.append('No results found')
    # name=request.GET.get('name')
    # payload=[]
    # if name:
    #    objs=Profile.objects.filter(name__icontains=name)
    #    for obj in objs:
    #        payload.append(obj.name)
    
    return  JsonResponse(payload,safe=False)


def random(request,key):
    return redirect(profile,key)
      
 


   