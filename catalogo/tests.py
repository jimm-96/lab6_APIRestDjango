from django.test import TestCase

from .models import Chef


class ChefEndpointTests(TestCase):
    def setUp(self):
        # Parte sin registros para que el conteo no dependa de datos precargados.
        Chef.objects.all().delete()
        Chef.objects.create(
            nombre='Auguste Escoffier',
            especialidad='Cocina francesa',
            anios_experiencia=15,
        )
        Chef.objects.create(
            nombre='Gastón Acurio',
            especialidad='Cocina peruana',
            anios_experiencia=30,
        )

    def test_get_chefs_devuelve_200_y_todos_los_registros(self):
        respuesta = self.client.get('/api/chefs/')

        self.assertEqual(respuesta.status_code, 200)
        self.assertEqual(len(respuesta.json()), 2)
