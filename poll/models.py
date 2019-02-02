import datetime
from django.db import models
from django.conf import settings
from django.db.models.manager import Manager
from django.contrib.auth.models import User


try:
    from django.contrib.auth import get_user_model
except ImportError:
    from django.contrib.auth.models import User
else:
    User = settings.AUTH_USER_MODEL


class PublishedManager(Manager):
    def get_query_set(self):
        return super(PublishedManager, self).get_query_set().filter(is_published=True)


class Poll(models.Model):
    def get_sentinel_user():
        return get_user_model().objects.get_or_create(username='deleted')[0]
    
    title = models.CharField(max_length=250, verbose_name=('poll'))
    description = models.CharField(max_length=250, verbose_name=('description'), blank=True, null=True, default='')
    date = models.DateField(verbose_name=('date'), default=datetime.date.today)
    is_published = models.BooleanField(default=True, verbose_name=('is published'))
    # флаг для отображения результатов (если False, то результат записывается в базу и не отображается)
    show_results = models.BooleanField(default=True, verbose_name=('show results'))
    owner = models.ForeignKey(User, on_delete=models.SET(get_sentinel_user),)

    objects = models.Manager()
    published = PublishedManager()

    class Meta:
        ordering = ['-date']
        verbose_name = ('poll')
        verbose_name_plural = ('polls')

    def __str__(self):
        return self.title

class Question(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, verbose_name=('poll'), related_name='questions')
    title = models.CharField(max_length=250, verbose_name=('question'))

    objects = models.Manager()

    class Meta:
        verbose_name = ('question')
        verbose_name_plural = ('questions')

    def __str__(self):
        return self.title

    def get_vote_count(self):
        return Vote.objects.filter(question=self).count()
    vote_count = property(fget=get_vote_count)
    
    '''написать функцию по типу get_vote_count которая будет фильтровать голоса по параметрам респондента'''

    def get_cookie_name(self):
        return 'question_%s' % self.pk


class Item(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name=('question'), related_name='items')
    value = models.CharField(max_length=250, verbose_name=('value'))
    pos = models.SmallIntegerField(default='0', verbose_name=('position'))

    class Meta:
        verbose_name = ('answer')
        verbose_name_plural = ('answers')
        ordering = ['pos']

    def __str__(self):
        return u'%s' % (self.value,)

    def get_vote_count(self):
        return Vote.objects.filter(item=self).count()
    vote_count = property(fget=get_vote_count)
    
    
class Vote(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name=('question'))
    item = models.ForeignKey(Item, on_delete=models.CASCADE, verbose_name=('voted item'))
    ip = models.GenericIPAddressField(verbose_name=('user\'s IP'))
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True,
                             verbose_name=('user'))
    datetime = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = ('vote')
        verbose_name_plural = ('votes')

    def __str__(self):
        if isinstance(User, str):
            UserModel = get_user_model()
        else:
            UserModel = User

        if isinstance(self.user, UserModel):
            username_field = getattr(User, 'USERNAME_FIELD', 'username')
            return getattr(User, username_field, '')
        return self.ip
        

