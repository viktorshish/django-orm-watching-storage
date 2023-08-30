from django.shortcuts import render
from django.utils import timezone

from datacenter.models import get_duration, format_duration
from datacenter.models import Visit


def storage_information_view(request):
    remainder = Visit.objects.filter(leaved_at__isnull=True)

    for visit in remainder:
        non_closed_visits = [
            {
                'who_entered': visit.passcard.owner_name,
                'entered_at': timezone.localtime(visit.entered_at),
                'duration': format_duration(get_duration(visit))
            }
        ]

    context = {
        'non_closed_visits': non_closed_visits,  # не закрытые посещения
    }

    return render(request, 'storage_information.html', context)
