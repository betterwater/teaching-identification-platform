from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Users
from .models import FosterPlan
from .models import CultivationGoal
from .models import GraduateRequest
from .models import GoalAndRequest
from .models import CourseInFosterPlan
from .models import CourseWeight
from .models import ClassSupportRequest
from .models import ClassPlan
from .models import ClassContent
from .models import ClassHours
from .models import ClassData
from .models import ClassDataRatio
from .models import IndexPointContent
from .models import IndexPointResult
from .serializers import UsersSerializer
from .serializers import FosterPlanSerializer
from .serializers import CultivationGoalSerializer
from .serializers import GraduateRequestSerializer
from .serializers import GoalAndRequestSerializer
from .serializers import CourseInFosterPlanSerializer
from .serializers import CourseWeightSerializer
from .serializers import ClassSupportRequestSerializer
from .serializers import ClassPlanSerializer
from .serializers import ClassContentSerializer
from .serializers import ClassHoursSerializer
from .serializers import ClassDataSerializer
from .serializers import ClassDataRatioSerializer
from .serializers import IndexPointContentSerializer
from .serializers import IndexPointResultSerializer

# Create your views here.

class UsersViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer

    @action(methods=['post'], detail=False)
    def login(self, request, pk=None):
        userAccount = request.data['userAccount']
        userPassword = request.data['userPassword']
        try:
            dbUserPassword = Users.objects.get(userAccount=userAccount).userPassword
        except:
            return Response({'code': 'false'})
        if (userPassword == dbUserPassword):
            data = {}
            user = Users.objects.get(userAccount=userAccount)
            data['code'] = 'true'
            data['userInfor'] = {'userName': user.userName, 'userAccount': user.userAccount, 'userPassword': user.userPassword}
            return Response(data)
        else:
            return Response({'code': 'false'})


class FosterPlanViewSet(viewsets.ModelViewSet):
    queryset = FosterPlan.objects.all()
    serializer_class = FosterPlanSerializer

    # 无 / facility、year、subject
    @action(methods=['post'], detail=False)
    def getAll(self, request, pk=None):
        if (not FosterPlan.objects.filter()):
            return Response({'code': 'false'})
        else:
            content = FosterPlan.objects.values('facility', 'subject', 'year').filter()
            data = {}
            data['code'] = 'true'
            data['content'] = content
            return Response(data)

    # facility、year、subject、briefInfo、subjectDescription、evaluationMechanism / 无
    @action(methods=['post'], detail=False)
    def uploadPlan(self, request, pk=None):
        facility = request.data['facility']
        subject = request.data['subject']
        year = request.data['year']
        briefInfo = request.data['briefInfo']
        subjectDescription = request.data['subjectDescription']
        evaluationMechanism = request.data['evaluationMechanism']

        if (facility == '' or subject == '' or year == '' or briefInfo == '' or subjectDescription == '' or evaluationMechanism == ''):
            return Response({'code': 'lack'})
        if (FosterPlan.objects.filter(facility=facility, subject=subject, year=year).first()):
            return Response({'code': 'exist'})
        else:
            FosterPlan.objects.create(facility=facility, subject=subject, year=year, briefInfo=briefInfo, subjectDescription=subjectDescription, evaluationMechanism=evaluationMechanism)
            return Response({'code': 'success'})

class CultivationGoalViewSet(viewsets.ModelViewSet):
    queryset = CultivationGoal.objects.all()
    serializer_class = CultivationGoalSerializer

    # facility、year、subject、index、cultivationGoal、description / 无
    @action(methods=['post'], detail=False)
    def uploadCG(self, request, pk=None):
        facility = request.data['facility']
        subject = request.data['subject']
        year = request.data['year']
        index = request.data['index']
        cultivationGoal = request.data['cultivationGoal']
        description = request.data['description']

        if (facility == '' or subject == '' or year == ''):
            return Response({'code': 'lack'})
        else:
            CultivationGoal.objects.create(facility=facility, subject=subject, year=year, index=index, cultivationGoal=cultivationGoal, description=description)
            return Response({'code': 'success'})

