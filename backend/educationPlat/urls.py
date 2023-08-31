from django.urls import path, include
from rest_framework.routers import DefaultRouter

from educationPlat import views

router = DefaultRouter()
router.register('users', views.UsersViewSet)
router.register('fosterPlan', views.FosterPlanViewSet)
router.register('cultivationGoal', views.CultivationGoalViewSet)
router.register('graduateRequest', views.GraduateRequestViewSet)
router.register('goalAndRequest', views.GoalAndRequestViewSet)
router.register('courseInFosterPlan', views.CourseInFosterPlanViewSet)
router.register('courseWeight', views.CourseWeightViewSet)
router.register('classSupportRequest', views.ClassSupportRequestViewSet)
router.register('classPlan', views.ClassPlanViewSet)
router.register('classContent', views.ClassContentViewSet)
router.register('classHours', views.ClassHoursViewSet)
router.register('classData', views.ClassDataViewSet)
router.register('classDataRatio', views.ClassDataRatioViewSet)
router.register('indexPointContent', views.IndexPointContentViewSet)
router.register('indexPointResult', views.IndexPointResultViewSet)

urlpatterns = [
    path('', include(router.urls)),
]