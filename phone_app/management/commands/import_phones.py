from django.core.management.base import BaseCommand
import csv

from phone_app.models import Phone


class Command(BaseCommand):

    def handle(self, *args, **options):
       
        with open('phones.csv', 'r', encoding='UTF-8') as f:
            phones = list(csv.DictReader(f, delimiter=';'))

        for phone in phones:
            model = Phone(
                name=phone.get('name'),
                price=float(phone.get('price')),
                image = phone.get('image'),
                release_date = phone.get('release_date'),
                lte_exists = phone.get('lte_exists'),
                slug = phone.get('name').lower().replace(' ', '-')
            )
            model.save()