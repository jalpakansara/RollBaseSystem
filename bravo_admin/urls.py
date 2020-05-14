from django.urls import path
from django.conf.urls.static import static
from bravo_kids import settings
from bravo_kids.login import Login
from bravo_kids.home import Home
from bravo_kids.register import Register
from bravo_kids.logout import Logout



urlpatterns = [
    path('',Login),
    path('home',Home),
    path('user/add/',Register),
    path('logout/',Logout)

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
