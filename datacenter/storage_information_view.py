from django.shortcuts import render
from django.utils import timezone

from datacenter.models import get_duration, format_duration
from datacenter.models import Visit


def storage_information_view(request):
    visitors_remaining = Visit.objects.filter(leaved_at__isnull=True)
    non_closed_visits_serialized = []
    for visit in visitors_remaining:
        non_closed_visits_serialized.append({
            'who_entered': visit.passcard.owner_name,
            'entered_at': timezone.localtime(visit.entered_at),
            'duration': format_duration(get_duration(visit))
        })
    context = {'non_closed_visits': non_closed_visits_serialized}

    return render(request, 'storage_information.html', context)
