from datacenter.models import Passcard
from datacenter.models import Visit
from django.utils.timezone import localtime
from datetime import datetime, timezone, timedelta


def format_duration(sec):
    sec_value = sec % (24 * 3600)
    hour_value = sec_value // 3600
    sec_value %= 3600
    min = sec_value // 60
    sec_value %= 60
    time = f"{hour_value}:{min}:{sec_value}"
    return time


def get_duration(visit):
    when_entered = localtime(visit.entered_at)
    now = datetime.now(timezone.utc)
    if visit.leaved_at:
        duration_miliseconds = (now - when_entered).total_seconds()
    else:
        duration_miliseconds = (when_entered - now).total_seconds()
    duration_seconds = int(duration_miliseconds // 1000)
    return duration_seconds

def is_suspicious(duration_seconds, minutes = 60):
    limit_seconds = minutes * 60
    return duration_seconds > limit_seconds