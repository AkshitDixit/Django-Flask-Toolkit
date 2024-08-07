from django.shortcuts import render
from django.http import HttpResponse

def main(response):
    return HttpResponse("response 1")

def mainApp(response):
    return HttpResponse("main app")