from django.contrib import admin

from polls.models import Choice, Question


# class QuestionAdmin(admin.ModelAdmin):
#     fields = [
#         'pub_date',
#         'question_text',
#     ]

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]


admin.site.register(Choice)
admin.site.register(Question, QuestionAdmin)
