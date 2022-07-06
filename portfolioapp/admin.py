from django.contrib import admin
from .models.personal_information import personal
from .models.skills import skills
from .models.education import education
from .models.projects import projects
# Register your models here.
admin.site.register(personal)
admin.site.register(skills)
admin.site.register(education)
admin.site.register(projects)
