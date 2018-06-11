import datetime
from src.accounts.models import User
from src.events.models import Event

def get_teachers_photo(request):
    alluser = User.objects.all()
    teachers = []
    for u in alluser:
        if u.photo:
            teachers.append(u)
    return {'teachers_photo': teachers}

def get_first_events(request):
    now = datetime.date.today()
    events_now = Event.objects.filter(date_begin__lte=now).filter(date_end__gte=now) #проходят сейчас
    events_tomorrow = Event.objects.filter(date_begin__gt=now)[:3] #Ближайшее будущее
    return {'events_now': events_now, 'events_tomorrow': events_tomorrow}
