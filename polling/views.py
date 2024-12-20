from django.shortcuts import render
from django.http import Http404
from polling.models import Poll
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from rest_framework.viewsets import ModelViewSet
from polling.serializers import PollSerializer


# html views
class PollListView(ListView):
    model = Poll
    template_name = "polling/list.html"


class PollDetailView(DetailView):
    model = Poll
    template_name = "polling/detail.html"

    def post(self, request, *args, **kwargs):
        poll = self.get_object()

        if request.POST.get("vote") == "Yes":
            poll.score += 1
        else:
            poll.score -= 1
        poll.save()

        return render(request, "polling/detail.html", {"object": poll})


# API views
class PollViewSet(ModelViewSet):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer
