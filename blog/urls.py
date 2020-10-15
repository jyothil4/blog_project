from django.conf.urls import url
from blog import views

urlpatterns = [
    url(r'^$',views.PostListView.as_view(),name='post_list'),
    url(r'^about/$',views.AboutView.as_view(),name='about'),
    url(r'^post/(?P<pk>\d+)/$',views.PostDetailView.as_view(),name='post_detail'),
    url(r'^post/create/$',views.CreatePostView.as_view(),name='post_create'),
    url(r'^post/(?P<pk>\d+)/update/$',views.PostUpdateView.as_view(),name='post_update'),
    url(r'^post/(?P<pk>\d+)/delete/$',views.PostDeleteView.as_view(),name='post_delete'),
    url(r'^draft/$',views.DraftListView.as_view(),name='post_draft'),
    url(r'^post/(?P<pk>\d+)/publish/$',views.post_publish,name='post_publish'),
    url(r'^post/(?P<pk>\d+)/comment/$',views.comment_to_post,name='comment_to_post'),
]
