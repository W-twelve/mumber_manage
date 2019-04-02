from django.conf.urls import url
from . import views

app_name = 'member'
urlpatterns=[
    url(r'^list/$', views.member_list, name='member_list'),
    url(r'^list/(?P<member_id>[0-9]*)/$',views.member_detail, name='member_detail'),
    url(r'^add/',views.member_add_xx, name='member_add'),
    url(r'^delet/(?P<member_id>[0-9]*)/$',views.member_delet, name='member_delet'),
    # url(r'^list/type/(?P<member_with_type_id>[0-9]*)/$',views.member_with_type,name='member_with_type'),
    #url(r'^date/(?P<year>[0-9]*)/(?P<month>[0-9]*)/(?P<day>[0-9]*)/$',views.blog_with_date,name='blog_with_date'),
]
