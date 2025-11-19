from django.http import JsonResponse
from django.views import View
import json
from shared.utils.derivate_calculator import calculate_derivative


class DerivativeCalculatorView(View):
    """
    Endpoint AJAX para calcular derivadas
    """
    
    def post(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body)
            function_str = data.get('function', '')
            order = int(data.get('order', 1))
            
            if not function_str:
                return JsonResponse({
                    'is_successful': False,
                    'message': 'Función vacía',
                    'derivative_str': '',
                }, status=400)
            
            # Calcular derivada
            result = calculate_derivative(function_str, order=order)
            
            return JsonResponse(result)
        
        except Exception as e:
            return JsonResponse({
                'is_successful': False,
                'message': f'Error: {str(e)}',
                'derivative_str': '',
            }, status=500)
