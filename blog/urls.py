from django.urls import path, re_path
from .views import AboutView, PostListView, PostCreateView, PostUpdateView, PostDeleteView, DraftListView
from .views import add_comment_to_post, comment_approve, comment_remove, post_publish

urlpatterns = [
    re_path(r'^$', PostListView.as_view(), name = 'post_list'),
    re_path(r'^about/$', AboutView.as_view(), name = 'about'),
    re_path(r'^post/(?P<pk>\d+)$', PostListView.as_view(), name = 'post_detail'),
    re_path(r'^post/new/$', PostCreateView.as_view(), name = 'post_new'),
    re_path(r'^post/(?P<pk>\d+)/edit/$', PostUpdateView.as_view(), name = 'post_edit'),
    re_path(r'^post/(?P<pk>\d+)/remove/$', PostDeleteView.as_view(), name='post_remove'),
    re_path(r'^drafts/$', DraftListView.as_view(), name='post_draft_list'),
    re_path(r'^post/(?P<pk>\d+)/comment/$', add_comment_to_post, name = 'add_comment_to_post'),
    re_path(r'^comment/(?P<pk>\d+)/approve/$', comment_approve, name='comment_approve'),
    re_path(r'^comment/(?P<pk>\d+)/remove/$', comment_remove, name='comment_remove'),
    re_path(r'^post/(?P<pk>\d+)/publish/$', post_publish, name = 'post_publish'),

]