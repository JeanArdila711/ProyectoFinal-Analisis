"""
Context processors globales para toda la aplicación
Inyecta automáticamente el contenido de ayuda según la URL
"""
from numerical.help_content import HELP_CONTENT


def help_content_processor(request):
    """
    Inyecta el contenido de ayuda en el contexto de todas las vistas
    basándose en la URL actual
    
    Args:
        request: HttpRequest de Django
    
    Returns:
        dict: Contexto con datos de ayuda si la URL tiene contenido definido
    """
    # Mapeo de URLs a claves de métodos en HELP_CONTENT
    url_to_method = {
        # CAPÍTULO 1: Ecuaciones No Lineales
        '/numerical/cap1/newton-raphson/': 'newton_raphson',
        '/numerical/cap1/multiple-roots/': 'multiple_roots',
        '/numerical/cap1/bisection/': 'biseccion',
        '/numerical/cap1/regula-falsi/': 'regula_falsi',
        '/numerical/cap1/secant/': 'secante',
        '/numerical/cap1/fixed-point/': 'punto_fijo',
        
        # CAPÍTULO 2: Sistemas Lineales
        '/numerical/cap2/jacobi/': 'jacobi',
        '/numerical/cap2/gauss-seidel/': 'gauss_seidel',
        '/numerical/cap2/sor/': 'sor',
        
        # CAPÍTULO 3: Interpolación
        '/numerical/cap3/vandermonde/': 'vandermonde',
        '/numerical/cap3/newton-interpol/': 'newton_interpol',
        '/numerical/cap3/lagrange/': 'lagrange',
        '/numerical/cap3/spline-linear/': 'spline_linear',
        '/numerical/cap3/spline-cubic/': 'spline_cubic',
    }
    
    current_path = request.path
    method_key = url_to_method.get(current_path)
    
    if method_key and method_key in HELP_CONTENT:
        return {
            'help_content': HELP_CONTENT[method_key],  # Solo el contenido
        }
    
    return {}
