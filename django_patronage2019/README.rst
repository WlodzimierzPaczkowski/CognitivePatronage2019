======================================================================================================
Django framework implementation for visualisation of simple machine learning dataset nad prediction
======================================================================================================
Following repository show implementation of django framework for Intive Patronage 2019 program second stage recruitment at Machine Learning & Big Data department.

Overall
========
According to guidelines this website have 2 views, main/home page and data page, each with link to each other.
Data for both html table and javascript charts are taken from db.sqlite3, based on django models function, imported from csvlearning.csv and csvpred.csv file with following code in manage.py shell of django project.::

    ```
    import csv

    from dashboard.models import dblearning
    with open('csvlearning.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            p = dblearning(worked=row['worked'], salary=row['salary'])
            p.save()
    ```

for learning dataset ::

    ```
    import csv
    
    from dashboard.models import dbpred
    with open('csvpred.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            p = dbpred(worked=row['worked'], salary=row['salary'])
            p.save()
    ```

for predicted dataset

Dataset are taken from machine learning linear regression algorithm for predicted value nad from stage one Patronage 2019 recruitment for learning value.

Models
=======
models possess two ``FloatField``, worked years and salary, they are rendered to 'data/index.html' and used in ``{% for data in all_dblearning/all_dbpred %}{{ data.floatField }},{% endfor %}`` loop to iterate through dataset.
In code there is also unimplemented color database for charts.

HTML tables
===========
tabel are simple HTML tables with both datasets iterated through, <table><tr><th> type, with absolute positon

Charts
======
charts are made with chart.js in javascript, two horizontal bar chart made to look like histogram, and two pie chart, data form them are from same source and same way of implemantation as HTML table.
Colors for pie chart are hard coded, however pie chart for learning dataest are only one color to reduce code line, soultion planed for this was iterable color model dataset, unfortunately it is not implemented.

CSS
====
few thing implemented from Bootstrap, buttons, homepage element

Author
======
Włodzimierz Paczkowski
https://github.com/WlodzimierzPaczkowski
