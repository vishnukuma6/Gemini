from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from stream.controller import streamcontroller
from user import views

urlpatterns = [
    path('video', streamcontroller.video_upload, name='video_upload'),
    url(r'^(?P<template_name>[\w-]+)/$', views.user_template , name='User_Template'),
]