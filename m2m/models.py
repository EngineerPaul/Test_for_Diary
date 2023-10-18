from django.db import models


class Record(models.Model):  # Course - python
    title = models.CharField(max_length=20)


class People(models.Model):  # Student - tom, sam
    record = models.ManyToManyField(
        Record, through='PeopleRecordsLink', related_name='people')
    name = models.CharField(max_length=20)


# что. если добавить related_name в каждый ключ
# можно ли тогда будет сделать запрос всех записей для одного пользователя за 1 запрос
class PeopleRecordsLink(models.Model):
    people = models.ForeignKey(People, on_delete=models.CASCADE)
    record = models.ForeignKey(Record, on_delete=models.CASCADE)
    color = models.CharField(max_length=15)
    assessment = models.IntegerField()
