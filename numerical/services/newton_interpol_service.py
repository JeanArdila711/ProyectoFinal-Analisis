import numpy as np
import sympy as sp
from numerical.interfaces.interpolation_method import InterpolationMethod

class NewtonInterpolService(InterpolationMethod):
    def solve(self, x: list[float], y: list[float]) -> dict:
        if len(x) != len(y):
            return {
                "message_method": "Error: Las listas de 'x' y 'y' deben tener la misma cantidad de elementos.",
                "polynomial": "",
                "is_successful": False,
                "have_solution": False,
            }

        n = len(x)
        divided_diff_table = np.zeros((n, n))
        divided_diff_table[:, 0] = y

        for j in range(1, n):
            for i in range(n - j):
                divided_diff_table[i, j] = (
                    divided_diff_table[i + 1, j - 1] - divided_diff_table[i, j - 1]
                ) / (x[i + j] - x[i])

        coefficients = divided_diff_table[0, :]

        x_symbol = sp.symbols("x")
        polynomial = coefficients[0]
        term = 1

        for i in range(1, n):
            term *= (x_symbol - x[i - 1])
            polynomial += coefficients[i] * term

        simplified_polynomial = sp.simplify(polynomial)

        # Evaluar el polinomio en los puntos originales para errores
        f_poly = sp.lambdify(x_symbol, simplified_polynomial, "numpy")
        x_np = np.array(x)
        y_np = np.array(y)
        y_approx = f_poly(x_np)

        error_abs = float(np.sqrt(np.mean((y_np - y_approx) ** 2)))
        error_rel = float(np.sqrt(np.mean(
            ((y_np - y_approx) / (y_np + 1e-12)) ** 2
        )))

        return {
            "message_method": "El polinomio interpolante fue encontrado con éxito.",
            "polynomial": str(simplified_polynomial),
            "is_successful": True,
            "have_solution": True,
            "error_absoluto": error_abs,
            "error_relativo": error_rel,
        }

    def validate_input(self, x_input: str, y_input: str) -> str | list[tuple[float, float]]:
        max_points = 10

        x_list = [value.strip() for value in x_input.split(" ") if value.strip()]
        y_list = [value.strip() for value in y_input.split(" ") if value.strip()]

        if len(x_list) == 0 or len(y_list) == 0:
            return "Error: Las listas de 'x' y 'y' no pueden estar vacías."
        if len(x_list) != len(y_list):
            return "Error: Las listas de 'x' y 'y' deben tener la misma cantidad de elementos."
        try:
            x_values = [float(value) for value in x_list]
            y_values = [float(value) for value in y_list]
        except ValueError:
            return "Error: Todos los valores de 'x' y 'y' deben ser numéricos."
        if len(set(x_values)) != len(x_values):
            return "Error: Los valores de 'x' deben ser únicos."
        if len(x_values) > max_points:
            return f"Error: El número máximo de puntos es {max_points}."
        return [x_values, y_values]