class GraduateRequestViewSet(viewsets.ModelViewSet):
    queryset = GraduateRequest.objects.all()
    serializer_class = GraduateRequestSerializer

    # facility、subject、year / requestIndex、graduateRequest、pointIndex、indexPoint
    @action(methods=['post'], detail=False)
    def getRequest(self, request, pk=None):
        facility = request.data['facility']
        subject = request.data['subject']
        year = request.data['year']
        if(not GraduateRequest.objects.filter(facility = facility, subject = subject, year = year)):
            return Response({'code': 'false'})
        else:
            content = GraduateRequest.objects.values('requestIndex', 'graduateRequest', 'pointIndex', 'indexPoint').filter(facility = facility, subject = subject, year = year)
            data = {}
            data['code'] = 'true'
            data['content'] = content
            return Response(data)

# facility、year、subject、requestIndex、graduateRequest、pointIndex、indexPoint / 无

    @action(methods=['post'], detail=False)
    def uploadRequest(self, request, pk=None):
        facility = request.data['facility']
        subject = request.data['subject']
        year = request.data['year']
        requestIndex = request.data['requestIndex']
        graduateRequest = request.data['graduateRequest']
        pointIndex = request.data['pointIndex']
        indexPoint = request.data['indexPoint']

        if (facility == '' or subject == '' or year == ''):
            return Response({'code': 'lack'})
        else:
            GraduateRequest.objects.create(facility=facility, subject=subject, year=year, requestIndex=requestIndex, graduateRequest=graduateRequest, pointIndex=pointIndex, indexPoint=indexPoint)
            return Response({'code': 'success'})

class GoalAndRequestViewSet(viewsets.ModelViewSet):
    queryset = GoalAndRequest.objects.all()
    serializer_class = GoalAndRequestSerializer

    # facility、year、subject、index、requestIndex / 无

    @action(methods=['post'], detail=False)
    def uploadGR(self, request, pk=None):
        facility = request.data['facility']
        subject = request.data['subject']
        year = request.data['year']
        index = request.data['index']
        requestIndex = request.data['requestIndex']

        if (facility == '' or subject == '' or year == ''):
            return Response({'code': 'lack'})
        else:
            GoalAndRequest.objects.create(facility=facility, subject=subject, year=year, index=index,
                                           requestIndex=requestIndex)
            return Response({'code': 'success'})

class CourseInFosterPlanViewSet(viewsets.ModelViewSet):
    queryset = CourseInFosterPlan.objects.all()
    serializer_class = CourseInFosterPlanSerializer

# facility、year、subject、className、courseCategory、credits、hours、semester、isRequired / 无

    @action(methods=['post'], detail=False)
    def uploadCIFP(self, request, pk=None):
        facility = request.data['facility']
        subject = request.data['subject']
        year = request.data['year']
        className = request.data['className']
        courseCategory = request.data['courseCategory']
        credits = request.data['credits']
        hours = request.data['hours']
        semester = request.data['semester']
        isRequired = request.data['isRequired']

        if (facility == '' or subject == '' or year == ''):
            return Response({'code': 'lack'})
        else:
            CourseInFosterPlan.objects.create(facility=facility, subject=subject, year=year, className=className,
                                          courseCategory=courseCategory, credits=credits, hours=hours, semester=semester, isRequired=isRequired)
            return Response({'code': 'success'})


# subject、className、year / courseCategory、credits、hours、semester、isRequired
    @action(methods=['post'], detail=False)
    def getCourse(self, request, pk=None):
        subject = request.data['subject']
        className = request.data['className']
        year = request.data['year']
        if (not CourseInFosterPlan.objects.filter(subject=subject, year=year, className=className)):
            return Response({'code': 'false'})
        else:
            content = CourseInFosterPlan.objects.values('courseCategory', 'credits', 'hours', 'semester', 'isRequired').filter(subject=subject, year=year, className=className)
            data = {}
            data['code'] = 'true'
            data['content'] = content
            return Response(data)

class CourseWeightViewSet(viewsets.ModelViewSet):
    queryset = CourseWeight.objects.all()
    serializer_class = CourseWeightSerializer

    # year、className / pointIndex、weight
    @action(methods=['post'], detail=False)
    def getWeight(self, request, pk=None):
        year = request.data['year']
        className = request.data['className']
        if (not CourseWeight.objects.filter(year=year, className=className)):
            return Response({'code': 'false'})
        else:
            content = CourseWeight.objects.values('pointIndex', 'weight').filter(className=className, year=year)
            data = {}
            data['code'] = 'true'
            data['content'] = content
            return Response(data)

