from django.contrib import admin

from .models import Question, Choice

# class ChoiceInline(admin.StackedInline):    #takes a lot of space in the admin UI, that's why switch to TabularInline
class ChoiceInline(admin.TabularInline):    
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ('Date Information', {"fields": ["pub_date"]}),
    ]
    inlines = [ChoiceInline]
    list_display = ["question_text", "pub_date", "was_published_recently"]  # In the list of ques it will show tabular view having columns mention here
    list_filter = ["pub_date"]  #Add filter option in admin page
    search_fields = ["question_text"]
    # fields = ["pub_date", "question_text"]    #can change the order of the column in db



# version1 without ModelAdmin
#admin.site.register(Question)

#Version2 with ModelAdmin
admin.site.register(Question, QuestionAdmin)

# admin.site.register(Choice)