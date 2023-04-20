from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.template import RequestContext
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin, messages
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.conf import settings
from django.template.loader import render_to_string
from django.core.mail import EmailMessage, send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.html import strip_tags
from admin_dashboard.forms import *


class AdminDashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'admin_dashboard/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


def admin_sign_in_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                try:
                    user = User.objects.get(email=username)
                except User.DoesNotExist:
                    user = None
            if not user:
                messages.error(request, 'Invalid Username or Email ')
            else:
                username = user.username
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    if user.is_active and user.is_superuser:
                        login(request, user)
                        messages.success(request, 'Welcome Back {}'.format(user.username))
                        if 'remember_login' not in request.POST:
                            request.session.set_expiry(0)
                            request.session.modified = True

                        nxt = request.GET.get("next", None)
                        if nxt:
                            return redirect(request.GET.get('next'))
                        return redirect(reverse('admin_dashboard'))
                    else:
                        messages.error(request, 'Account Does Not Have Permission for this Action')
                else:
                    messages.error(request, 'Invalid Credentials')
    else:
        form = LoginForm()
    context = {
        'form': form
    }
    return render(request, 'admin_dashboard/login.html', context)


def admin_sign_out_view(request):
    logout(request)
    return redirect(reverse('admin_login'))


class SiteInfoView(LoginRequiredMixin, TemplateView):
    template_name = 'admin_dashboard/site_info/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        site_info = SiteSetupModel.objects.first()
        if not site_info:
            form = SiteSetupForm()
            is_site_info = False
        else:
            form = SiteSetupForm(instance=site_info)
            is_site_info = True
        context['form'] = form
        context['is_site_info'] = is_site_info
        context['site_info'] = site_info
        return context


class SiteInfoCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = SiteSetupModel
    form_class = SiteSetupForm
    template_name = 'admin_dashboard/site_info/index.html'
    success_message = 'Site Info updated Successfully'

    def get_success_url(self):
        return reverse('site_info')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class SiteInfoUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = SiteSetupModel
    form_class = SiteSetupForm
    template_name = 'admin_dashboard/site_info/index.html'
    success_message = 'Site Info updated Successfully'

    def get_success_url(self):
        return reverse('site_info')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class GalleryCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = GalleryModel
    form_class = GalleryForm
    template_name = 'admin_dashboard/gallery/create.html'
    success_message = 'Image Uploaded Successfully'

    def get_success_url(self):
        return reverse('gallery_index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class GalleryListView(LoginRequiredMixin, ListView):
    model = GalleryModel
    fields = '__all__'
    template_name = 'admin_dashboard/gallery/index.html'
    context_object_name = "gallery_list"

    def get_queryset(self):
        return GalleryModel.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class GalleryDeleteView(LoginRequiredMixin, DeleteView):
    model = GalleryModel
    fields = '__all__'
    template_name = 'admin_dashboard/gallery/delete.html'
    context_object_name = "gallery"

    def get_success_url(self):
        return reverse('gallery_index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


def contact_us_mail(request):
    if request.method == 'POST':
        subject = request.POST.get('subject')
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        context = {
            'domain': get_current_site(request),
            'full_name': full_name,
            'email': email
        }
        mail_subject = subject
        from_email = settings.EMAIL_HOST_USER

        sent = send_mail(mail_subject, message, from_email, [from_email], fail_silently=True)
        if sent:
            return redirect('contact')

    return redirect('home')
