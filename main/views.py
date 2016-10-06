from django.shortcuts import render
from django.views.generic import View, ListView, DetailView
from django.http import HttpResponse
from django.template import loader
from blog.models import Post
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect


from main.models import *

def index(request):
    prefaces_list = Preface.objects.all()
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    context = {'prefaces_list': prefaces_list, 'posts': posts}
    return render(request, 'index.html', context)

# class PrefaceMixin(object):
#     model = Preface
#
# class PrefaceList(PrefaceMixin, ListView):
#     template_name = 'main/sidebar.html'

class SkillMixin(object):
    model = Skill

class SkillList(SkillMixin, ListView):
    template_name = 'main/about.html'

class AboutMixin(object):
    model = About

class AboutList(AboutMixin, ListView):
    template_name = 'main/about.html'

class GoalMixin(object):
    model = Goal

class GoalList(GoalMixin, ListView):
    template_name = 'main/goals.html'

class BenefitMixin(object):
    model = Benefit

class BenefitList(BenefitMixin, ListView):
    template_name = 'main/benefits.html'

class FeeMixin(object):
    model = Fee

class FeeList(FeeMixin, ListView):
    template_name = 'main/fees.html'

class SkillMixin(object):
    model = Skill

class SkillList(SkillMixin, ListView):
    template_name = 'main/about.html'

class TestimonialMixin(object):
    model = Testimonial

class TestimonialList(TestimonialMixin, ListView):
    template_name = 'main/testimonials.html'

class TestimonialDetail(TestimonialMixin, DetailView):
    def get_context_data(self, **kwargs):
        context = super(TestimonialDetail, self).get_context_data(**kwargs)
        context['testimonials'] = Testimonial.objects.filter(testimonial=Testimonial)

        return context
