from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.utils.timezone import localtime

from .security_helper import get_duration, format_duration, is_suspicious


def passcard_info_view(request, passcode):
    passcard = get_object_or_404(Passcard, passcode = passcode)
    passcard_visits = Visit.objects.filter(passcard = passcard)
    this_passcard_visits = []

    for passcard_visit in passcard_visits:
        visit_duration = get_duration(passcard_visit)
        when_entered = localtime(passcard_visit.entered_at)
        is_strange = is_suspicious(visit_duration)
        visit_duration = format_duration(visit_duration)

        this_passcard_visits.append(
            {
                'entered_at': when_entered,
                'duration': visit_duration,
                'is_strange': is_strange
            },
        )
    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