# facility、subject、year / pointIndex、className、weight

    @action(methods=['post'], detail=False)
    def getPointW(self, request, pk=None):
        facility = request.data['facility']
        subject = request.data['subject']
        year = request.data['year']
        if (not CourseWeight.objects.filter(facility=facility, year=year, subject=subject)):
            return Response({'code': 'false'})
        else:
            content = CourseWeight.objects.values('pointIndex', 'className', 'weight').filter(facility=facility, year=year, subject=subject)
            data = {}
            data['code'] = 'true'
            data['content'] = content
            return Response(data)

# facility、year、subject、pointIndex、className、weight / 无

    @action(methods=['post'], detail=False)
    def uploadCW(self, request, pk=None):
        facility = request.data['facility']
        subject = request.data['subject']
        year = request.data['year']
        pointIndex = request.data['pointIndex']
        className = request.data['className']
        weight = request.data['weight']

        if (facility == '' or subject == '' or year == ''):
            return Response({'code': 'lack'})
        else:
            CourseWeight.objects.create(facility=facility, subject=subject, year=year, pointIndex=pointIndex,
                                              className=className, weight=weight)
            return Response({'code': 'success'})


class ClassSupportRequestViewSet(viewsets.ModelViewSet):
    queryset = ClassSupportRequest.objects.all()
    serializer_class = ClassSupportRequestSerializer

    # facility、year、subject、className、requestIndex、weight / 无

    @action(methods=['post'], detail=False)
    def uploadCSR(self, request, pk=None):
        facility = request.data['facility']
        subject = request.data['subject']
        year = request.data['year']
        className = request.data['className']
        requestIndex = request.data['requestIndex']
        weight = request.data['weight']

        if (facility == '' or subject == '' or year == ''):
            return Response({'code': 'lack'})
        else:
            ClassSupportRequest.objects.create(facility=facility, subject=subject, year=year, className=className,
                                        requestIndex=requestIndex, weight=weight)
            return Response({'code': 'success'})

class ClassPlanViewSet(viewsets.ModelViewSet):
    queryset = ClassPlan.objects.all()
    serializer_class = ClassPlanSerializer

    # 无 / className、year、userAccount | | userAccount / username
    @action(methods=['post'], detail=False)
    def getAllPlan(self, request, pk=None):
        if (not ClassPlan.objects.filter()):
            return Response({'code': 'false'})
        else:
            content = ClassPlan.objects.values('className', 'year', 'userAccount').filter()
            names = []
            for i in content:
                userName = Users.objects.get(userAccount=i['userAccount']).userName
                names.append(userName)
            data = {}
            data['userName'] = names
            data['code'] = 'true'
            data['content'] = content
            return Response(data)

    # userAccount / className、year
    @action(methods=['post'], detail=False)
    def getMine(self, request, pk=None):
        userAccount = request.data['userAccount']

        if (not ClassPlan.objects.filter(userAccount=userAccount)):
            return Response({'code': 'false'})
        else:
            content = ClassPlan.objects.values('className', 'year').filter(userAccount=userAccount)
            data = {}
            data['code'] = 'true'
            data['content'] = content
            return Response(data)


# userAccount、className、year 、classInfo/ 无
    @action(methods=['post'], detail=False)
    def uploadClass(self, request, pk=None):
        userAccount = request.data['userAccount']
        className = request.data['className']
        year = request.data['year']
        classInfo = request.data['classInfo']

        if (className == '' or year == ''):
            return Response({'code': 'lack'})
        else:
            ClassPlan.objects.create(userAccount=userAccount, className=className, year=year, classInfo=classInfo)
            return Response({'code': 'success'})

    # className、year / 无
    @action(methods=['post'], detail=False)
    def deleteCP(self, request, pk=None):
        className = request.data['className']
        year = request.data['year']

        if (className == '' or year == ''):
            return Response({'code': 'lack'})
        else:
            ClassPlan.objects.filter(className=className, year=year).delete()
            return Response({'code': 'success'})

class ClassContentViewSet(viewsets.ModelViewSet):
    queryset = ClassContent.objects.all()
    serializer_class = ClassContentSerializer

# className、year、chapterIndex、chapter、keyPointIndex、keyPoint / 无
    @action(methods=['post'], detail=False)
    def uploadCC(self, request, pk=None):
        className = request.data['className']
        year = request.data['year']
        chapterIndex = request.data['chapterIndex']
        chapter = request.data['chapter']
        keyPointIndex = request.data['keyPointIndex']
        keyPoint = request.data['keyPoint']

        if (className == '' or year == ''):
            return Response({'code': 'lack'})
        else:
            ClassContent.objects.create(className=className, year=year, chapterIndex=chapterIndex, chapter=chapter, keyPointIndex=keyPointIndex, keyPoint=keyPoint)
            return Response({'code': 'success'})

