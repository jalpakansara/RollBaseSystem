from django.urls import path
from bravo_kids.login import Login
from django.conf.urls.static import static
from bravo_kids import settings
from bravo_kids.home import Home
from .tutorial import Tutorial_add


urlpatterns = [
    path('',Login),
    path('home/',Home),
    path('tutorial/add/',Tutorial_add),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
