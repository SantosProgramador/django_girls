from django.conf.urls import include, url
from . import views
from django.views.generic import TemplateView

urlpatterns = [
	url(r'^$', views.post_list, name='post_list'),
	url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail),
	url(r'^post/new/$', views.post_new, name='post_new'),
	url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
	url(r'^post/(?P<pk>[0-9]+)/delete/$', views.post_delete, name='post_delete'),
	#url(r'^logout/$','django.contrib.auth.views.logout',{'next_page':'/'})
	url(r'^about/', TemplateView.as_view(template_name="about.html"),name='about'),
]