# className、year / 无
    @action(methods=['post'], detail=False)
    def deleteCContent(self, request, pk=None):
        className = request.data['className']
        year = request.data['year']

        if (className == '' or year == ''):
            return Response({'code': 'lack'})
        else:
            ClassContent.objects.filter(className=className, year=year).delete()
            return Response({'code': 'success'})

class ClassHoursViewSet(viewsets.ModelViewSet):
    queryset = ClassHours.objects.all()
    serializer_class = ClassHoursSerializer

    # className、year、chapterIndex、theoryHours、practiceHours、selfLearningHours、description / 无
    @action(methods=['post'], detail=False)
    def uploadCH(self, request, pk=None):
        className = request.data['className']
        year = request.data['year']
        chapterIndex = request.data['chapterIndex']
        theoryHours = request.data['theoryHours']
        practiceHours = request.data['practiceHours']
        selfLearningHours = request.data['selfLearningHours']
        description = request.data['description']

        if (className == '' or year == ''):
            return Response({'code': 'lack'})
        else:
            ClassHours.objects.create(className=className, year=year, chapterIndex=chapterIndex, theoryHours=theoryHours,
                                        practiceHours=practiceHours, selfLearningHours=selfLearningHours, description=description)
            return Response({'code': 'success'})

# className、year / 无
    @action(methods=['post'], detail=False)
    def deleteCH(self, request, pk=None):
        className = request.data['className']
        year = request.data['year']

        if (className == '' or year == ''):
            return Response({'code': 'lack'})
        else:
            ClassHours.objects.filter(className=className, year=year).delete()
            return Response({'code': 'success'})

class ClassDataViewSet(viewsets.ModelViewSet):
    queryset = ClassData.objects.all()
    serializer_class = ClassDataSerializer

    # className、year、data（homework、exp、exam） / 无
    @action(methods=['post'], detail=False)
    def uploadData(self, request, pk=None):
        className = request.data['className']
        year = request.data['year']
        homework = request.data['homework']
        exam = request.data['exam']
        experience = request.data['experience']
# //User.objects.filter(id=data['id']).update(email=data['email'], phone=data['phone'])
        if (ClassData.objects.filter(className=className, year=year).exists()):
            if (homework != ''):
                ClassData.objects.filter(className=className, year=year).update(homework=homework)
            if (exam != ''):
                ClassData.objects.filter(className=className, year=year).update(exam=exam,)
            if (experience != ''):
                ClassData.objects.filter(className=className, year=year).update(experience=experience)
            return Response({'code': 'success'})
        else:
            ClassData.objects.create(className=className, year=year, homework=homework, exam=exam, experience=experience)
            return Response({'code': 'success'})

# className、year / homework、exam、experience
    @action(methods=['post'], detail=False)
    def getData(self, request, pk=None):
        year = request.data['year']
        className = request.data['className']
        if (not ClassData.objects.filter(year=year, className=className)):
            return Response({'code': 'false'})
        else:
            content = ClassData.objects.values('homework', 'exam', 'experience').filter(year=year,className=className)
            data = {}
            data['code'] = 'true'
            data['content'] = content
            return Response(data)

# className、year / 无
    @action(methods=['post'], detail=False)
    def deleteCData(self, request, pk=None):
        className = request.data['className']
        year = request.data['year']

        if (className == '' or year == ''):
            return Response({'code': 'lack'})
        else:
            ClassData.objects.filter(className=className, year=year).delete()
            return Response({'code': 'success'})

class ClassDataRatioViewSet(viewsets.ModelViewSet):
    queryset = ClassDataRatio.objects.all()
    serializer_class = ClassDataRatioSerializer


