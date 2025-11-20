import numpy as np
from numerical.interfaces.matrix_method import MatrixMethod
from shared.utils.plot_matrix_solution import plot_matrix_solution, plot_system_equations


class JacobiService(MatrixMethod):
    def solve(
        self,
        A: list[list[float]],
        b: list[float],
        x0: list[float],
        tolerance: float,
        max_iterations: int,
        precision_type: str = "decimales_correctos",
        **kwargs,
    ) -> dict:

        A = np.array(A)
        b = np.array(b)
        x0 = np.array(x0)

        n = len(b)
        x1 = np.zeros_like(x0)
        current_error = tolerance + 1
        current_iteration = 0
        table = {}
        warnings = []  # ✅ NUEVO: Lista de advertencias

        # ========================================
        # ✅ VALIDACIÓN 1: Diagonal no nula (verificación adicional)
        # ========================================
        for i in range(n):
            if abs(A[i, i]) < 1e-12:
                return {
                    "message_method": f"❌ Error crítico: El elemento diagonal a[{i+1}][{i+1}] = {A[i,i]:.2e} es cero o muy cercano a cero. El método de Jacobi no puede continuar.",
                    "table": {},
                    "is_successful": False,
                    "have_solution": False,
                    "solution": [],
                    "spectral_radius": None,
                }

        # ========================================
        # ✅ VALIDACIÓN 2: Dominancia diagonal (advertencia, no error)
        # ========================================
        for i in range(n):
            diagonal = abs(A[i, i])
            suma_fila = sum(abs(A[i, j]) for j in range(n) if j != i)
            
            if diagonal <= suma_fila:
                warnings.append(
                    f"⚠️ Fila {i+1}: |a[{i+1}][{i+1}]| = {diagonal:.4f} ≤ suma_otros = {suma_fila:.4f}. "
                    "La matriz NO es estrictamente diagonalmente dominante. El método puede no converger."
                )

        # ========================================
        # Cálculo de la matriz de iteración T y radio espectral
        # ========================================
        try:
            D = np.diag(np.diag(A))
            L = np.tril(A, -1)
            U = np.triu(A, 1)

            # Matriz de iteración T para Jacobi
            T = np.linalg.inv(D).dot(L + U)
            spectral_radius = max(abs(np.linalg.eigvals(T)))
            
            # ✅ Advertencia si radio espectral >= 1
            if spectral_radius >= 1:
                warnings.append(
                    f"⚠️ Radio espectral = {spectral_radius:.6f} ≥ 1. "
                    "El método NO convergerá. Verifica que la matriz sea diagonalmente dominante."
                )

        except np.linalg.LinAlgError:
            return {
                "message_method": "❌ Error: No se pudo calcular la matriz de iteración. La matriz D es singular.",
                "table": {},
                "is_successful": False,
                "have_solution": False,
                "solution": [],
                "spectral_radius": None,
            }

        # ========================================
        # Iteración de Jacobi con manejo de excepciones
        # ========================================
        try:
            while current_error > tolerance and current_iteration < max_iterations:
                # Iteración de Jacobi
                for i in range(n):
                    # ✅ Validación adicional durante iteración
                    if abs(A[i, i]) < 1e-14:
                        raise ValueError(f"Diagonal a[{i+1}][{i+1}] se volvió cero durante la iteración {current_iteration}")
                    
                    sum_others = np.dot(A[i, :i], x0[:i]) + np.dot(A[i, i + 1:], x0[i + 1:])
                    x1[i] = (b[i] - sum_others) / A[i, i]

                current_error = np.linalg.norm(x1 - x0, ord=np.inf)

                # Aplicar precisión según el tipo seleccionado
                formatted_x1 = self.apply_precision(x1.tolist(), precision_type, tolerance)
                formatted_error = self.apply_precision([current_error], precision_type, tolerance)[0]

                # Guardamos la información de la iteración actual
                table[current_iteration + 1] = {
                    "iteration": current_iteration + 1,
                    "X": formatted_x1,
                    "Error": formatted_error,
                }

                # Preparación para la siguiente iteración
                x0 = x1.copy()
                current_iteration += 1

        except (ValueError, RuntimeWarning, FloatingPointError) as e:
            return {
                "message_method": f"❌ Error numérico durante las iteraciones: {str(e)}",
                "table": table,
                "is_successful": False,
                "have_solution": False,
                "solution": x1.tolist(),
                "spectral_radius": spectral_radius,
                "warnings": warnings,
            }

        # ========================================
        # Resultados finales
        # ========================================
        result = {}
        
        if current_error <= tolerance:
            message = f"✅ Aproximación encontrada con tolerancia = {tolerance}"
            if warnings:
                message += f"\n\n⚠️ ADVERTENCIAS:\n" + "\n".join(warnings)
            
            result = {
                "message_method": message,
                "table": table,
                "is_successful": True,
                "have_solution": True,
                "solution": formatted_x1,
                "spectral_radius": spectral_radius,
                "warnings": warnings,
            }
        
        elif current_iteration >= max_iterations:
            message = f"⚠️ Se alcanzaron {max_iterations} iteraciones sin convergencia (error final = {current_error:.2e}, radio espectral = {spectral_radius:.6f})"
            if warnings:
                message += f"\n\nPosibles causas:\n" + "\n".join(warnings)
            
            result = {
                "message_method": message,
                "table": table,
                "is_successful": True,
                "have_solution": False,
                "solution": formatted_x1,
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

        # Generar gráficas para 2x2
        if len(A) == 2 and result["have_solution"]:
            try:
                plot_matrix_solution(table, x1.tolist(), spectral_radius)
                plot_system_equations(A.tolist(), b.tolist(), x1.tolist())
            except Exception as e:
                result["warnings"].append(f"⚠️ No se pudieron generar las gráficas: {str(e)}")

        return result

    def apply_precision(self, values, precision_type, tolerance):
        """
        Aplica precisión a una lista de valores basada en el tipo de precisión seleccionado.
        """
        if precision_type == "cifras_significativas":
            significant_figures = -int(np.floor(np.log10(tolerance)))
            return [round(value, significant_figures) for value in values]
        elif precision_type == "decimales_correctos":
            decimal_places = -int(np.floor(np.log10(tolerance)))
            return [round(value, decimal_places) for value in values]
        else:
            return values

    def validate_input(
        self,
        matrix_a_raw: str,
        vector_b_raw: str,
        initial_guess_raw: str,
        tolerance: float,
        max_iterations: int,
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

        # ✅ Verificar diagonal no nula
        A_np = np.array(A)
        for i in range(len(A)):
            if abs(A_np[i, i]) < 1e-12:
                return f"❌ El elemento diagonal a[{i+1}][{i+1}] = {A_np[i,i]:.2e} es cero o muy cercano a cero. El método de Jacobi no puede continuar."

        # Validar compatibilidad de vectores
        if len(b) != len(A) or len(x0) != len(A):
            return "❌ Los vectores b y x₀ deben tener el mismo tamaño que la matriz A."

        return [A, b, x0]
