import math
from numerical.interfaces.interval_method import (
    IntervalMethod,
)
from shared.utils.plot_function import plot_function
"""
El método de la secante es una técnica numérica para encontrar raíces de ecuaciones no lineales utilizando dos puntos iniciales interval_a y interval_b. La idea es aproximar la raíz mediante la intersección de la recta secante entre (a, f(a)) y (b, f(b)) con el eje x, y luego usar este nuevo punto como base para iterar el proceso hasta alcanzar una tolerancia deseada.
"""


class SecantService(IntervalMethod):
    def solve(
        self,
        function_f: str,
        x0: float,  # ← primer punto
        tolerance: float,
        max_iterations: int,
        precision: bool = False,
        interval_b: float = None,  # ← segundo punto
        **kwargs,
    ) -> dict:
        
        # Asignar los nombres internos
        interval_a = x0
        # interval_b ya viene como parámetro
        
        # Validar que interval_b no sea None
        if interval_b is None:
            return {
                "message_method": "El método de Secante requiere dos puntos iniciales. Por favor, proporcione interval_b.",
                "table": {},
                "is_successful": False,
                "have_solution": False,
                "root": 0.0,
            }
        
        # Resto del código sigue igual...
        table = {}
        current_iteration = 1
        current_error = math.inf
        
        # Evaluamos la función en los puntos iniciales
        try:
            f_a = eval(str(function_f), {"x": interval_a, "math": math})
            f_b = eval(str(function_f), {"x": interval_b, "math": math})
        except Exception as e:
            return {
                "message_method": f"Error al evaluar la función en los puntos iniciales: {str(e)}.",
                "table": {},
                "is_successful": False,
                "have_solution": False,
                "root": 0.0,
            }

        # Bucle del método de la secante
        while current_iteration <= max_iterations:
            # Almacenamos la información de la iteración actual en la tabla.
            table[current_iteration] = {}
            # Comprobamos si se puede continuar con la fórmula de la secante
            if f_b - f_a == 0:
                return {
                    "message_method": "Error: División por cero debido a que f(b) y f(a) son iguales.",
                    "table": table,
                    "is_successful": False,
                    "have_solution": False,
                    "root": 0.0,
                }
            # Calculamos el valor aproximado usando la fórmula de la secante
            Xn = interval_b - (f_b * (interval_b - interval_a) / (f_b - f_a))
            # Evaluamos la función en el nuevo valor aproximado
            try:
                f = eval(str(function_f), {"x": Xn, "math": math})
            except Exception as e:
                return {
                    "message_method": f"Error al evaluar la función en el punto aproximado: {str(e)}.",
                    "table": table,
                    "is_successful": False,
                    "have_solution": False,
                    "root": 0.0,
                }
            # Guardamos los datos de la iteración actual en la tabla.
            table[current_iteration]["iteration"] = current_iteration
            table[current_iteration]["a"] = interval_a
            table[current_iteration]["b"] = interval_b
            table[current_iteration]["f_a"] = f_a
            table[current_iteration]["f_b"] = f_b
            table[current_iteration]["approximate_value"] = Xn
            table[current_iteration]["f_evaluated"] = f
            # Para la primera iteración, el error se mantiene como infinito (no hay valor previo para comparar).
            if current_iteration == 1:
                table[current_iteration]["error"] = current_error
            # Calculamos el error dependiendo de la precisión
            else:
                if precision:  # Precisión absoluta
                    current_error = abs(
                        table[current_iteration]["approximate_value"]
                        - table[current_iteration - 1]["approximate_value"]
                    )
                else:  # Precisión relativa
                    current_error = abs(
                        (
                            table[current_iteration]["approximate_value"]
                            - table[current_iteration - 1]["approximate_value"]
                        )
                        / table[current_iteration]["approximate_value"]
                    )
                table[current_iteration]["error"] = current_error
            # Si la función evaluada en el valor aproximado es cero, hemos encontrado la raíz exacta.
            if f == 0:
                return {
                    "message_method": "{} es raiz de f(x)".format(Xn),
                    "table": table,
                    "is_successful": True,
                    "have_solution": True,
                    "root": Xn,
                }
            # Si el error es menor que la tolerancia especificada, aceptamos el valor aproximado como una aproximación de la raíz.
            elif current_error < tolerance:
                return {
                    "message_method": "{} es una aproximación de la raiz de f(x) con un error de {}".format(
                        Xn, current_error
                    ),
                    "table": table,
                    "is_successful": True,
                    "have_solution": True,
                    "root": Xn,
                }
            # Actualizamos los puntos para la siguiente iteración
            interval_a = interval_b
            interval_b = Xn
            # Re-evaluar las funciones en los nuevos puntos
            try:
                f_a = eval(str(function_f), {"x": interval_a, "math": math})
                f_b = eval(str(function_f), {"x": interval_b, "math": math})
            except Exception as e:
                return {
                    "message_method": f"Error durante la evaluación en el nuevo intervalo: {str(e)}.",
                    "table": table,
                    "is_successful": False,
                    "have_solution": False,
                    "root": 0.0,
                }
            # Incrementamos el contador de iteraciones.
            current_iteration += 1
        # Si se alcanzó el número máximo de iteraciones sin encontrar una raíz, se retorna un mensaje de fallo.
        return {
            "message_method": "El método funcionó correctamente pero no se encontró solución para {} iteraciones".format(
                max_iterations
            ),
            "table": table,
            "is_successful": True,
            "have_solution": False,
            "root": 0.0,
        }

    def validate_input(
        self,
        x0: float,
        tolerance: float,
        max_iterations: int,
        function_f: str,
        **kwargs,
    ) -> str | bool:
        interval_a = x0
        interval_b = kwargs.get("interval_b")

        # Validación de interval_b
        if interval_b is None:
            return "El método de Secante requiere dos puntos iniciales. Por favor, proporcione interval_b."

        # Validación de los parámetros de entrada tolerancia positiva
        if not isinstance(tolerance, (int, float)) or tolerance <= 0:
            return "La tolerancia debe ser un número positivo"

        # Validación de los parámetros de entrada maximo numero de iteraciones positivo
        if not isinstance(max_iterations, int) or max_iterations <= 0:
            return "El máximo número de iteraciones debe ser un entero positivo."

        # Evaluamos la función en los puntos iniciales interval_a y interval_b
        
        try:
            f_a = eval(str(function_f), {"x": interval_a, "math": math})
            f_b = eval(str(function_f), {"x": interval_b, "math": math})
        except ValueError as ve:
            plot_function(function_f, False, [(interval_a, 0), (interval_b, 0)]);
            return f"Error de dominio matemático al evaluar la función: {str(ve)}. Asegúrese de que los valores iniciales están en el dominio válido de la función."
       
        except SyntaxError:
            return "Error de sintaxis en la función ingresada: Verifique la expresión y asegúrese de que sea válida en Python."

        except NameError:
            return "Error de nombre en la función ingresada: Nombre no definido en la función. Asegúrese de usar la variable 'x' y las funciones de la biblioteca 'math' correctamente."

        except ZeroDivisionError:
            plot_function(function_f, False, [(interval_a, 0), (interval_b, 0)]);
            return "Error: División por cero en la función. Asegúrese de que la función no tenga denominadores que se anulen en el intervalo dado."

        except Exception as e:
            return f"Error desconocido: {str(e)}."
        
        # Si el producto de los valores en los extremos del intervalo es positivo, no se puede garantizar la existencia de una raíz.
        if f_a * f_b > 0:
            plot_function(function_f, False, [(interval_a, 0), (interval_b, 0)]);
            return "El intervalo es inadecuado, recuerde que se debe encontrar un raíz para el intervalo dado"

        # Validación de division por cero en la formula de regla falsa
        if f_a == f_b:
            plot_function(function_f, False, [(interval_a, 0), (interval_b, 0)]);
            return "División por cero. Los valores de f(a) y f(b) son iguales, lo cual impide aplicar la Regla Falsa."
                

        return True
