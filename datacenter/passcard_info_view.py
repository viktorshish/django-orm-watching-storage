import django
from django.shortcuts import get_object_or_404
from django.shortcuts import render

from datacenter.models import get_duration, format_duration, is_visit_long
from datacenter.models import Passcard
from datacenter.models import Visit


def passcard_info_view(request, passcode):
    passcard = get_object_or_404(Passcard, passcode=passcode)
    visits = Visit.objects.filter(passcard=passcard)
    this_passcard_visits = []
    for visit in visits:
        entered = django.utils.timezone.localtime(visit.entered_at)
        time_left_inside = get_duration(visit)
        duration = format_duration(time_left_inside)
        is_strange = is_visit_long(visit, minutes=60)
        passcard_visits = {
            'entered_at': entered,
            'duration': duration,
            'is_strange': is_strange
        }
        this_passcard_visits.append(passcard_visits)
        
    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
