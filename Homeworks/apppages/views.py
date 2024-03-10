from django.http import HttpResponseBadRequest
from django.shortcuts import render
import os

def index(request):
    return render(request, 'home.html')

points=[
    {'id': 1, 'name': 'Inomjon Qurbonov', 'bir': {2, 4, 1}, 'ikki': {5, 10, 5}, 'uch': {5, 5}, 'jami': 37},
    {'id': 2, 'name': 'Muhammadyusuf Abduvaliyev', 'bir': {3, 5, 2}, 'ikki': {4, 10, 4}, 'uch': {5, 3}, 'jami': 36},
    {'id': 3, 'name': 'Shoxruhbek Turdaliyev', 'bir': {3, 0, 2}, 'ikki': {3, 10, 3}, 'uch': {5, 3}, 'jami': 29},
    {'id': 4, 'name': 'Zafarbek Olimboyev', 'bir': {3, 5, 2}, 'ikki': {5, 10, 4}, 'uch': {5, 5}, ' jami': 39},
    {'id': 5, 'name': 'Samariddin Baxtiyorov', 'bir': {2, 5, 1}, 'ikki': {4, 10, 5}, 'uch': {5, 5}, 'jami': 37},
    {'id': 6, 'name': 'Ozodbek Axrorov', 'bir': {3, 5, 2}, 'ikki': {5, 10, 5}, 'uch': {5, 5}, 'jami': 40},
    {'id': 7, 'name': 'Javohir Otaboyev', 'bir': {0, 5, 0}, 'ikki': {5, 10, 5}, 'uch': {5, 5}, 'jami': 35},
    {'id': 8, 'name': 'Mubina Nusratullayeva', 'bir': {3, 5, 2}, 'ikki': {1, 10, 2}, 'uch': {4, 4}, 'jami': 31},
    {'id': 9, 'name': 'Sunnatillo Sharipov', 'bir': {3, 5, 2}, 'ikki': {5, 10, 5}, 'uch': {5, 5}, 'jami': 40},
    {'id': 10, 'name': 'Ruslan Mamatanov', 'bir': {2, 5, 2}, 'ikki': {5, 10, 5}, 'uch': {3, 3}, 'jami': 35},
    {'id': 11, 'name': "Firdavs Jo'rayev", 'bir': {2, 5, 2}, 'ikki': {2, 10, 2}, 'uch': {4, 3}, 'jami': 30},
    {'id': 12, 'name': "Javlonbek Jo'rayev", 'bir': {3, 5, 2}, 'ikki': {1, 10, 2}, 'uch': {4, 4}, 'jami': 31},
    {'id': 13, 'name': 'Naziraxon Qodirova', 'bir': {3, 5, 2}, 'ikki': {1, 10, 2}, 'uch': {4, 4}, 'jami': 31},
    {'id': 14, 'name': 'Arabboy Yunusov', 'bir': {2, 5, 1}, 'ikki': {5, 10, 5}, 'uch': {5, 3}, 'jami': 36},
    {'id': 15, 'name': 'Fazilatxon Axmedova', 'bir': {2, 5, 1}, 'ikki': {5, 10, 5}, 'uch': {5, 3}, 'jami': 36},
]

def themes(request):
    lessons_file_path = os.path.join(os.path.dirname(__file__), 'lessons.txt')
    with open(lessons_file_path, 'r') as file:
        lessons = file.read().splitlines()
    return render(request, 'themes.html',context={'lessons': lessons})

def pupils(request):
    return render(request, 'pupils.html', context={'pupils':points})

def homework(request):
    homeworks_file_path = os.path.join(os.path.dirname(__file__), 'homeworks.txt')
    with open(homeworks_file_path,'r') as file:
        homeworks = file.read().splitlines()
    return render(request, 'homework.html', context={'homeworks': homeworks})

def point_for_month(request,pk):
    if pk > 15 or pk < 1:
        return HttpResponseBadRequest('Point must be between 1 and 15')
    return render(request,'point.html',{'points':points[pk-1]})
