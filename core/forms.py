from django import forms
from .models import Nurse, Contract, NurseShift, SPECIALIZATION_CHOICES, CONTRACT_CATEGORY_CHOICES

ZON_CHOICES = [
    (1, 'Zon 1'),
    (2, 'Zon 2'),
    (3, 'Zon 3'),
]

class CostCalculatorForm(forms.Form):
    specialization = forms.ChoiceField(choices=[('', 'Alla typer')] + SPECIALIZATION_CHOICES, label="Specialisering")
    zon = forms.ChoiceField(choices=ZON_CHOICES, label="Zon")
    nurse_wage = forms.FloatField(label="Timlön till sjuksköterskan (SEK/h)", min_value=0.0, required=True)

    regular_hours = forms.FloatField(label="Vanliga arbetade timmar", min_value=0.0, required=False, initial=0)

    evening_hours = forms.FloatField(label="Kväll (19-22)", min_value=0.0, required=False, initial=0)
    night_hours = forms.FloatField(label="Natt (22-06)", min_value=0.0, required=False, initial=0)
    weekend_evening_hours = forms.FloatField(label="Helg/kväll (19-22)", min_value=0.0, required=False, initial=0)
    weekend_day_hours = forms.FloatField(label="Helg/dag (06-19)", min_value=0.0, required=False, initial=0)
    weekend_night_hours = forms.FloatField(label="Helg/natt (22-06)", min_value=0.0, required=False, initial=0)
    storhelg_day_hours = forms.FloatField(label="Storhelg dag/kväll (07-22)", min_value=0.0, required=False, initial=0)
    storhelg_night_hours = forms.FloatField(label="Storhelg natt (22-07)", min_value=0.0, required=False, initial=0)

    jour_hours_weekend = forms.FloatField(label="Jour ej utfört (lör/sön/storhelg)", min_value=0.0, required=False, initial=0)
    beredskap_hours_weekend = forms.FloatField(label="Beredskap ej utfört (lör/sön/storhelg)", min_value=0.0, required=False, initial=0)
    jour_hours_weekday = forms.FloatField(label="Jour ej utfört (annan tid)", min_value=0.0, required=False, initial=0)
    beredskap_hours_weekday = forms.FloatField(label="Beredskap ej utfört (annan tid)", min_value=0.0, required=False, initial=0)
    jour_beredskap_aktiv_hours = forms.FloatField(label="Jour/beredskap aktiv tid (alla tider)", min_value=0.0, required=False, initial=0)

    sick_days_15_90 = forms.IntegerField(label="Sjukdagar (15-90)", min_value=0, required=False, initial=0)
    sick_days_15_45_if_under_year = forms.IntegerField(label="Sjukdagar (15-45, <1 års anst.)", min_value=0, required=False, initial=0)
    social_fee_percent = forms.FloatField(label="Sociala avgifter %", initial=31.42, required=True, help_text="Ex: 31.42")

class AdminSearchForm(forms.Form):
    specialization = forms.ChoiceField(choices=[('', 'Alla typer')] + SPECIALIZATION_CHOICES, required=False, label="Specialisering")
    city = forms.ChoiceField(required=False, label="Region")

    def __init__(self, *args, **kwargs):
        super(AdminSearchForm, self).__init__(*args, **kwargs)
        cities = Nurse.objects.values_list('city', flat=True).distinct().order_by('city')
        city_choices = [('', 'Alla regioner')] + [(c, c) for c in cities if c]
        self.fields['city'].choices = city_choices

class ContractForm(forms.ModelForm):
    class Meta:
        model = Contract
        fields = ['name', 'category', 'file']

class ContractFilterForm(forms.Form):
    category = forms.ChoiceField(choices=[('', 'Alla kategorier')] + CONTRACT_CATEGORY_CHOICES, required=False, label="Kategori")
    name = forms.CharField(label="Sök avtal", required=False)

class NurseShiftForm(forms.ModelForm):
    class Meta:
        model = NurseShift
        fields = ['nurse', 'start_time', 'end_time', 'region', 'hospital', 'department', 'responsible_name']
        widgets = {
            'start_time': forms.DateTimeInput(attrs={'type':'datetime-local'}),
            'end_time': forms.DateTimeInput(attrs={'type':'datetime-local'}),
        }
