from django.db import models

class Stanowiska(models.Model):
    nazwa = models.CharField(max_length=255)
    opis = models.CharField(max_length=255)
    def __str__(self):
        return self.nazwa


class Pracownicy(models.Model):
    imie = models.CharField(max_length=255)
    nazwisko = models.CharField(max_length=255)
    adres = models.CharField(max_length=255)
    miasto = models.CharField(max_length=255)
    czyRodo = models.PositiveIntegerField()
    czyBadania = models.PositiveIntegerField()
    dataUr = models.DateField()
    stanowiska_id = models.ForeignKey(Stanowiska, on_delete=models.CASCADE)
    def __str__(self):
        return self.imie + " " + self.nazwisko
