from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import ListView
from django.views.generic.edit import FormView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

from .models import Company, Job
from .forms import JobForm, CompanyForm 
from django.views.decorators.csrf import csrf_protect

# Create your views here.
def index(request):
	return render(request, 'app/index.html', {})

@csrf_protect
@login_required(login_url="index")
def all_jobs(request):
	jobs = Job.objects.all()
	return render(request, 'app/list_jobs.html', {'jobs': jobs, 'username': request.user.username})

class JobDeleteView(DeleteView):
	model = Job 
	success_url = reverse_lazy('all_jobs')

class CompanyListView(LoginRequiredMixin, ListView):
	login_url="index"
	model = Company
	context_object_name = 'companies'
	redirect_field_name = 'redirect_to'
	template_name = "app/list_company.html"

	def get_context_data(self, **kwargs):
		context = super(CompanyListView, self).get_context_data(**kwargs)
		context['username'] = self.request.user.username

		return context

class JobCreateView(LoginRequiredMixin, FormView):
	login_url="index"
	redirect_field_name = 'redirect_to'

	template_name = "app/create_form.html"
	form_class = JobForm
	success_url = "/jobs/all"

	def form_valid(self, form):
		form.save()
		return super(JobCreateView, self).form_valid(form)

	def get_context_data(self, **kwargs):
		context = super(JobCreateView, self).get_context_data(**kwargs)
		context['username'] = self.request.user.username

		return context

class CompanyCreateView(LoginRequiredMixin, FormView):
	login_url="index"
	redirect_field_name = 'redirect_to'

	template_name = "app/create_form.html"
	form_class = CompanyForm
	success_url = "/jobs/all"

	def form_valid(self, form):
		form.save()
		return super(CompanyCreateView, self).form_valid(form)

	def get_context_data(self, **kwargs):
		context = super(CompanyCreateView, self).get_context_data(**kwargs)
		context['username'] = self.request.user.username

		return context

def login_view(request):
	username = request.POST['username']
	password = request.POST['password']
	user = authenticate(username=username, password=password)
	if user is not None:
		if user.is_active:
			login(request, user)
			return redirect("all_jobs")
		else:
			return render(request, 'app/index.html', {'errors': "Usuário disabilitado."})
	else:
		return render(request, 'app/index.html', {'errors': "Usuário e senha não conferem."})

def logout_view(request):
	logout(request)
	return redirect("index")

class CompanyDelete(DeleteView):
	model = Company
	success_url = reverse_lazy('all_companies')