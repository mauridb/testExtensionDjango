# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Customer(models.Model):
    business_name = models.CharField(max_length=256, blank=False, null=False)
    email = models.EmailField()


class Network(models.Model):
    name = models.CharField(max_length=256, blank=False, null=False)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Network'
        verbose_name_plural = 'Network'


class Node(models.Model):
    name = models.CharField(blank=False, null=False, max_length=256)
    latitude = models.DecimalField(max_digits=10, decimal_places=8, blank=False, null=False)
    longitude = models.DecimalField(max_digits=10, decimal_places=8, blank=False, null=False)
    network = models.ForeignKey(Network, on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Node'
        verbose_name_plural = 'Nodes'

    def __unicode__(self):
        return self.name


class FileModel(models.Model):
    file = models.FileField(upload_to='spreadsheets')
