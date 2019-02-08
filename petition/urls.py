from django.urls import path
from . import views

app_name='petition'
urlpatterns = [    
    path('', views.index, name='index'),
    path('petitions/<int:petition_id>', views.view_petition, name='view_petition'),
    path('about', views.about, name='about'),
    path('petitions/create', views.create_petition, name='create_petition'),
    path('login', views.login, name='login'),
    path('tags/<slug:tag_label>', views.view_tag, name='view_tag'),
]

# Use static() to add url mapping to serve static files during development (only)
# from django.conf import settings
# from django.conf.urls.static import static


# urlpatterns+= static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)