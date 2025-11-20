import numpy as np
from numerical.interfaces.matrix_method import MatrixMethod
from shared.utils.plot_matrix_solution import plot_matrix_solution, plot_system_equations

class SORService(MatrixMethod):
    def solve(
        self,
        A: list[list[float]],
        b: list[float],
        x0: list[float],
        tolerance: float,
        max_iterations: int,
        relaxation_factor: float,
        **kwargs,
    ) -> dict:

        A = np.array(A)
        b = np.array(b)
        x0 = np.array(x0)

        n = len(b)
        x = x0.copy()
        table = {}
        warnings = []

        # Validaciones extra (diagonal no nula, dominancia diagonal, factor w)
        for i in range(n):
            if abs(A[i, i]) < 1e-12:
                return {
                    "message_method": f"❌ Error crítico: El elemento diagonal a[{i+1}][{i+1}] = {A[i,i]:.2e} es cero o muy cercano a cero.",
                    "table": {},
                    "is_successful": False,
                    "have_solution": False,
                    "solution": [],
                    "spectral_radius": None,
                }

        for i in range(n):
            diagonal = abs(A[i, i])
            suma_fila = sum(abs(A[i, j]) for j in range(n) if j != i)
            if diagonal <= suma_fila:
                warnings.append(
                    f"⚠️ Fila {i+1}: |a[{i+1}][{i+1}]| = {diagonal:.4f} ≤ suma_otros = {suma_fila:.4f}. "
                    "La matriz NO es estrictamente diagonalmente dominante. El método puede no converger."
                )

        if not (0 < relaxation_factor < 2):
            return {
                "message_method": f"❌ Error: El factor de relajación ω = {relaxation_factor} está fuera del rango válido (0, 2).",
                "table": {},
                "is_successful": False,
                "have_solution": False,
                "solution": [],
                "spectral_radius": None,
            }

        # Cálculo de matriz de iteración y radio espectral
        try:
            D = np.diag(np.diag(A))
            L = -np.tril(A, -1)
            U = -np.triu(A, 1)

            T = np.linalg.inv(D - relaxation_factor * L).dot(
                (1 - relaxation_factor) * D + relaxation_factor * U
            )
            spectral_radius = max(abs(np.linalg.eigvals(T)))
            if spectral_radius >= 1:
                warnings.append(
                    f"⚠️ Radio espectral = {spectral_radius:.6f} ≥ 1. "
                    "El método puede NO converger. Ajustá ω o verifica la matriz."
                )
        except np.linalg.LinAlgError:
            return {
                "message_method": "❌ Error: No se pudo calcular la matriz de iteración. La matriz (D - ωL) es singular.",
                "table": {},
                "is_successful": False,
                "have_solution": False,
                "solution": [],
                "spectral_radius": None,
            }

        current_error_rel = tolerance + 1
        current_error_abs = tolerance + 1
        current_iteration = 0

        try:
            while current_error_rel > tolerance and current_iteration < max_iterations:
                x_new = x.copy()
                for i in range(n):
                    if abs(A[i, i]) < 1e-14:
                        raise ValueError(f"Diagonal a[{i+1}][{i+1}] se volvió cero durante la iteración {current_iteration}")
                    sum_others = np.dot(A[i, :i], x_new[:i]) + np.dot(A[i, i + 1:], x[i + 1:])
                    x_new[i] = (1 - relaxation_factor) * x[i] + (relaxation_factor / A[i, i]) * (b[i] - sum_others)

                # --- Calcula ambos errores
                current_error_abs = np.linalg.norm(x_new - x, ord=np.inf)
                # División segura (evita división por cero)
                div = np.where(np.abs(x_new) > 1e-15, np.abs(x_new), 1e-15)
                current_error_rel = np.linalg.norm((x_new - x) / div, ord=np.inf)

                table[current_iteration + 1] = {
                    "iteration": current_iteration + 1,
                    "X": x_new.tolist(),
                    "Error": current_error_rel,
                    "ErrorAbsoluto": current_error_abs,
                }

                x = x_new
                current_iteration += 1

        except (ValueError, RuntimeWarning, FloatingPointError) as e:
            return {
                "message_method": f"❌ Error numérico durante las iteraciones: {str(e)}",
                "table": table,
                "is_successful": False,
                "have_solution": False,
                "solution": x.tolist(),
                "spectral_radius": spectral_radius,
                "warnings": warnings,
            }

        # Resultados finales
        result = {}
        if current_error_rel <= tolerance:
            message = f"✅ Aproximación encontrada con tolerancia = {tolerance}"
            if warnings:
                message += f"\n\n⚠️ ADVERTENCIAS:\n" + "\n".join(warnings)
            result = {
                "message_method": message,
                "table": table,
                "is_successful": True,
                "have_solution": True,
                "solution": x.tolist(),
                "spectral_radius": spectral_radius,
                "warnings": warnings,
            }
        elif current_iteration >= max_iterations:
            message = f"⚠️ Se alcanzaron {max_iterations} iteraciones sin convergencia (error final relativo = {current_error_rel:.2e})"
            if warnings:
                message += f"\n\nPosibles causas:\n" + "\n".join(warnings)
            result = {
                "message_method": message,
                "table": table,
                "is_successful": True,
                "have_solution": False,
                "solution": x.tolist(),
                "spectral_radius": spectral_radius,
                "warnings": warnings,
            }
        else:
            result = {
                "message_method": "❌ El método falló al intentar aproximar una solución",
                "table": table,
                "is_successful": False,
                "have_solution": False,
                "solution": [],
                "spectral_radius": spectral_radius,
                "warnings": warnings,
            }

        # Opcional: genera gráficas para sistemas 2x2
        if len(A) == 2 and result["have_solution"]:
            try:
                plot_matrix_solution(table, x.tolist(), spectral_radius)
                plot_system_equations(A.tolist(), b.tolist(), x.tolist())
            except Exception as e:
                result["warnings"].append(f"⚠️ No se pudieron generar las gráficas: {str(e)}")

        return result

    # (El método validate_input no requiere cambios nuevos, puede quedarse tal cual lo enviaste antes)


    def validate_input(
        self,
        matrix_a_raw: str,
        vector_b_raw: str,
        initial_guess_raw: str,
        tolerance: float,
        max_iterations: int,
        relaxation_factor: float,
        matrix_size: int,
        **kwargs,
    ) -> str | list:

        # Validación de tolerancia
        if not isinstance(tolerance, (int, float)) or tolerance <= 0:
            return "❌ La tolerancia debe ser un número positivo."

        # Validación de iteraciones
        if not isinstance(max_iterations, int) or max_iterations <= 0:
            return "❌ El máximo número de iteraciones debe ser un entero positivo."

        # Validación de entradas numéricas
        try:
            A = [
                [float(num) for num in row.strip().split()]
                for row in matrix_a_raw.replace(";", "\n").split("\n")
                if row.strip()
            ]
            b = [float(num) for num in vector_b_raw.strip().split()]
            x0 = [float(num) for num in initial_guess_raw.strip().split()]
        except ValueError:
            return "❌ Todas las entradas deben ser numéricas."

        # Validar tamaño de matriz
        if len(A) != matrix_size or any(len(row) != matrix_size for row in A):
            return f"❌ La matriz A debe ser cuadrada {matrix_size}x{matrix_size}."

        if len(A) > 7:
            return "❌ La matriz A debe ser de hasta 7x7."

        # Validar compatibilidad de vectores
        if len(b) != len(A) or len(x0) != len(A):
            return "❌ Los vectores b y x₀ deben tener el mismo tamaño que la matriz A."

        # ✅ Verificar diagonal no nula
        A_np = np.array(A)
        for i in range(len(A)):
            if abs(A_np[i, i]) < 1e-12:
                return f"❌ El elemento diagonal a[{i+1}][{i+1}] = {A_np[i,i]:.2e} es cero o muy cercano a cero. El método SOR no puede continuar."

        # Validar factor de relajación
        if relaxation_factor <= 0 or relaxation_factor >= 2:
            return f"❌ El factor de relajación ω = {relaxation_factor} debe estar en el rango (0, 2)."

        return [A, b, x0]
