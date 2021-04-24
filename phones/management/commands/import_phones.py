import csv

from django.core.management.base import BaseCommand
from phones.models import Phone, Apple, Samsung, Xiaomi
from datetime import date
from django.utils.text import slugify
from phones import data


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        for el in data.items():
            phone = Phone.objects.create(
                name=el[1]['phone']['name'],
                price=el[1]['phone']['price'],
                OS_version=el[1]['phone']['OS_version'],
                RAM=el[1]['phone']['RAM'],
                internal_memory_capacity=el[1]['phone']['internal_memory_capacity'],
                ppi=el[1]['phone']['ppi'],
                processor=el[1]['phone']['processor'],
                image_size=el[1]['phone']['image_size'],
                number_cameras=el[1]['phone']['number_cameras'],
            )
            if el[0] == 'apple':
                manufacturer = Apple.objects.create(
                    phone_id = phone,
                    optimization = el[1]['optimization'],
                )
            elif el[0] == 'samsung':
                manufacturer = Samsung.objects.create(
                    phone_id = phone,
                    top_android = el[1]['top_android'],
                )
            elif el[0] == 'xiaomi':
                manufacturer = Xiaomi.objects.create(
                    phone_id = phone,
                    quality_price = el[1]['quality_price'],
                )

            
