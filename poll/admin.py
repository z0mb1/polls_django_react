from django.contrib import admin
from poll.models import *
from django.utils.translation import gettext as _


# опросы
class QuestionInline(admin.TabularInline):
    model = Question

class PollAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'owner', 'date', 'is_published', 'show_results')
    list_editable = ['description', 'is_published', 'show_results']
    inlines = [QuestionInline,]

admin.site.register(Poll, PollAdmin)

# вопросы
class QuestionItemInline(admin.TabularInline):
    model = Item
    extra = 0
    max_num = 15


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('title', 'poll')
    list_filter = ('poll',)
    inlines = [QuestionItemInline,]
    
admin.site.register(Question, QuestionAdmin)

# голоса
class VoteAdmin(admin.ModelAdmin):
    list_display = ('item', 'ip', 'user', 'datetime')
    list_filter = ('item', 'datetime')

admin.site.register(Vote, VoteAdmin)
