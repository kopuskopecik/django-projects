from django.core.management.base import BaseCommand
from django.utils import timezone

from cars.models import Slot

class Command(BaseCommand):
    help = 'Creating the parking slots'

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help='Indicates the number of parking slots to be created')

    def handle(self, *args, **kwargs):
        slots = Slot.objects.all()
        if slots.exists():
            slots.delete()
        
        total = kwargs['total']
        for i in range(1, total + 1):
            Slot.objects.create()
        self.stdout.write(self.style.SUCCESS(f'{total} parking slots were created with success!'))
        
        with open(".env", "w") as env_file:
            env_file.write(f"total_slot_number={total}")
            self.stdout.write(self.style.SUCCESS(".env file was created with success!"))