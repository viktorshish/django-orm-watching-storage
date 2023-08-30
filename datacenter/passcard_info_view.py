from django.shortcuts import get_object_or_404, render
from django.utils import timezone

from datacenter.models import get_duration, format_duration, is_visit_long
from datacenter.models import Passcard
from datacenter.models import Visit


def passcard_info_view(request, passcode):
    access_card = get_object_or_404(Passcard, passcode=passcode)
    visits_passcard = Visit.objects.filter(passcard=access_card)
    this_passcard_visits_serialized = []
    for visit in visits_passcard:
        this_passcard_visits_serialized.append({
                'entered_at': timezone.localtime(visit.entered_at),
                'duration': format_duration(get_duration(visit)),
                'is_strange': is_visit_long(visit, minutes=60)
            })
    context = {
        'passcard': access_card,
        'this_passcard_visits': this_passcard_visits_serialized
    }
    return render(request, 'passcard_info.html', context)
