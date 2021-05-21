from django.shortcuts import render
from django.http import HttpResponseNotFound, HttpResponseRedirect, Http404
from django.urls import reverse
from django.template.loader import render_to_string

monthly_challenges = {
    'january': 'Eat no meat for the entire month!',
    'february': 'Walk for at least 20 minutes every day!',
    'march': 'Learn Django for at least 20 minutes every day!',
    'april': 'Eat no meat for the entire month!',
    'may': 'Learn Django for at least 20 minutes every day!',
    'june': 'Walk for at least 20 minutes every day!',
    'july': 'Eat no meat for the entire month!',
    'august': 'Walk for at least 20 minutes every day!',
    'september': 'Learn Django for at least 20 minutes every day!',
    'october': 'Eat no meat for the entire month!',
    'november': 'Learn Django for at least 20 minutes every day!',
    # 'december': 'Walk for at least 20 minutes every day!',
    'december': None,
}

def index(request):
  months = list(monthly_challenges.keys())
  return render(request, 'challenges/index.html', {
    'months': months
  })

def monthly_challenge_by_number(request, month):
  months = list(monthly_challenges.keys())
  if month > len(months):
    return HttpResponseNotFound('Invalid Month')
  redirect_month = months[month - 1]
  redirect_path = reverse('month-challenge', args=[redirect_month])
  return HttpResponseRedirect(redirect_path)

def monthly_challenge(request, month):
  try:
    challenge_text = monthly_challenges[month]
    return render(request, 'challenges/challenge.html', {
      'challenge': challenge_text,
      'month': month
    })
  except:
    raise Http404()
