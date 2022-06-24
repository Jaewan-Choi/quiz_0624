from rest_framework import serializers
from .models import JobPost as JobPostModel
from .models import Company as CompanyModel
from .models import JobPostSkillSet as JobPostSkillSetModel
from .models import SkillSet as SkillSetModel
from .models import CompanyBusinessArea


class CompanySerializer(serializers.ModelSerializer):
    
    business_area = serializers.SerializerMethodField()

    def get_business_area(self, obj):
        business_area = CompanyBusinessArea.objects.get(company_id=obj.id).business_area.area
        return business_area

    class Meta:
        model = CompanyModel
        fields = ["company_name", "business_area"]


class JobPostSerializer(serializers.ModelSerializer):

    company = CompanySerializer()
    job_type = serializers.SerializerMethodField()
    
    def get_job_type(self, obj):
        return obj.job_type.job_type

    class Meta:
        model = JobPostModel
        fields = ["company", "job_description", "salary", "job_type", "created_at"]


class SkillSetSerializer(serializers.ModelSerializer):

    class Meta:
        model = SkillSetModel
        fields = "__all__"


class JobPostSkillSetSerializer(serializers.ModelSerializer):

    skillset = serializers.SerializerMethodField()
    job_post = JobPostSerializer()

    def get_skillset(self, obj):
        return obj.skill_set.name

    class Meta:
        model = JobPostSkillSetModel
        fields = ["skillset", "job_post"]