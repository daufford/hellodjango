from django.contrib import admin

# Register your models here.
from .models import Choice, Question

class ChoiceInline(admin.TabularInline):
  model = Choice
  extra = 3

class QuestionAdmin(admin.ModelAdmin):
  #control edit form field sets
  fieldsets = [ ('Question details',{'fields':['question_text']}),
      ('Date information',{'fields':['pub_date'],'classes':['collapse']}) ]
  #enable inline editing of child choices
  inlines = [ChoiceInline]
  #control what columns are displayed / filterable in the list mode
  list_display = ('question_text','pub_date','was_published_recently')  #
  list_filter = ['pub_date']
  search_fields=['question_text']



admin.site.register(Question, QuestionAdmin)
#admin.site.register(Choice, ChoiceInline)
