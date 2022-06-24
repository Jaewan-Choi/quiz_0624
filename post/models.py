from django.db import models


class SkillSet(models.Model):
    name = models.CharField(max_length=128)
    job_posts = models.ManyToManyField('JobPost', through='JobPostSkillSet')

    class Meta:
        db_table = 'skill_sets'

    def __str__(self):
        return f"[기술] {self.name}"


class JobPostSkillSet(models.Model):
    skill_set = models.ForeignKey('SkillSet', on_delete=models.SET_NULL, null=True)
    job_post = models.ForeignKey('JobPost', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.skill_set} / {self.job_post}"


class JobType(models.Model):
    job_type = models.CharField(max_length=128)

    class Meta:
        db_table = 'job_types'

    def __str__(self):
        return f"[타입] {self.job_type}"


class JobPost(models.Model):
    job_type = models.ForeignKey(JobType, on_delete=models.SET_NULL, null=True)
    company = models.ForeignKey('Company', on_delete=models.SET_NULL, null=True)
    job_description = models.TextField()
    salary = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'job_posts'

    def __str__(self):
        return f"[공고] {self.company.company_name}"


class Company(models.Model):
    company_name = models.CharField(max_length=128)
    business_area = models.ManyToManyField('BusinessArea', through='CompanyBusinessArea')

    class Meta:
        db_table = 'companies'

    def __str__(self):
        return f"[회사] {self.company_name}"


class CompanyBusinessArea(models.Model):
    company = models.ForeignKey('Company', on_delete=models.SET_NULL, null=True)
    business_area = models.ForeignKey('BusinessArea', on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = 'company_business_areas'

    def __str__(self):
        return f"{self.company} / {self.business_area}"


class BusinessArea(models.Model):
    area = models.CharField(max_length=128)

    class Meta:
        db_table = 'business_areas'

    def __str__(self):
        return f"[분야] {self.area}"