# year、className / classTargetIndex、homeworkRatio、examRatio、experienceRatio、courseGoalAttainment
    @action(methods=['post'], detail=False)
    def getRatio(self, request, pk=None):
        year = request.data['year']
        className = request.data['className']
        if (not ClassDataRatio.objects.filter(year=year, className=className)):
            return Response({'code': 'false'})
        else:
            content = ClassDataRatio.objects.values('classTargetIndex', 'homeworkRatio', 'examRatio', 'experienceRatio', 'courseGoalAttainment').filter(year=year,
                                                                                                     className=className)
            data = {}
            data['code'] = 'true'
            data['content'] = content
            return Response(data)

    # className、year、classTargetIndex、homeworkRatio、examRatio、experienceRatio / 无
    @action(methods=['post'], detail=False)
    def uploadRatio(self, request, pk=None):
        className = request.data['className']
        year = request.data['year']
        classTargetIndex = request.data['classTargetIndex']
        homeworkRatio = request.data['homeworkRatio']
        examRatio = request.data['examRatio']
        experienceRatio = request.data['experienceRatio']

        if (className == '' or year == ''):
            return Response({'code': 'lack'})
        else:
            ClassDataRatio.objects.create(className=className, year=year, classTargetIndex=classTargetIndex, homeworkRatio=homeworkRatio, examRatio=examRatio, experienceRatio=experienceRatio)
            return Response({'code': 'success'})

# className、year / 无
    @action(methods=['post'], detail=False)
    def deleteCDR(self, request, pk=None):
        className = request.data['className']
        year = request.data['year']

        if (className == '' or year == ''):
            return Response({'code': 'lack'})
        else:
            ClassDataRatio.objects.filter(className=className, year=year).delete()
            return Response({'code': 'success'})

class IndexPointContentViewSet(viewsets.ModelViewSet):
    queryset = IndexPointContent.objects.all()
    serializer_class = IndexPointContentSerializer

    # year、className / pointIndex、classTargetIndex、classTarget、weight

    @action(methods=['post'], detail=False)
    def getTarget(self, request, pk=None):
        year = request.data['year']
        className = request.data['className']
        if (not IndexPointContent.objects.filter(year=year, className=className)):
            return Response({'code': 'false'})
        else:
            content = IndexPointContent.objects.values('pointIndex', 'classTargetIndex', 'classTarget', 'weight').filter(year=year, className=className)
            data = {}
            data['code'] = 'true'
            data['content'] = content
            return Response(data)

# className、year、classTargetIndex、classTarget、pointIndex、weight / 无
    @action(methods=['post'], detail=False)
    def uploadIPC(self, request, pk=None):
        className = request.data['className']
        year = request.data['year']
        classTargetIndex = request.data['classTargetIndex']
        classTarget = request.data['classTarget']
        pointIndex = request.data['pointIndex']
        weight = request.data['weight']

        if (className == '' or year == ''):
            return Response({'code': 'lack'})
        else:
            IndexPointContent.objects.create(className=className, year=year, classTargetIndex=classTargetIndex, classTarget=classTarget, pointIndex=pointIndex, weight=weight)
            return Response({'code': 'success'})

# className、year / 无
    @action(methods=['post'], detail=False)
    def deleteIPC(self, request, pk=None):
        className = request.data['className']
        year = request.data['year']

        if (className == '' or year == ''):
            return Response({'code': 'lack'})
        else:
            IndexPointContent.objects.filter(className=className, year=year).delete()
            return Response({'code': 'success'})

class IndexPointResultViewSet(viewsets.ModelViewSet):
    queryset = IndexPointResult.objects.all()
    serializer_class = IndexPointResultSerializer

    # year、className、pointIndex 、goal / 无
    @action(methods=['post'], detail=False)
    def uploadGoal(self, request, pk=None):
        year = request.data['year']
        className = request.data['className']
        pointIndex = request.data['pointIndex']
        goal = request.data['goal']

        if (className == '' or year == ''):
            return Response({'code': 'lack'})
        else:
            IndexPointResult.objects.create(className=className, year=year, pointIndex=pointIndex, goal=goal)
            return Response({'code': 'success'})

        # year、className、pointIndex / goal

    @action(methods=['post'], detail=False)
    def getPoint(self, request, pk=None):
        year = request.data['year']
        className = request.data['className']
        pointIndex = request.data['pointIndex']
        if (not IndexPointResult.objects.filter(year=year, className=className, pointIndex=pointIndex)):
            return Response({'code': 'false'})
        else:
            content = IndexPointResult.objects.values('goal').filter(year=year, className=className, pointIndex=pointIndex)
            data = {}
            data['code'] = 'true'
            data['content'] = content
            return Response(data)

# className、year / 无
    @action(methods=['post'], detail=False)
    def deleteIPR(self, request, pk=None):
        className = request.data['className']
        year = request.data['year']

        if (className == '' or year == ''):
            return Response({'code': 'lack'})
        else:
            IndexPointResult.objects.filter(className=className, year=year).delete()
            return Response({'code': 'success'})