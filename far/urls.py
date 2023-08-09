from django.urls import path
from .import views

urlpatterns = [
    path('',views.home,name='home'),
    # path('register',views.register,name='register'),
	# path('login',views.login,name='login'),
    # path('logout',views.logout,name='logout'),
    # path('name1',views.name1,name='name1'),
    # path('name2',views.name2,name='name2')
    path('org',views.org,name='org'),
    path('chem',views.chem,name='chem'),
    path('story',views.story,name='story'),
    path('about',views.about,name='about'),
    path('want',views.want,name='want'),
    path('find',views.find,name='find'),
    path('cont',views.cont,name='cont'),
    path('form1',views.form1,name='form1'),
    
]
