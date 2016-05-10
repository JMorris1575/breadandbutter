"""
    Bread and Butter Notes

    Notes app url configuration
"""

from django.conf.urls import url

from notes import views

urlpatterns = [
    url(r'^$', views.note_list, name='note_list'),
    url(r'^create/$', views.create_note, name='create_note'),
    url(r'^create/add/$', views.add_note, name='add_note'),
]
