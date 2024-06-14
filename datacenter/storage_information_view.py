from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.utils.timezone import localtime

from .security_helper import get_duration, format_duration


def storage_information_view(request):
    non_leaved_visits = Visit.objects.filter(leaved_at = None)
    non_closed_visits = []
    for visit in non_leaved_visits:
        visit_duration = get_duration(visit)
        when_entered = localtime(visit.entered_at)
        visit_duration = format_duration(visit_duration)
        passcard_visit = visit.passcard

        non_closed_visits.append(
            {
                'who_entered': passcard_visit,
                'entered_at': when_entered,
                'duration': visit_duration,
            }
        )
    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
