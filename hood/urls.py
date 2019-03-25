from django.conf.urls import url
from . import views
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from .forms import LoginForm

urlpatterns=[
    url(r'^$', views.home, name='home'),
    url(r'^hood/(\d+)',views.hood, name='hood'),
    url(r'^business/$',views.business,name='business'),
    url(r'^myprofile/$',views.own_profile,name='myprofile'),
    url(r'^new_business/$',views.new_business,name='new_business'),
    url(r'^posts/$',views.posts,name='posts'),
    url(r'^new_hood/$',views.new_hood,name='new_hood'),
    url(r'^search/$',views.search,name='search'),
    url(r'^new_posts/$',views.new_posts,name='new_posts'),
    url(r'login/', auth_views.LoginView.as_view(authentication_form=LoginForm), name='login'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'login'}, name='logout'),
    url(r'^edit/$', views.edit_profile, name='edit_profile'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)