from django.urls import URLPattern, path
from django.urls import  include

from .import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns= [
    path('', views.loginadmin, name='loginadmin'),
    path('signinadmin', views.signinadmin, name='signinadmin'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('dash/', views.dash, name='dash'),
    path('platform1/', views.platform1, name='platform1'),
    path('addplatform/', views.addplatform, name='addplatform'),
    path('register', views.register,name='register'),
    path('cshow/', views.cshow, name='cshow'),
    path('edit/', views.edit, name='edit'),
    path('edit/<int:platformid>', views.edit, name='edit'),
    path('update/<int:platformid>', views.update, name='update'),
    path('delete/<int:platformid>', views.delete, name='delete'),
    path('cources/', views.cources, name='cources'),
    path('show/', views.show, name='show'),
    path('cadd/', views.cadd, name='cadd'),
    path('register2', views.register2,name='register2'),
    path('tadd/', views.tadd, name='tadd'),
    path('editcource/<int:courceid>', views.editcource, name='editcource'),
    path('update2/<int:courceid>', views.update2, name='update2'),
    path('deletecource/<int:courceid>', views.deletecource, name='deletecource'),
    path('register3', views.register3,name='register3'),
    path('tshow', views.tshow, name='tshow'),
    path('delete1/<int:tutorialid>', views.delete1, name='delete1'),
    path('tedit/<int:tutorialid>', views.tedit, name='tedit'),
    path('update3/<int:tutorialid>', views.update3, name='update3'),
    path('qa/', views.qa, name='qa'),
    path('qashow/', views.qashow, name='qashow'),
    path('register4', views.register4,name='register4'),
    path('deleteq/<int:questionsid>', views.deleteq, name='deleteq'),
    path('logout/', views.logout, name='logout'),




    
    

    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)