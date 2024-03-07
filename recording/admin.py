from django.contrib import admin
from recording.models import Recording


class RecordingAdmin(admin.ModelAdmin):
    readonly_fields = ['uuid']


admin.site.register(Recording, RecordingAdmin)