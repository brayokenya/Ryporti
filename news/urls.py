from django.urls import include, re_path
from . import views

urlpatterns=[
    re_path('^$',views.welcome,name = 'welcome'),
    re_path('^today/$',views.news_of_day,name='newsToday'),
    re_path(r'^archives/(\d{4}-\d{2}-\d{2})/$',views.past_days_news,name = 'pastNews')
]