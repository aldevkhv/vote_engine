from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views
from mezzanine.pages import views as pages_view

urlpatterns = [
    # url(r'^$', pages_view.page, {'slug': 'competition'}, name='home'),

    url('^$', views.competition_list, name='competitions'),
    url('^competition/(?P<competition_id>[0-9]+)$', views.about_competition, name='about_competition'),
    url('^competition_add/$', views.competition_add, name='competition_add'),
    url('^competition_edit/$', views.competition_edit, name='competition_edit'),
    url('^competition_delete/(?P<competition_id>[0-9]+)$', views.competition_delete, name='competition_delete'),


    url('^participate/$', views.participates_in_competition, name='participates_in_competition'),
    url('^participate_manage/$', views.participate_manage, name='participate_manage'),
    url('^participate/(?P<participate_id>[0-9]+)$', views.about_participate, name='about_participate'),
    url('^participate_add/$', views.participate_add, name='participate_add'),
    url('^participate_edit/$', views.participate_edit, name='participate_edit'),
    url('^participate_delete/(?P<participate_id>[0-9]+)$', views.participate_delete, name='participate_delete'),

    url('^vote/(\d{1,9})$', views.vote, name='vote'),

    url(r'^change_password/$', views.change_password, name='change_password'),
    url(r'^register/', views.register, name='register'),
]
