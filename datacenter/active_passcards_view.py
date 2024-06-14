from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.utils.timezone import localtime
from datetime import datetime, timezone

def active_passcards_view(request):
    active_passcards = Passcard.objects.filter(is_active=True)
    context = {
        'active_passcards': active_passcards,
    }
    return render(request, 'active_passcards.html', context)


if __name__ == '__main__':
    passcards = Passcard.objects.all()
    active_passcards = Passcard.objects.filter(is_active=True)

