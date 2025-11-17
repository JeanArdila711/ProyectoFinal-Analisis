from django.apps import AppConfig

class NumericalConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'numerical'

    def ready(self):
        """Se ejecuta cuando Django carga la aplicación"""
        from numerical.containers.numerical_method_container import NumericalMethodContainer
        
        # Crear instancia del container
        container = NumericalMethodContainer()
        
        # Hacer wiring con los módulos que usan inyección
        container.wire(
            packages=['numerical.views'],  # Wire todas las views
        )
        
        print("✅ Container wired successfully!")
