from django.conf.urls import url
import views

urlpatterns = [
    url(r'^(?P<id>[0-9]+)', views.details),
    url(r'^all$' , views.showAllQuestions),
]
