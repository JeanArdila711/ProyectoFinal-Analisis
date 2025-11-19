"""
Calculadora automática de derivadas usando SymPy
"""
from sympy import symbols, diff, sympify, latex
from sympy.parsing.sympy_parser import (
    parse_expr,
    standard_transformations,
    implicit_multiplication_application,
)


def calculate_derivative(function_str: str, order: int = 1) -> dict:
    """
    Calcula la derivada de una función de forma automática
    
    Args:
        function_str: Función como string (ej: "x**2 + 3*x")
        order: Orden de la derivada (1=primera, 2=segunda)
    
    Returns:
        dict con:
            - derivative_str: Derivada como string
            - derivative_latex: Derivada en LaTeX
            - is_successful: bool
            - message: mensaje de error/éxito
    """
    try:
        x = symbols('x')
        
        # Parse con transformaciones para aceptar notación flexible
        transformations = standard_transformations + (implicit_multiplication_application,)
        
        # Intentar parsear la función
        try:
            f = parse_expr(function_str, transformations=transformations)
        except:
            # Fallback sin transformaciones
            f = sympify(function_str)
        
        # Calcular derivada
        df = f
        for _ in range(order):
            df = diff(df, x)
        
        # Convertir a string simplificado
        derivative_str = str(df)
        
        # Convertir a LaTeX para mostrar bonito
        derivative_latex = latex(df)
        
        return {
            "derivative_str": derivative_str,
            "derivative_latex": derivative_latex,
            "is_successful": True,
            "message": f"Derivada de orden {order} calculada exitosamente",
        }
    
    except Exception as e:
        return {
            "derivative_str": "",
            "derivative_latex": "",
            "is_successful": False,
            "message": f"Error al calcular derivada: {str(e)}",
        }


def calculate_first_derivative(function_str: str) -> str:
    """Shortcut para primera derivada (retorna solo el string)"""
    result = calculate_derivative(function_str, order=1)
    return result["derivative_str"] if result["is_successful"] else ""


def calculate_second_derivative(function_str: str) -> str:
    """Shortcut para segunda derivada"""
    result = calculate_derivative(function_str, order=2)
    return result["derivative_str"] if result["is_successful"] else ""
