from rest_framework import serializers

from educationPlat.models import Users
from educationPlat.models import FosterPlan
from educationPlat.models import CultivationGoal
from educationPlat.models import GraduateRequest
from educationPlat.models import GoalAndRequest
from educationPlat.models import CourseInFosterPlan
from educationPlat.models import CourseWeight
from educationPlat.models import ClassSupportRequest
from educationPlat.models import ClassPlan
from educationPlat.models import ClassContent
from educationPlat.models import ClassHours
from educationPlat.models import ClassData
from educationPlat.models import ClassDataRatio
from educationPlat.models import IndexPointContent
from educationPlat.models import IndexPointResult



class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'

class FosterPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = FosterPlan
        fields = '__all__'

class CultivationGoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = CultivationGoal
        fields = '__all__'

class GraduateRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = GraduateRequest
        fields = '__all__'

class GoalAndRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoalAndRequest
        fields = '__all__'

class CourseInFosterPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseInFosterPlan
        fields = '__all__'

class CourseWeightSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseWeight
        fields = '__all__'

class ClassSupportRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassSupportRequest
        fields = '__all__'

class ClassPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassPlan
        fields = '__all__'

class ClassContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassContent
        fields = '__all__'

class ClassHoursSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassHours
        fields = '__all__'

class ClassDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassData
        fields = '__all__'

class ClassDataRatioSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassDataRatio
        fields = '__all__'

class IndexPointContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = IndexPointContent
        fields = '__all__'

class IndexPointResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = IndexPointResult
        fields = '__all__'
