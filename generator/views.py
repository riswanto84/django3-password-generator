from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from pyproc import Lpse
import json
import random

def home(request):
    return render(request, 'generator/home.html')

def about(request):
    return render(request, 'generator/about.html')

def password(request):

    charaters = list('abcdefghijklmnopqrstupwxyz')

    if request.GET.get('uppercase'):
        charaters.extend(list('ABCDEFGHIJKLMNOPQRSTUPWXYZ'))
    if request.GET.get('special'):
        charaters.extend(list('!@#$%^&*()'))
    if request.GET.get('numbers'):
        charaters.extend(list('0123456789'))

    length = int(request.GET.get('lenght', 12))
    thepassword = ''
    for x in range(length):
        thepassword += random.choice(charaters)

    return render(request, 'generator/password.html', {'password':thepassword})

def lpse(request):
    lpse = Lpse('http://lpse.kemenkeu.go.id')
    detil = lpse.detil_paket_tender(id_paket='32016011')
    detil.get_all_detil()
    datapemenang = detil.get_pemenang()
    datapeserta = detil.get_peserta()
    dataevaluasi = detil.get_hasil_evaluasi()
    return render(request, 'generator/datapemenanglpse.html', {'datapemenang' : datapemenang, 'datapeserta' : datapeserta, 'dataevaluasi' : dataevaluasi})
    
    
    #return HttpResponse(datapemenang)
    #return JsonResponse({'dataevaluasi' : dataevaluasi})
