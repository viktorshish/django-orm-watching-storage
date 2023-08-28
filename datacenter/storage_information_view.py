from datacenter.models import Passcard
from datacenter.models import Visit
from datacenter.models import get_duration, format_duration
from django.shortcuts import render
import django


def storage_information_view(request):
    # Программируем здесь
    non_closed_visits = []
    left_inside = Visit.objects.filter(leaved_at__isnull=True)
    for visitor in left_inside:
        owner_name_entered = visitor.passcard.owner_name
        enteret_time = django.utils.timezone.localtime(visitor.entered_at)
        time_left_inside = get_duration(enteret_time)
        duration = format_duration(time_left_inside)
        passcard_visitor = {
            'who_entered': owner_name_entered,
            'entered_at': enteret_time,
            'duration': duration
        }
        non_closed_visits.append(passcard_visitor)
   
    context = {
        'non_closed_visits': non_closed_visits,  # не закрытые посещения
    }
    
    return render(request, 'storage_information.html', context)
