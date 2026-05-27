from django.core.management.base import BaseCommand

from catalog.importers import import_shop_yaml


class Command(BaseCommand):
    help = 'Import products from YAML file'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str)

    def handle(self, *args, **options):
        import_shop_yaml(
            options['file_path']
        )

        self.stdout.write(
            self.style.SUCCESS(
                'YAML import completed successfully'
            )
        )