from django.shortcuts import render, redirect
from .models import Hrac

def vypis_hracu(request):
    if request.method == 'POST':
        jmeno = request.POST.get('jmeno')
        klub = request.POST.get('klub')
        goly = request.POST.get('goly')

        if jmeno and goly:
            Hrac.objects.create(jmeno=jmeno, klub=klub, goly=int(goly))
            
        
        return redirect('vypis_hracu')

    hraci = Hrac.objects.all().order_by('-goly')
    return render(request, 'stats/vypis.html', {'hraci': hraci})