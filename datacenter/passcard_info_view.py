import django
from django.shortcuts import get_object_or_404
from django.shortcuts import render

from datacenter.models import get_duration, format_duration, is_visit_long
from datacenter.models import Passcard
from datacenter.models import Visit


def passcard_info_view(request, passcode):
    access_card = get_object_or_404(Passcard, passcode=passcode)
    visits_passcard = Visit.objects.filter(passcard=access_card)

    this_passcard_visits = []
    for visit in visits_passcard:
        time_entry = django.utils.timezone.localtime(visit.entered_at)
        duration = get_duration(visit)
        formatted_duration = format_duration(duration)
        is_strange = is_visit_long(visit, minutes=60)
        passcard_visits = {
            'entered_at': time_entry,
            'duration': formatted_duration,
            'is_strange': is_strange
        }
        this_passcard_visits.append(passcard_visits)

    context = {
        'passcard': access_card,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
