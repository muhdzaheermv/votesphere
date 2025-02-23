from django.contrib import admin
from .models import Candidate, Vote,ElectionOfficer

admin.site.register(ElectionOfficer)
admin.site.register(Candidate)
admin.site.register(Vote)
