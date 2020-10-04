from django.urls import path,include
from . import views #this is to use view file(user front end design)
urlpatterns = [
    #path('admin/', admin.site.urls),
    path('',views.home,name='blog-home'), #start of run there #in this calling the function which is the file called view.py
    #path('about/',views.about,name='blog-home1'),
    #url(r'^search/$',search),
    path('index/',views.index,name='index'),

    path('search/',views.search,name='submit'),
    #path('search/',views.search,name='submit'),
    #path('search/frontpage2.html',views.apply,name='submit'),
    #path is to route the page of it.like when we click on the page saying which page to appear
    #path('back',views.back, name="back")
    path('about', views.about, name="about"),
    path('index/apply', views.search, name="apply"),


]
