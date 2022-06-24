from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions, status
from .models import (
    JobPostSkillSet,
    JobType,
    JobPost,
    Company
)
from django.db.models.query_utils import Q
from .serializers import JobPostSerializer
from django.shortcuts import get_object_or_404


class SkillView(APIView):

    permission_classes = [permissions.AllowAny]

    def get(self, request):
        skills = self.request.query_params.getlist('skills', '')
        print("skills = ", end=""), print(skills)

        return Response(status=status.HTTP_200_OK)


class JobView(APIView):

    def post(self, request):
        job_type = request.data.get("job_type", None)
        job_type_object = get_object_or_404(JobType, id=job_type)

        company_name = request.data.get("company_name", None)
        company_id = Company.objects.filter(company_name=company_name)
        if not company_id.exists():
            Company.objects.create(company_name=company_name)
            company_object = Company.objects.get(company_name = company_name)
            JobPost.objects.create(job_description=request.data['job_description'], salary=request.data['salary'], job_type=job_type_object, company=company_object)

            return Response(request.data, status=status.HTTP_200_OK)

        return Response({'message': '이미 등록된 회사입니다'}, status=status.HTTP_200_OK)

