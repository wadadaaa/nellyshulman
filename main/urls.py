from django.conf.urls import include, url
from .views import *
from . import views

urlpatterns = [
    url(r'^about/$',
                   AboutList.as_view(), name='about'),
    url(r'^goals/$',
                   GoalList.as_view(), name='goal'),
    url(r'^benefits/$',
                   BenefitList.as_view(), name='benefit'),
    url(r'^fees/$',
                   FeeList.as_view(), name='fee'),
    url(r'^testimonial/$',
                   TestimonialList.as_view(), name='testimonial'),
    url(r'^testimonial/detail/(?P<slug>[-_\w]+)/$',
                   TestimonialDetail.as_view(), name='testimonial_detail'),
    url(r'^contact/$',
                   views.contact, name='contact'),
]
