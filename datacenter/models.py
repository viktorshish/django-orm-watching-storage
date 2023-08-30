import django
from django.db import models


SECONDS_IN_HOUR = 3600
SECONDS_IN_MINUTE = 60


class Passcard(models.Model):
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    passcode = models.CharField(max_length=200, unique=True)
    owner_name = models.CharField(max_length=255)

    def __str__(self):
        if self.is_active:
            return self.owner_name
        return f'{self.owner_name} (inactive)'


class Visit(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    passcard = models.ForeignKey(Passcard, on_delete=models.CASCADE)
    entered_at = models.DateTimeField()
    leaved_at = models.DateTimeField(null=True)

    def __str__(self):
        return '{user} entered at {entered} {leaved}'.format(
            user=self.passcard.owner_name,
            entered=self.entered_at,
            leaved=(
                f'leaved at {self.leaved_at}'
                if self.leaved_at else 'not leaved'
            )
        )


def get_duration(visit):
    if not visit.leaved_at:
        now_time = django.utils.timezone.localtime()
        entered_time = django.utils.timezone.localtime(visit.entered_at)
        delta_time = now_time - entered_time
    else:
        entered_time = django.utils.timezone.localtime(visit.entered_at)
        leaved_time = django.utils.timezone.localtime(visit.leaved_at)
        delta_time = leaved_time - entered_time

    duration = delta_time.total_seconds()

    return duration


def format_duration(duration):
    hours = int(duration // SECONDS_IN_HOUR)
    minutes = int((duration % SECONDS_IN_HOUR) // SECONDS_IN_MINUTE)
    formatted_duration = f'{hours}ч {minutes}мин'

    return formatted_duration


def is_visit_long(visit, minutes=60):
    delta_seconds = get_duration(visit)
    delta_minutes = int(delta_seconds // SECONDS_IN_MINUTE)

    return delta_minutes > minutes
