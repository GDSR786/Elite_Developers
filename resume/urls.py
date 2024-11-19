from django.urls import path
from .views import *

urlpatterns = [
    path("", Homepage.as_view(), name="home"),
    path("about", About.as_view(), name="about"),
    path("contact", Contact.as_view(), name="contact"),
    path("subscribe", SubscribeView.as_view(), name="newsletter"),
    path("latest-articles", BlogsView.as_view(), name="blogs"),
    path("blog-details/<slug:url>", BlogDetailsView.as_view(), name="blog-details"),
]
