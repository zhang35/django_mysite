from django.contrib import admin

# Register your models here.
from .models import Question, Choice


class ChoiceInline(admin.TabularInline):
    model = Choice  # Choice objects are edited on the Question admin page
    extra = 3  # provide enough fields for 3 choices


class QuestionAdmin(admin.ModelAdmin):
    # fields = ['pub_date', 'question_text']
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']
    fieldsets = [
        ('Text', {'fields': ['question_text']}),
        ('Date information', {
            'fields': ['pub_date'],
            'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]


admin.site.register(Question, QuestionAdmin)

