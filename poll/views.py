from django.shortcuts import render
from .forms import AnonUserParamsForm
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.list import ListView
from django.template import RequestContext
from django.shortcuts import redirect

#from .utils import set_cookie
from .models import Poll, Item, Vote, Question
from users.models import Profile

def poll_vote(request, poll_pk):
    
    if request.is_ajax():
        try:
            poll = Poll.objects.get(pk=poll_pk)
        except:
            return HttpResponse('Wrong parameters', status=400)
        
        # возможно стоит убрать проверку, надо проверить функциональность
        answers = request.GET.items()
        if not answers:
            return HttpResponse('Wrong parameters', status=400)

        if request.user.is_authenticated:
            user = request.user
            profile = Profile.objects.get(user=user.pk)
            profile.finished_polls.add(poll)
        else:
            user = None
            finished_polls = request.session['anon_user_data'].get('finished_polls', [])
            finished_polls.append(poll_pk)
            request.session['anon_user_data']['finished_polls'] = list(set(finished_polls))
            request.session.modified = True
            #print(request.session['anon_user_data']['finished_polls'] )
            
        for q, i in list(request.GET.items()):
            try:
                question = Question.objects.get(pk=int(q))
                item = Item.objects.get(pk=int(i))
            except:
                return HttpResponse('Wrong parameters', status=400)
            
            
            Vote.objects.create(
                question=question,
                item=item,
                ip=request.META['REMOTE_ADDR'],
                user=user,
            )
            #print('vote object created')


        response = HttpResponse(status=200)
        #set_cookie(response, poll.get_cookie_name(), poll_pk)

        return response
    return HttpResponse(status=400)

def clear_session(request):
    if request.session.get('anon_user_data'):
        del request.session['anon_user_data']
    return redirect('polls:polls')

def poll(request, poll_pk):
    try:
        poll = Poll.objects.get(pk=poll_pk)
    except Poll.DoesNotExists:
        return HttpResponse('Wrong parameters', status=400)
    # все вопросы из выбранного опроса
    questions = Question.objects.filter(poll=poll)
    # к каждому вопросу добавляется список вариантов ответов
    for q in questions:
        q.items_set = q.items.all()

    return render(request, "poll/poll.html", {
        'poll': poll,
        'questions': questions,
    })


class PollsListView(ListView):
    template_name = 'poll/polls.html'
    queryset = Poll.objects.order_by('-date')
    paginate_by = 6
    context_object_name = 'polls'
    
    '''
    def get_context_data(self, **kwargs):
        context = super(PollsListView, self).get_context_data(**kwargs)
        questions = Question.objects.all()
        context['questions'] = questions
        return context'''

   
def poll_result(request, poll_pk):
    try:
        poll = Poll.objects.get(pk=poll_pk)
        # все вопросы из выбранного опроса
        questions = Question.objects.filter(poll=poll)
        # к каждому вопросу добавляется список вариантов ответов
        for q in questions:
            q.items_set = q.items.all()
    except Poll.DoesNotExists:
        return HttpResponse('Wrong parameters', status=400)
    if request.is_ajax():
        return render(request, "poll/result.html", {
            'questions': questions,})
    else:
        return render(request, "poll/poll_result.html", {
            'questions': questions,})
  
    
def index(request):
    return render(request, "poll/index.html")

def user_data_input(request):  
    GENDER = {
       '1': "man",
       '2': "woman", 
    }
    AGE = {
       '1': "<18",
       '2': "18-25", 
       '3': "25-35", 
       '4': "35-50", 
       '5': ">50", 
    }
    
    if request.method == 'POST':
        form = AnonUserParamsForm(request.POST)
        #Если форма заполнена корректно, сохраняем все введённые пользователем значения
        if form.is_valid():
            request.session['anon_user_data']['age'] = AGE[form.cleaned_data['age']]
            request.session['anon_user_data']['sex'] = GENDER[form.cleaned_data['sex']]
            request.session.modified = True
            return HttpResponseRedirect('/index/')
    else:
        form = AnonUserParamsForm()
    context = {'form': form}
    return render(request, "poll/user_data_input.html", context)
    




