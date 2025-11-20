import numpy as np
from numerical.interfaces.interpolation_method import InterpolationMethod
from shared.utils.plot_spline import plot_spline_linear

class SplineLinearService(InterpolationMethod):
    def solve(
        self,
        x: list[float],
        y: list[float],
    ) -> dict:
        n = len(x)
        if n < 2:
            return {
                "message_method": "Se necesitan al menos 2 puntos para calcular un spline lineal.",
                "is_successful": False,
                "have_solution": False,
                "tramos": [],
            }

        tramos = []
        equations = []

        # Evaluar el spline en los puntos de entrada (y_approx)
        y_approx = []
        for i in range(n - 1):
            m = (y[i + 1] - y[i]) / (x[i + 1] - x[i])
            tramo = f"{m:.10f}*(x - ({x[i]:.10f})) + {y[i]:.10f}"
            tramos.append(tramo)
            equations.append(f"Tramo {i + 1}: {tramo}")

            # Evaluar el tramo lineal para x[i]
            y_approx.append(y[i])
        # El último punto lo replica literalmente (el spline conecta todos)
        y_approx.append(y[-1])

        # Errores respecto a los valores y originales
        y_approx = np.array(y_approx)
        y_real = np.array(y)
        error_abs = float(np.sqrt(np.mean((y_real - y_approx) ** 2)))
        error_rel = float(np.sqrt(np.mean(
            ((y_real - y_approx) / (y_real + 1e-12)) ** 2
        )))

        points = list(zip(x, y))
        sorted_points = sorted(points, key=lambda point: point[0])
        plot_spline_linear(sorted_points)

        return {
            "message_method": "Spline lineal calculado con éxito.",
            "is_successful": True,
            "have_solution": True,
            "tramos": tramos,
            "equations": equations,
            "error_absoluto": error_abs,
            "error_relativo": error_rel,
        }

    def validate_input(
        self, x_input: str, y_input: str
    ) -> str | list[tuple[float, float]]:
        max_points = 8

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
