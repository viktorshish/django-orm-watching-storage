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
    now_time = django.utils.timezone.localtime()
    enteret_time = django.utils.timezone.localtime(visit)
    delta_time = now_time - enteret_time
    delta_seconds = delta_time.total_seconds()
    
    return delta_seconds


def format_duration(duration):
    hours = int(duration // 3600)
    minutes = int((duration % 3600) // 60)
    being_in = f'{hours}ч {minutes}мин'
    
    return being_in


def is_visit_long(visit, minutes=60):
    long_visits = []
    
    for visiting in visit:
        enter = django.utils.timezone.localtime(visiting.entered_at)
       
        if not visiting.leaved_at:
            now_time = django.utils.timezone.localtime()
            delta_time = now_time - enter
        else:
            leaved_time = django.utils.timezone.localtime(visiting.leaved_at)
            delta_time = leaved_time - enter    
        delta_seconds = delta_time.total_seconds()
        delta_minutes = int(delta_seconds // 60)
        
        if delta_minutes > minutes:
            long_visits.append(visiting)
            
            return True
        return False
