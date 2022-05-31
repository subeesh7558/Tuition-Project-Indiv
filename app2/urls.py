from django.urls import URLPattern, path
from .import views



urlpatterns= [
    path('loginuser/', views.loginuser, name='loginuser'),
    path('signin/', views.signinuser, name='signinuser'),
    path('signup2/', views.signup2, name='signup2'),
    path('login2/', views.login2, name='login2'),
    path('firstpage/', views.firstpage, name='firstpage'),
    path('secondpage/', views.secondpage, name='secondpage'),
    # path('tutorialpage/', views.tutorialpage, name='tutorialpage'),
    path('certi/', views.certi, name='certi'),
    path('pro/', views.pro, name='pro'),
    path('tutorialselection/<int:tutorialid>',views.tutorialselection, name='tutorialselection'),
    path('tutorialpage/',views.tutorialpage, name='tutorialpage'),
    
   

    
    

    
]