from django.conf.urls import url
from . import views

# here r'^$' matches a beginning (^) followed by an end ($),
# so only an empty string will match

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
]
