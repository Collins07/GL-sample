# data_visualization_app/models.py

from django.db import models

class EnvironmentalData(models.Model):
    date = models.DateField(auto_now=True)
    industry_category = models.CharField(max_length=50, choices=[('Transport', 'Transport'), ('Banking', 'Banking'), ('Agriculture', 'Agriculture')])
    total_vehicles = models.PositiveIntegerField()
    fossil_fuel_cars = models.PositiveIntegerField()
    electric_vehicles = models.PositiveIntegerField()
    source_of_energy_1 = models.CharField(max_length=50, choices=[('Hydro', 'Hydro'), ('Solar', 'Solar')])
    energy_consumption_1 = models.FloatField()
    source_of_energy_2 = models.CharField(max_length=50, choices=[('Hydro', 'Hydro'), ('Solar', 'Solar')])
    energy_consumption_2 = models.FloatField()

class SocialData(models.Model):
    total_employees = models.PositiveIntegerField()
    female_employees = models.PositiveIntegerField()
    male_employees = models.PositiveIntegerField()
    employees_with_disabilities = models.PositiveIntegerField()
    employees_age_20_30 = models.PositiveIntegerField()
    employees_age_31_40 = models.PositiveIntegerField()
    employees_age_41_50 = models.PositiveIntegerField()
    employees_age_51_60 = models.PositiveIntegerField()
    employees_age_61_plus = models.PositiveIntegerField()
