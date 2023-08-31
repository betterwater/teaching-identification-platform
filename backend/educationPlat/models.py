from django.db import models

# Create your models here.
class Users(models.Model):
    userName = models.CharField(null=False, max_length=50)
    userAccount = models.CharField(null=False, unique=True, max_length=50)
    userPassword = models.CharField(null=False, max_length=50)

class FosterPlan(models.Model):
    facility = models.CharField(null=False, max_length=50)
    subject = models.CharField(null=False, max_length=50)
    year = models.CharField(null=False, max_length=50)
    briefInfo = models.TextField(null=False)
    subjectDescription = models.TextField(null=False)
    evaluationMechanism = models.TextField(null=False)

class CultivationGoal(models.Model):
    facility = models.CharField(null=False, max_length=50)
    subject = models.CharField(null=False, max_length=50)
    year = models.CharField(null=False, max_length=50)
    index = models.CharField(null=False, max_length=50)
    cultivationGoal = models.TextField(null=False)
    description = models.TextField(null=False)

class GraduateRequest(models.Model):
    facility = models.CharField(null=False, max_length=50)
    subject = models.CharField(null=False, max_length=50)
    year = models.CharField(null=False, max_length=50)
    requestIndex = models.CharField(null=False, max_length=50)
    graduateRequest = models.CharField(null=False, max_length=50)
    pointIndex = models.CharField(null=False, max_length=50)
    indexPoint = models.CharField(null=False, max_length=50)

class GoalAndRequest(models.Model):
    facility = models.CharField(null=False, max_length=50)
    subject = models.CharField(null=False, max_length=50)
    year = models.CharField(null=False, max_length=50)
    index = models.CharField(null=False, max_length=50)
    requestIndex = models.CharField(null=False, max_length=50)

class CourseInFosterPlan(models.Model):
    facility = models.CharField(null=False, max_length=50)
    subject = models.CharField(null=False, max_length=50)
    year = models.CharField(null=False, max_length=50)
    className = models.CharField(null=False, max_length=50)
    courseCategory = models.CharField(null=False, max_length=50)
    credits = models.CharField(null=False, max_length=50)
    hours = models.CharField(null=False, max_length=50)
    semester = models.CharField(null=False, max_length=50)
    isRequired = models.CharField(null=False, max_length=50)

class CourseWeight(models.Model):
    facility = models.CharField(null=False, max_length=50)
    subject = models.CharField(null=False, max_length=50)
    year = models.CharField(null=False, max_length=50)
    pointIndex = models.CharField(null=False, max_length=50)
    className = models.CharField(null=False, max_length=50)
    weight = models.CharField(null=False, max_length=50)

class ClassSupportRequest(models.Model):
    facility = models.CharField(null=False, max_length=50)
    subject = models.CharField(null=False, max_length=50)
    year = models.CharField(null=False, max_length=50)
    className = models.CharField(null=False, max_length=50)
    requestIndex = models.CharField(null=False, max_length=50)
    weight = models.CharField(null=False, max_length=50)

class ClassPlan(models.Model):
    className = models.CharField(null=False, max_length=50)
    userAccount = models.CharField(null=False, max_length=50)
    year = models.CharField(null=False, max_length=50)
    classInfo = models.TextField(null=True)

class ClassContent(models.Model):
    className = models.CharField(null=False, max_length=50)
    year = models.CharField(null=False, max_length=50)
    chapterIndex = models.CharField(null=False, max_length=50)
    chapter = models.CharField(null=False, max_length=50)
    keyPointIndex = models.CharField(null=False, max_length=50)
    keyPoint = models.CharField(null=False, max_length=50)

class ClassHours(models.Model):
    className = models.CharField(null=False, max_length=50)
    year = models.CharField(null=False, max_length=50)
    chapterIndex = models.CharField(null=False, max_length=50)
    theoryHours = models.CharField(null=False, max_length=50)
    practiceHours = models.CharField(null=False, max_length=50)
    selfLearningHours = models.CharField(null=False, max_length=50)
    description = models.TextField(null=False, max_length=50)

class ClassData(models.Model):
    className = models.CharField(null=False, max_length=50)
    year = models.CharField(null=False, max_length=50)
    homework = models.TextField(null=True)
    exam = models.TextField(null=True)
    experience = models.TextField(null=True)

class ClassDataRatio(models.Model):
    className = models.CharField(null=False, max_length=50)
    year = models.CharField(null=False, max_length=50)
    classTargetIndex = models.CharField(null=False, max_length=50)
    homeworkRatio = models.CharField(null=True, max_length=50)
    examRatio = models.CharField(null=True, max_length=50)
    experienceRatio = models.CharField(null=True, max_length=50)
    courseGoalAttainment = models.CharField(null=True, max_length=50)

class IndexPointContent(models.Model):
    className = models.CharField(null=False, max_length=50)
    year = models.CharField(null=False, max_length=50)
    pointIndex = models.CharField(null=False, max_length=50)
    classTarget = models.CharField(null=False, max_length=50)
    classTargetIndex = models.CharField(null=False, max_length=50)
    weight = models.CharField(null=False, max_length=50)

class IndexPointResult(models.Model):
    goal = models.CharField(null=True, max_length=50)
    pointIndex = models.CharField(null=False, max_length=50)
    className = models.CharField(null=False, max_length=50)
    year = models.CharField(null=False, max_length=50)
