from django.db import models

SPECIALIZATION_CHOICES = [
    ('VANLIG', 'Allmänsjuksköterska (Vanlig)'),
    ('ANESTESI', 'Anestesisjuksköterska'),
    ('BARN', 'Barnsjuksköterska'),
    ('BARNMORSKA', 'Barnmorska'),
    ('DISTRIKT', 'Distriktssköterska'),
    ('INTENSIV', 'Intensivvårdssjuksköterska'),
    ('OPERATION', 'Operationssjuksköterska'),
    ('PSYKIATRI', 'Psykiatrisjuksköterska'),
    ('ONKOLOGI', 'Onkologisjuksköterska'),
    ('GERIATRIK', 'Geriatriksjuksköterska'),
    ('RÖNTGEN', 'Röntgensjuksköterska'),
    ('MOTTAGNING', 'Mottagningssjuksköterska'),
    ('SKOL', 'Skolsköterska'),
    ('INFEKTION', 'Infektionssjuksköterska'),
]

CONTRACT_CATEGORY_CHOICES = [
    ('BESTÄLLARE', 'Avtal med beställare'),
    ('SAMARBETE', 'Avtal med Samarbetspartners'),
    ('KONSULTBOLAG', 'Avtal med konsulter (egna bolag)'),
    ('ANSTÄLLNING', 'Anställningsavtal'),
    ('TJÄNSTER', 'Avtal för tjänster'),
    ('MALLAR', 'Avtalsmallar'),
]

class Nurse(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(unique=True)
    city = models.CharField(max_length=100)
    specialization = models.CharField(max_length=50, choices=SPECIALIZATION_CHOICES, blank=True, null=True)
    cv_file = models.FileField(upload_to='cvs/', blank=True, null=True)
    license_file = models.FileField(upload_to='licenses/', blank=True, null=True)
    accepted_gdpr = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class NurseShift(models.Model):
    nurse = models.ForeignKey(Nurse, on_delete=models.CASCADE, related_name='shifts')
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    region = models.CharField(max_length=100, blank=True, null=True)
    hospital = models.CharField(max_length=100, blank=True, null=True)
    department = models.CharField(max_length=100, blank=True, null=True)
    responsible_name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.nurse.name} {self.start_time.strftime('%Y-%m-%d %H:%M')} - {self.end_time.strftime('%H:%M')}"

class Contract(models.Model):
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=50, choices=CONTRACT_CATEGORY_CHOICES)
    file = models.FileField(upload_to='contracts/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
