from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name="index"),
	url(r'^register/$', views.UserFormView.as_view(), name="register"),
	url(r'^login/$', views.login_view, name="login"),
	url(r'^logout/$', views.logout_view, name="logout"),
	url(r'^all$', views.all_jobs, name="all_jobs"),
	url(r'^create$', views.JobCreateView.as_view(), name='create_job'),
	url(r'^(?P<pk>\d+)/delete$', views.JobDeleteView.as_view(), name="delete_job"),
	url(r'^(?P<pk>\d+)/edit$', views.JobUpdateView.as_view(), name="edit_job"),
	url(r'^company/create$', views.CompanyCreateView.as_view(), name='create_company'),
	url(r'^company/$', views.CompanyListView.as_view(), name="all_companies"),
	url(r'^company/(?P<pk>\d+)/delete$', views.CompanyDelete.as_view(), name="delete_company"),
	url(r'^company/(?P<pk>\d+)/edit$', views.CompanyUpdateView.as_view(), name="edit_company"),
]