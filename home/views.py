from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView
from django.core.exceptions import PermissionDenied, ObjectDoesNotExist
from django.contrib.messages.views import SuccessMessageMixin, messages
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.template import RequestContext
from django.http import HttpResponse
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from admin_dashboard.models import *


class HomePageView(TemplateView):
    template_name = 'home/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['gallery_list'] = GalleryModel.objects.all()
        return context


class AboutPageView(TemplateView):
    template_name = 'home/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context


class ContactPageView(TemplateView):
    template_name = 'home/contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context


class ServicePageView(TemplateView):
    template_name = 'home/service.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context


class GalleryPageView(TemplateView):
    template_name = 'home/gallery.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['gallery_list'] = GalleryModel.objects.all()
        return context
