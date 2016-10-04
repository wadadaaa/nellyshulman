from django.conf.urls import include, url
from .views import *

urlpatterns = [
    url(r'^about/$',
                   AboutList.as_view(), name='about'),
    url(r'^goals/$',
                   GoalList.as_view(), name='goal'),
    url(r'^benefits/$',
                   BenefitList.as_view(), name='benefit'),
   url(r'^fees/$',
                  FeeList.as_view(), name='fee'),                   
]
