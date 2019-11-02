from django.http import HttpResponse
from django.http import Http404
from polls.models import Question
from polls.models import Choice

from rest_framework import generics
from polls.serializers import ChoiceSerializer


def index(request):
    return HttpResponse("Hello, world. Views in polls")

def index_other(request):
    return HttpResponse("Hello, world. OTHER")

class ChoiceList(generics.ListCreateAPIView):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer


class ChoiceDetail(generics.RetrieveUpdateDestroyAPIView):
    
    serializer_class = ChoiceSerializer

    def get_object(self):
        obj = get_object_or_404(Choice, pk=self.kwargs.get('choice_id'))
        return obj
