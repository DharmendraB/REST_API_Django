from django.views.generic import TemplateView
from learn.models import Branch, Notice
from django.db.models import Q
from rest_framework import viewsets
from learn.myserializer import BranchSerializer, NoticeSerializer

# Create your views here.
class HomeView(TemplateView):
    template_name = "learn/home.html"
    
class AboutView(TemplateView):
    template_name = "learn/about.html"
class ContactView(TemplateView):
    template_name = "learn/contact.html"

class BranchViewSet(viewsets.ModelViewSet):
    queryset = Branch.objects.all().order_by("-id")
    serializer_class = BranchSerializer

class NoticeViewSet(viewsets.ModelViewSet):
    queryset = Notice.objects.all().order_by("-id")
    serializer_class = NoticeSerializer
    def get_queryset(self):
        search = self.request.GET.get('uq')
        if search == None:
            search =""
        return Notice.objects.filter(Q(subject__icontains = search) | Q(msg__icontains = search)).order_by("-id")




