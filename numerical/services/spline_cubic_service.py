import numpy as np
from numerical.interfaces.interpolation_method import InterpolationMethod
from scipy.interpolate import CubicSpline
from shared.utils.plot_spline import plot_spline_cubic

class SplineCubicService(InterpolationMethod):
    
    def solve(self, x: list[float], y: list[float]) -> dict:
        if len(x) < 3:
            return {
                "message_method": "Se necesitan al menos 3 puntos para calcular un spline cúbico.",
                "is_successful": False,
                "have_solution": False,
            }
        
        # Ordenar los datos por x
        sorted_points = sorted(zip(x, y), key=lambda point: point[0])
        x = np.array([point[0] for point in sorted_points])
        y = np.array([point[1] for point in sorted_points])
        
        cs = CubicSpline(x, y, bc_type='natural')

        # Obtener los coeficientes del spline por tramo
        coefs = cs.c.T
        tramos = []
        for i in range(len(coefs)):
            tramo = (
                f"{coefs[i, 0]:.10f} + {coefs[i, 1]:.10f}*(x - {x[i]:.10f}) "
                f"+ {coefs[i, 2]:.10f}*(x - {x[i]:.10f})^2 + {coefs[i, 3]:.10f}*(x - {x[i]:.10f})^3"
            )
            tramos.append(tramo)

        # Evaluar el spline en puntos originales para calcular errores
        y_approx = cs(x)
        error_abs = float(np.sqrt(np.mean((y - y_approx) ** 2)))
        error_rel = float(np.sqrt(np.mean(
            ((y - y_approx) / (y + 1e-12)) ** 2
        )))
        
        plot_spline_cubic("Spline Cúbico", list(zip(x, y)), x, y)

        return {
            "message_method": "Spline cúbico calculado con éxito.",
            "is_successful": True,
            "have_solution": True,
            "tramos": tramos,
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
