from django.db import migrations

CHEFS = [
    ('Auguste Escoffier', 'Cocina clásica francesa', 15),
    ('Gastón Acurio', 'Cocina peruana', 30),
    ('Carolina Bazán', 'Cocina de autor chilena', 18),
]


def cargar_chefs(apps, schema_editor):
    Chef = apps.get_model('catalogo', 'Chef')
    for nombre, especialidad, anios in CHEFS:
        Chef.objects.get_or_create(
            nombre=nombre,
            defaults={'especialidad': especialidad, 'anios_experiencia': anios},
        )


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0002_categoria'),
    ]

    operations = [
        # Al revertir no se borra nada, para no eliminar chefs creados a mano.
        migrations.RunPython(cargar_chefs, migrations.RunPython.noop),
    ]
