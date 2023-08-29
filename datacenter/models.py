from django.db import models
import django


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
        enteret_time = django.utils.timezone.localtime(visit.entered_at)
        delta_time = now_time - enteret_time
    else:
        enteret_time = django.utils.timezone.localtime(visit.entered_at)
        leaved_time = django.utils.timezone.localtime(visit.leaved_at) 
        delta_time = leaved_time - enteret_time
    delta_seconds = delta_time.total_seconds()
    
    return delta_seconds


def format_duration(duration):
    hours = int(duration // 3600)
    minutes = int((duration % 3600) // 60)
    being_in = f'{hours}ч {minutes}мин'
    
    return being_in


def is_visit_long(visit, minutes=60):    
    delta_seconds = get_duration(visit)
    delta_minutes = int(delta_seconds // 60)
        
    if delta_minutes > minutes:            
        return True
    return False
