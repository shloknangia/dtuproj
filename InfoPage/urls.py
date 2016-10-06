from django.conf.urls import url
from . import views

app_name = 'InfoPage'

urlpatterns = [
	#our basic url(main page)
	url(r'^$', views.index, name= 'index'),
	#urls of particular users
	url(r'^(?P<user_id>[0-9]+)/$', views.user_detail, name='user_detail'),
]