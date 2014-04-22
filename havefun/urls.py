from django.conf.urls import patterns,url

from havefun import views
urlpatterns=patterns('',
    url(r'^register/$',views.register,name="register"),
    url(r'^thanks/$',views.thanks,name="thanks"),
    url(r'^list/$',views.listRegister.as_view(),name="listRegister"),



    )