from django.shortcuts import render
from .models import dblearning, dbpred, chartColor



# moduł przesyłający dane do wyświetlenia tabel html z bazy danych

def index(request):
    all_dblearning = dblearning.objects.all()
    all_dbpred = dbpred.objects.all()
    return render(request, 'data/index.html', {'all_dblearning': all_dblearning,
                                               'all_dbpred': all_dbpred,
                                               })

# moduł kolorów nie działający

def chartColor(request):
    all_Color = chartColor.objects.all()

    return render(request, 'data/index.html', {'all_Color': all_Color,
                                                })

