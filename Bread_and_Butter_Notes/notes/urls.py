"""
    Bread and Butter Notes

    Notes app url configuration
"""

from django.conf.urls import url

from notes import views

urlpatterns = [
    url(r'^$', views.note_list, name='note_list'),
]
