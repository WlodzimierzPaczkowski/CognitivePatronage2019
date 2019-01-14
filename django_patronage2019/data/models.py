from django.db import models
# Modele w których przechowywane są dane użyte przy ML (dblearing) i po ML (dbpred) oraz nie zaimplementowany model kolorów


class dblearning(models.Model):
    worked = models.FloatField(max_length=100)
    salary = models.FloatField(max_length=100)

    def __str__(self):
        return str(self.worked) + ', ' + str(self.salary)



class dbpred(models.Model):
    worked = models.FloatField(max_length=100)
    salary = models.FloatField(max_length=100)

    def __str__(self):
        return str(self.worked) + ', ' + str(self.salary)


class chartColor(models.Model):
    backgroundColor = models.CharField(max_length=40)
    borderColor = models.CharField(max_length=40)

    def __str__(self):
        return str(self.backgroundColor)

