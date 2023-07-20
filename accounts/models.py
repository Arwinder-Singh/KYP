from django.db import models

# Create your models here.
class Tag(models.Model):
        tag_name=models.CharField(max_length=30)
        tag_hint=models.TextField(null=True,blank=True)
        
        
        def __str__(self):
            return self.tag_name
        
class Profile(models.Model):
    name=models.CharField(max_length=30)
    department=models.CharField(max_length=10)
    mainRating=models.FloatField(null=True,blank=True,default=0)
    post=models.CharField(max_length=20)
    pic=models.ImageField(upload_to="profile_pic/",default="default.png")
    email=models.EmailField()
    ph_num=models.IntegerField(null=True)
    
    
    def __str__(self):
        return self.name+"                            "+self.department
    
class Rate(models.Model):
    profile=models.ForeignKey(Profile,on_delete=models.CASCADE,related_name='profile')
    GetreadytodoworkRating=models.FloatField(null=True,blank=True,default=None)
    SkipclassyouwillnotpassRating=models.FloatField(null=True,blank=True,default=None)
    ClarityRating=models.FloatField(null=True,blank=True,default=None)
    TimelyteacherRating=models.FloatField(null=True,blank=True,default=None)
    ControlfreakRating=models.FloatField(null=True,blank=True,default=None)
    ToughGraderRating=models.FloatField(null=True,blank=True,default=None)
    BewareofquestioningRating=models.FloatField(null=True,blank=True,default=None)
    LectureheavyRating=models.FloatField(null=True,blank=True,default=None)
    NotesprovidedRating=models.FloatField(null=True,blank=True,default=None)
    ExtraactivitiesRating=models.FloatField(null=True,blank=True,default=None)
  
    
    
class AvgRating(models.Model):
    profile=models.OneToOneField(Profile,on_delete=models.CASCADE,related_name='avg_profile',primary_key=True,)
    avgAssignmentsRating=models.FloatField(null=True,blank=True,default=0)
    avgAttendanceRating=models.FloatField(null=True,blank=True,default=0)
    avgClarityRating=models.FloatField(null=True,blank=True,default=0)
    avgTimingRating=models.FloatField(null=True,blank=True,default=0)
    avgControlRating=models.FloatField(null=True,blank=True,default=0)
    avgGraderRating=models.FloatField(null=True,blank=True,default=0)
    avgQuestioningRating=models.FloatField(null=True,blank=True,default=0)
    avgLectureRating=models.FloatField(null=True,blank=True,default=0)
    avgNotesRating=models.FloatField(null=True,blank=True,default=0)
    avgActivitiesRating=models.FloatField(null=True,blank=True,default=0)
    
    
    
    
    

    
    
    
        