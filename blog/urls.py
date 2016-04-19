from django.conf.urls import include, url
from . import views
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required

urlpatterns = [
	url(r'^$', views.PostList.as_view(template_name="post_list.html"), name='post_list'),
	url(r'^post/(?P<pk>[0-9]+)/$', views.PostDetail.as_view(), name='post_detail'),
	url(r'^post/new/$', login_required(views.PostCreate.as_view(),login_url='login'),name='post_new'),
	url(r'^post/(?P<pk>[0-9]+)/edit/$', views.EditPost.as_view(), name='post_edit'),
	url(r'^post/(?P<pk>[0-9]+)/delete/$', views.PostDelete.as_view(), name='post_delete'),
	#url(r'^logout/$','django.contrib.auth.views.logout',{'next_page':'/'})
	url(r'^about/', TemplateView.as_view(template_name="about.html"),name='about'),
	url(r'^comment/(?P<pk>[0-9]+)/like/$',views.comment_like, name='comment_like'),
	url(r'^comment/(?P<pk>[0-9]+)/dislike/$',views.comment_dislike, name='comment_dislike')
]