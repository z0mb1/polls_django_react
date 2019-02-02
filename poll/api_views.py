'''rest framework api view'''

from poll.serializers import PollSerializer, QuestionSerializer, ItemSerializer, VoteSerializer
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Poll, Item, Vote, Question


class PollListCreate(generics.ListCreateAPIView):
    queryset = Poll.objects.all()
    lookup_field = 'id'
    lookup_url_kwarg = 'poll_pk'
    serializer_class = PollSerializer

class PollDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Poll.objects.all()
    lookup_field = 'id'
    lookup_url_kwarg = 'poll_pk'
    serializer_class = PollSerializer
    
class QuestionList(generics.ListCreateAPIView):
    def get_queryset(self):
        queryset = Question.objects.filter(poll_id=self.kwargs["poll_pk"])
        return queryset
    lookup_field = 'id'
    lookup_url_kwarg = 'question_pk'
    serializer_class = QuestionSerializer

class QuestionDetail(generics.RetrieveUpdateDestroyAPIView):
    #queryset = Question.objects.all()
    def get_queryset(self):
        queryset = Question.objects.filter(poll_id=self.kwargs["poll_pk"])
        return queryset
    lookup_field = 'id'
    lookup_url_kwarg = 'question_pk'
    serializer_class = QuestionSerializer

class ItemList(generics.ListCreateAPIView):
    def get_queryset(self):
        queryset = Item.objects.filter(question_id=self.kwargs["question_pk"])
        return queryset
    lookup_field = 'id'
    lookup_url_kwarg = 'item_pk'
    serializer_class = ItemSerializer

class ItemDetail(generics.RetrieveUpdateDestroyAPIView):
    def get_queryset(self):
        queryset = Item.objects.filter(question_id=self.kwargs["question_pk"])
        return queryset
    lookup_field = 'id'
    lookup_url_kwarg = 'item_pk'
    serializer_class = ItemSerializer


class CreateVote(APIView):

    def post(self, request, poll_pk, question_pk, item_pk):
        user = request.data.get("user")
        ip=request.META['REMOTE_ADDR']
        data = {'question': question_pk, 'item': item_pk, 'ip': ip, 'user': user}
        serializer = VoteSerializer(data=data)
        if serializer.is_valid():
            vote = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
