from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    people=[
        {'name':'abjeet','age':45},
        {'name':'abhi','age':5},
        {'name':'abhishek','age':55},
        {'name':'acashek','age':35},
    ]
    for member in people:
        print(member)
    return render(request, "home/index.html",context={'people':people})
def success_page(request):
    return render(request,"temp/hi.html")
def menu(request):
    return render(request,"temp/menu.html")
def about(request):
    return render(request,"home/about.html")
def charts(request):
    return render(request,"temp/charts.html")
