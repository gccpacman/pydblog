from django.contrib import admin

from polls.models import Choice, Question


class QuestionAdmin(admin.ModelAdmin):
    fields = [
        'pub_date',
        'question_text',
    ]


admin.site.register(Choice)
admin.site.register(Question, QuestionAdmin)
