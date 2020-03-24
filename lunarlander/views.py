from django.shortcuts import render
from lunarlander.models import Score
from django.http import HttpResponse
# Create your views here.

def home(request):
    data = {
        "scores": Score.objects.order_by('-score','-date').all()
    }
    return render(request, 'lunarlander/lunarlander.html', data)

def highScores(request):
    if request.method == 'POST' and request.POST:
        try:
            submittedScore = int(request.POST.get('score', '0'))
            newScore = Score(score=submittedScore)
            newScore.save()
            data = {
                "scores": Score.objects.order_by('-score','-date').all()
            }
            return render(request, 'lunarlander/highScoreList.html', data)
        except:
            return HttpResponse('Error loading high scores.', status=400)