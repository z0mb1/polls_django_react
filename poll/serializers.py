from rest_framework import serializers
from poll.models import Poll, Question, Item, Vote
from rest_framework.reverse import reverse


class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = '__all__'


class ItemSerializer(serializers.ModelSerializer):
    votes = VoteSerializer(many=True, required=False)

    class Meta:
        model = Item
        fields = '__all__'


class QuestionSerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True, read_only=True, required=False)
    class Meta:
        model = Question
        fields = '__all__'

class QuestionHyperlink(serializers.HyperlinkedRelatedField):
    # We define these as class attributes, so we don't need to pass them as arguments.
    view_name = 'question-detail'
    queryset = Question.objects.all()

    def get_url(self, obj, view_name, request, format):
        url_kwargs = {
            'poll_pk': obj.poll.pk,
            'question_pk': obj.pk
        }
        return reverse(view_name, kwargs=url_kwargs, request=request, format=format)

    def get_object(self, view_name, view_args, view_kwargs):
        lookup_kwargs = {
           'poll__pk': view_kwargs['poll_pk'],
           'pk': view_kwargs['question_pk']
        }
        return self.get_queryset().get(**lookup_kwargs)
        

class PollSerializer(serializers.ModelSerializer):
    #questions = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    #questions = QuestionSerializer(many=True, read_only=True, required=False)
    questions = QuestionHyperlink(
        many=True,
        read_only=False,
        view_name='polls:question-detail',
        lookup_field='id',
        lookup_url_kwarg='question_pk',
    )
    url = serializers.HyperlinkedIdentityField(
        read_only=True,
        view_name='polls:poll-detail',
        lookup_field='id',
        lookup_url_kwarg='poll_pk',
    )
    
    class Meta:
        model = Poll
        #fields = '__all__'
        fields = ('url', 'id', 'title', 'description', 'date', 'owner', 'questions')
        

