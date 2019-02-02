from django.conf.urls import url
from django.urls import path, include

from poll import views
from poll import api_views


app_name = 'polls'
urlpatterns = [
    # для отдельного вопроса
    #url(r'^vote/single/(?P<question_pk>\d+)/$', views.vote, name='question_ajax_vote'),
    # для опроса
    url(r'^vote/(?P<poll_pk>\d+)/$', views.poll_vote, name='poll_ajax_vote'),
    url(r'^poll/(?P<poll_pk>\d+)/$', views.poll, name='poll'),
    url(r'^polls/$', views.PollsListView.as_view(), name='polls'),
    # результаты для отдельнго вопроса
    #url(r'^result/(?P<question_pk>\d+)/$', views.result, name='question_result'),
    # результаты для опроса
    url(r'^poll_result/(?P<poll_pk>\d+)/$', views.poll_result, name='poll_result'),
    # результаты для аякс запроса (без меню)
    url(r'^result/(?P<poll_pk>\d+)/$', views.poll_result, name='result'),
    url(r'^$', views.index, name='poll_index'),
    url(r'^clear_session/$', views.clear_session, name='clear_session'),
    
    #rest-framwork
    path('api/polls/', api_views.PollListCreate.as_view(), name="poll-list"),
    path('api/polls/<int:poll_pk>/', api_views.PollDetail.as_view(), name="poll-detail"),
    path("api/polls/<int:poll_pk>/questions/", api_views.QuestionList.as_view(), name="question-list"),
    path("api/polls/<int:poll_pk>/questions/<int:question_pk>/", api_views.QuestionDetail.as_view(), name="question-detail"),
    path("api/polls/<int:poll_pk>/questions/<int:question_pk>/items/", api_views.ItemList.as_view(), name="item-list"),
    path("api/polls/<int:poll_pk>/questions/<int:question_pk>/items/<int:item_pk>/", api_views.ItemDetail.as_view(), name="item-detail"),
    path("api/polls/<int:poll_pk>/questions/<int:question_pk>/items/<int:item_pk>/vote/", 
                        api_views.CreateVote.as_view(), name="create_vote"),
]


