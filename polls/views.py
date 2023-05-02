from django.shortcuts import render, redirect
from polls.forms import ScheduleForm
from polls.models import Schedule
from datetime import datetime


def index(request):
    if request.method == 'POST':
        schedule_form = ScheduleForm(request.POST)
        if schedule_form.is_valid():
            saving_obj = Schedule(**schedule_form.cleaned_data)
            saving_obj.save()
            return render(request, "register_schedule.html")
        else:
            context = {'schedule_form': schedule_form}
            return render(request, 'register_schedule.html', context)
    else:
        return render(request, 'register_schedule.html')

def check_schecule(date: str) -> dict:
    schecules = Schedule.objects.all()
    possible_schecule = schecules.filter(
            date__year=date.year,
            date__month=date.month,
            date__day=date.day)
    all_results = list()
    if len(possible_schecule) > 0:
        for schecule in possible_schecule:
            occurrence = {
                "description": schecule.description,
                "date": schecule.date,
            }
            all_results.append(occurrence)
        return {"all_results": all_results}
    return {"all_results": {}}


def home(request) -> render:
    date = request.GET.get("schedule")
    print(date)
    if date:
        final_date = datetime.strptime(date, '%Y-%m-%d').date()
    else: 
        final_date = datetime.now().date()
    schecules = check_schecule(final_date)
    schecules['date'] = final_date
    schecules['today'] = datetime.now().date()
    return render(request, "list_schedule.html", schecules)
