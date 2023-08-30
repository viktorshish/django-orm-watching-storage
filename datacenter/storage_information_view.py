import django
from django.shortcuts import render

from datacenter.models import get_duration, format_duration
from datacenter.models import Visit


def storage_information_view(request):
    remainder = Visit.objects.filter(leaved_at__isnull=True)

    non_closed_visits = []
    for visitor in remainder:
        owner_name_entered = visitor.passcard.owner_name
        time_entry = django.utils.timezone.localtime(visitor.entered_at)
        duration = get_duration(visitor)
        formatted_duration = format_duration(duration)
        passcard_visitor = {
            'who_entered': owner_name_entered,
            'entered_at': time_entry,
            'duration': formatted_duration
        }
        non_closed_visits.append(passcard_visitor)

    context = {
        'non_closed_visits': non_closed_visits,  # не закрытые посещения
    }

    return render(request, 'storage_information.html', context)
