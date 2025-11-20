"""
Guías de uso para métodos numéricos
Cap 1: Con acordeón colapsable
Cap 2 y 3: Fijos (sin acordeón)
"""

# ==========================================
# CONTENIDO DE AYUDA POR MÉTODO
# ==========================================

HELP_CONTENT = {
    # ==========================================
    # CAPÍTULO 1
    # ==========================================
    
    'biseccion': '''
        <h4 style="color:#ffc107;" class="mb-3">GUÍA PARA INGRESAR LOS PARÁMETROS</h4>
    <!-- Acordeón Item 1: Operadores -->
    <div class="accordion-item" style="background:#232d3e; color:#fff; border:1.5px solid #343a40;">
        <h2 class="accordion-header">
            <button class="accordion-button collapsed"
                    style="background:#232d3e; color:#ffd54f; font-weight:bold;"
                    type="button" data-bs-toggle="collapse" data-bs-target="#collapse-operadores">
                 Operadores Matemáticos
            </button>
        </h2>
        <div id="collapse-operadores" class="accordion-collapse collapse" data-bs-parent="#helpAccordion">
            <div class="accordion-body" style="background:#262a32; color:#fff;">
                <table class="table table-dark table-sm" style="border-radius:7px;overflow:hidden;">
                    <thead>
                        <tr><th>Operación</th><th>Símbolo</th><th>Ejemplo</th></tr>
                    </thead>
                    <tbody>
                        <tr><td>Suma</td><td><code>+</code></td><td><code>x + 5</code></td></tr>
                        <tr><td>Resta</td><td><code>-</code></td><td><code>x - 3</code></td></tr>
                        <tr><td>Multiplicación</td><td><code>*</code></td><td><code>3*x</code></td></tr>
                        <tr><td>División</td><td><code>/</code></td><td><code>x/2</code></td></tr>
                        <tr><td>Potencia</td><td><code>**</code></td><td><code>x**2</code>, <code>x**3</code></td></tr>
                    </tbody>
                </table>
            </div>
        </div>
    </div>

    <!-- Acordeón Item 2: Funciones -->
    <div class="accordion-item" style="background:#232d3e; color:#fff; border:1.5px solid #343a40;">
        <h2 class="accordion-header">
            <button class="accordion-button collapsed"
                    style="background:#232d3e; color:#ffd54f;"
                    type="button" data-bs-toggle="collapse" data-bs-target="#collapse-funciones">
                 Funciones Matemáticas
            </button>
        </h2>
        <div id="collapse-funciones" class="accordion-collapse collapse" data-bs-parent="#helpAccordion">
            <div class="accordion-body" style="background:#262a32; color:#fff;">
                <ul>
                    <li><code>math.sin(x)</code> → Seno</li>
                    <li><code>math.cos(x)</code> → Coseno</li>
                    <li><code>math.tan(x)</code> → Tangente</li>
                    <li><code>math.log(x)</code> → Logaritmo natural</li>
                    <li><code>math.log10(x)</code> → Log base 10</li>
                    <li><code>math.exp(x)</code> → Exponencial</li>
                    <li><code>math.sqrt(x)</code> → Raíz cuadrada</li>
                </ul>
            </div>
        </div>
    </div>

    <!-- Acordeón Item 3: Paréntesis -->
    <div class="accordion-item" style="background:#232d3e; color:#fff; border:1.5px solid #343a40;">
        <h2 class="accordion-header">
            <button class="accordion-button collapsed"
                    style="background:#232d3e; color:#ffd54f;"
                    type="button" data-bs-toggle="collapse" data-bs-target="#collapse-parentesis">
                Uso de Paréntesis
            </button>
        </h2>
        <div id="collapse-parentesis" class="accordion-collapse collapse" data-bs-parent="#helpAccordion">
            <div class="accordion-body" style="background:#262a32; color:#fff;">
                <h6 style="color:#87ea97;"> CORRECTO:</h6>
                <ul>
                    <li><code>(x + 2) / (x - 1)</code></li>
                    <li><code>math.sin(x + 1)</code></li>
                </ul>
                <h6 style="color:#ffd54f;"> INCORRECTO:</h6>
                <ul>
                    <li><code>x + 2 / x - 1</code></li>
                    <li><code>2x + 5</code> (falta *)</li>
                </ul>
            </div>
        </div>
    </div>
        
        <!-- Acordeón Item 4: Parámetros Específicos -->
        <div class="accordion-item bg-info">
            <h2 class="accordion-header">
                <button class="accordion-button collapsed bg-info text-dark fw-bold" type="button" data-bs-toggle="collapse" data-bs-target="#collapse-parametros">
                     Parámetros de Bisección
                </button>
            </h2>
            <div id="collapse-parametros" class="accordion-collapse collapse" data-bs-parent="#helpAccordion">
                <div class="accordion-body bg-dark text-white">
                    <h6>1. FUNCIÓN f(x):</h6>
                    <p><code>x**3 - 2*x - 5</code></p>
                    
                    <h6 class="mt-3">2. INTERVALO [a, b]:</h6>
                    <p>a = <code>0</code>, b = <code>3</code></p>
                    <p class="text-danger"><strong></strong> Debe cumplir f(a) × f(b) &lt; 0</p>
                    
                    <h6 class="mt-3">3. TOLERANCIA:</h6>
                    <p><code>5e-5</code></p>
                    
                    <h6 class="mt-3">4. ITERACIONES MÁXIMAS:</h6>
                    <p><code>100</code></p>
                </div>
            </div>
        </div>
    ''',
    
    'regula_falsi': '''
        <h4 style="color:#ffc107;" class="mb-3">GUÍA PARA INGRESAR LOS PARÁMETROS</h4>
    <!-- Acordeón Item 1: Operadores -->
    <div class="accordion-item" style="background:#232d3e; color:#fff; border:1.5px solid #343a40;">
        <h2 class="accordion-header">
            <button class="accordion-button collapsed"
                    style="background:#232d3e; color:#ffd54f; font-weight:bold;"
                    type="button" data-bs-toggle="collapse" data-bs-target="#collapse-operadores">
                 Operadores Matemáticos
            </button>
        </h2>
        <div id="collapse-operadores" class="accordion-collapse collapse" data-bs-parent="#helpAccordion">
            <div class="accordion-body" style="background:#262a32; color:#fff;">
                <table class="table table-dark table-sm" style="border-radius:7px;overflow:hidden;">
                    <thead>
                        <tr><th>Operación</th><th>Símbolo</th><th>Ejemplo</th></tr>
                    </thead>
                    <tbody>
                        <tr><td>Suma</td><td><code>+</code></td><td><code>x + 5</code></td></tr>
                        <tr><td>Resta</td><td><code>-</code></td><td><code>x - 3</code></td></tr>
                        <tr><td>Multiplicación</td><td><code>*</code></td><td><code>3*x</code></td></tr>
                        <tr><td>División</td><td><code>/</code></td><td><code>x/2</code></td></tr>
                        <tr><td>Potencia</td><td><code>**</code></td><td><code>x**2</code>, <code>x**3</code></td></tr>
                    </tbody>
                </table>
            </div>
        </div>
    </div>

    <!-- Acordeón Item 2: Funciones -->
    <div class="accordion-item" style="background:#232d3e; color:#fff; border:1.5px solid #343a40;">
        <h2 class="accordion-header">
            <button class="accordion-button collapsed"
                    style="background:#232d3e; color:#ffd54f;"
                    type="button" data-bs-toggle="collapse" data-bs-target="#collapse-funciones">
                 Funciones Matemáticas
            </button>
        </h2>
        <div id="collapse-funciones" class="accordion-collapse collapse" data-bs-parent="#helpAccordion">
            <div class="accordion-body" style="background:#262a32; color:#fff;">
                <ul>
                    <li><code>math.sin(x)</code> → Seno</li>
                    <li><code>math.cos(x)</code> → Coseno</li>
                    <li><code>math.tan(x)</code> → Tangente</li>
                    <li><code>math.log(x)</code> → Logaritmo natural</li>
                    <li><code>math.log10(x)</code> → Log base 10</li>
                    <li><code>math.exp(x)</code> → Exponencial</li>
                    <li><code>math.sqrt(x)</code> → Raíz cuadrada</li>
                </ul>
            </div>
        </div>
    </div>

    <!-- Acordeón Item 3: Paréntesis -->
    <div class="accordion-item" style="background:#232d3e; color:#fff; border:1.5px solid #343a40;">
        <h2 class="accordion-header">
            <button class="accordion-button collapsed"
                    style="background:#232d3e; color:#ffd54f;"
                    type="button" data-bs-toggle="collapse" data-bs-target="#collapse-parentesis">
                Uso de Paréntesis
            </button>
        </h2>
        <div id="collapse-parentesis" class="accordion-collapse collapse" data-bs-parent="#helpAccordion">
            <div class="accordion-body" style="background:#262a32; color:#fff;">
                <h6 style="color:#87ea97;"> CORRECTO:</h6>
                <ul>
                    <li><code>(x + 2) / (x - 1)</code></li>
                    <li><code>math.sin(x + 1)</code></li>
                </ul>
                <h6 style="color:#ffd54f;"> INCORRECTO:</h6>
                <ul>
                    <li><code>x + 2 / x - 1</code></li>
                    <li><code>2x + 5</code> (falta *)</li>
                </ul>
            </div>
        </div>
    </div>
        
        <div class="accordion-item bg-info">
            <h2 class="accordion-header">
                <button class="accordion-button collapsed bg-info text-dark fw-bold" type="button" data-bs-toggle="collapse" data-bs-target="#collapse-parametros">
                     Parámetros de Regla Falsa
                </button>
            </h2>
            <div id="collapse-parametros" class="accordion-collapse collapse" data-bs-parent="#helpAccordion">
                <div class="accordion-body bg-dark text-white">
                    <h6>1. FUNCIÓN f(x):</h6>
                    <p><code>x**3 - x - 2</code></p>
                    
                    <h6 class="mt-3">2. INTERVALO [a, b]:</h6>
                    <p>a = <code>1</code>, b = <code>2</code></p>
                    <p class="text-danger"><strong></strong> Debe cumplir f(a) × f(b) &lt; 0</p>
                    
                    <h6 class="mt-3">3. TOLERANCIA:</h6>
                    <p><code>5e-5</code></p>
                </div>
            </div>
        </div>
    ''',
    
    'newton_raphson': '''
        <h4 style="color:#ffc107;" class="mb-3">GUÍA PARA INGRESAR LOS PARÁMETROS</h4>
    <!-- Acordeón Item 1: Operadores -->
    <div class="accordion-item" style="background:#232d3e; color:#fff; border:1.5px solid #343a40;">
        <h2 class="accordion-header">
            <button class="accordion-button collapsed"
                    style="background:#232d3e; color:#ffd54f; font-weight:bold;"
                    type="button" data-bs-toggle="collapse" data-bs-target="#collapse-operadores">
                 Operadores Matemáticos
            </button>
        </h2>
        <div id="collapse-operadores" class="accordion-collapse collapse" data-bs-parent="#helpAccordion">
            <div class="accordion-body" style="background:#262a32; color:#fff;">
                <table class="table table-dark table-sm" style="border-radius:7px;overflow:hidden;">
                    <thead>
                        <tr><th>Operación</th><th>Símbolo</th><th>Ejemplo</th></tr>
                    </thead>
                    <tbody>
                        <tr><td>Suma</td><td><code>+</code></td><td><code>x + 5</code></td></tr>
                        <tr><td>Resta</td><td><code>-</code></td><td><code>x - 3</code></td></tr>
                        <tr><td>Multiplicación</td><td><code>*</code></td><td><code>3*x</code></td></tr>
                        <tr><td>División</td><td><code>/</code></td><td><code>x/2</code></td></tr>
                        <tr><td>Potencia</td><td><code>**</code></td><td><code>x**2</code>, <code>x**3</code></td></tr>
                    </tbody>
                </table>
            </div>
        </div>
    </div>

    <!-- Acordeón Item 2: Funciones -->
    <div class="accordion-item" style="background:#232d3e; color:#fff; border:1.5px solid #343a40;">
        <h2 class="accordion-header">
            <button class="accordion-button collapsed"
                    style="background:#232d3e; color:#ffd54f;"
                    type="button" data-bs-toggle="collapse" data-bs-target="#collapse-funciones">
                 Funciones Matemáticas
            </button>
        </h2>
        <div id="collapse-funciones" class="accordion-collapse collapse" data-bs-parent="#helpAccordion">
            <div class="accordion-body" style="background:#262a32; color:#fff;">
                <ul>
                    <li><code>math.sin(x)</code> → Seno</li>
                    <li><code>math.cos(x)</code> → Coseno</li>
                    <li><code>math.tan(x)</code> → Tangente</li>
                    <li><code>math.log(x)</code> → Logaritmo natural</li>
                    <li><code>math.log10(x)</code> → Log base 10</li>
                    <li><code>math.exp(x)</code> → Exponencial</li>
                    <li><code>math.sqrt(x)</code> → Raíz cuadrada</li>
                </ul>
            </div>
        </div>
    </div>

    <!-- Acordeón Item 3: Paréntesis -->
    <div class="accordion-item" style="background:#232d3e; color:#fff; border:1.5px solid #343a40;">
        <h2 class="accordion-header">
            <button class="accordion-button collapsed"
                    style="background:#232d3e; color:#ffd54f;"
                    type="button" data-bs-toggle="collapse" data-bs-target="#collapse-parentesis">
                Uso de Paréntesis
            </button>
        </h2>
        <div id="collapse-parentesis" class="accordion-collapse collapse" data-bs-parent="#helpAccordion">
            <div class="accordion-body" style="background:#262a32; color:#fff;">
                <h6 style="color:#87ea97;"> CORRECTO:</h6>
                <ul>
                    <li><code>(x + 2) / (x - 1)</code></li>
                    <li><code>math.sin(x + 1)</code></li>
                </ul>
                <h6 style="color:#ffd54f;"> INCORRECTO:</h6>
                <ul>
                    <li><code>x + 2 / x - 1</code></li>
                    <li><code>2x + 5</code> (falta *)</li>
                </ul>
            </div>
        </div>
    </div>
        
        <div class="accordion-item bg-info">
            <h2 class="accordion-header">
                <button class="accordion-button collapsed bg-info text-dark fw-bold" type="button" data-bs-toggle="collapse" data-bs-target="#collapse-parametros">
                     Parámetros de Newton-Raphson
                </button>
            </h2>
            <div id="collapse-parametros" class="accordion-collapse collapse" data-bs-parent="#helpAccordion">
                <div class="accordion-body bg-dark text-white">
                    <h6>1. FUNCIÓN f(x):</h6>
                    <p><code>x**3 - 2*x - 5</code></p>
                    
                    <h6 class="mt-3">2. DERIVADA f'(x):</h6>
                    <p>Usa el botón <span class="badge bg-warning"> Calcular Automáticamente</span></p>
                    <p>O ingresa: <code>3*x**2 - 2</code></p>
                    
                    <h6 class="mt-3">3. VALOR INICIAL x₀:</h6>
                    <p><code>1.5</code></p>
                    
                    <h6 class="mt-3">4. TOLERANCIA:</h6>
                    <p><code>5e-5</code></p>
                </div>
            </div>
        </div>
    ''',
    
    'secante': '''
        <h4 style="color:#ffc107;" class="mb-3">GUÍA PARA INGRESAR LOS PARÁMETROS</h4>
    <!-- Acordeón Item 1: Operadores -->
    <div class="accordion-item" style="background:#232d3e; color:#fff; border:1.5px solid #343a40;">
        <h2 class="accordion-header">
            <button class="accordion-button collapsed"
                    style="background:#232d3e; color:#ffd54f; font-weight:bold;"
                    type="button" data-bs-toggle="collapse" data-bs-target="#collapse-operadores">
                 Operadores Matemáticos
            </button>
        </h2>
        <div id="collapse-operadores" class="accordion-collapse collapse" data-bs-parent="#helpAccordion">
            <div class="accordion-body" style="background:#262a32; color:#fff;">
                <table class="table table-dark table-sm" style="border-radius:7px;overflow:hidden;">
                    <thead>
                        <tr><th>Operación</th><th>Símbolo</th><th>Ejemplo</th></tr>
                    </thead>
                    <tbody>
                        <tr><td>Suma</td><td><code>+</code></td><td><code>x + 5</code></td></tr>
                        <tr><td>Resta</td><td><code>-</code></td><td><code>x - 3</code></td></tr>
                        <tr><td>Multiplicación</td><td><code>*</code></td><td><code>3*x</code></td></tr>
                        <tr><td>División</td><td><code>/</code></td><td><code>x/2</code></td></tr>
                        <tr><td>Potencia</td><td><code>**</code></td><td><code>x**2</code>, <code>x**3</code></td></tr>
                    </tbody>
                </table>
            </div>
        </div>
    </div>

    <!-- Acordeón Item 2: Funciones -->
    <div class="accordion-item" style="background:#232d3e; color:#fff; border:1.5px solid #343a40;">
        <h2 class="accordion-header">
            <button class="accordion-button collapsed"
                    style="background:#232d3e; color:#ffd54f;"
                    type="button" data-bs-toggle="collapse" data-bs-target="#collapse-funciones">
                 Funciones Matemáticas
            </button>
        </h2>
        <div id="collapse-funciones" class="accordion-collapse collapse" data-bs-parent="#helpAccordion">
            <div class="accordion-body" style="background:#262a32; color:#fff;">
                <ul>
                    <li><code>math.sin(x)</code> → Seno</li>
                    <li><code>math.cos(x)</code> → Coseno</li>
                    <li><code>math.tan(x)</code> → Tangente</li>
                    <li><code>math.log(x)</code> → Logaritmo natural</li>
                    <li><code>math.log10(x)</code> → Log base 10</li>
                    <li><code>math.exp(x)</code> → Exponencial</li>
                    <li><code>math.sqrt(x)</code> → Raíz cuadrada</li>
                </ul>
            </div>
        </div>
    </div>

    <!-- Acordeón Item 3: Paréntesis -->
    <div class="accordion-item" style="background:#232d3e; color:#fff; border:1.5px solid #343a40;">
        <h2 class="accordion-header">
            <button class="accordion-button collapsed"
                    style="background:#232d3e; color:#ffd54f;"
                    type="button" data-bs-toggle="collapse" data-bs-target="#collapse-parentesis">
                Uso de Paréntesis
            </button>
        </h2>
        <div id="collapse-parentesis" class="accordion-collapse collapse" data-bs-parent="#helpAccordion">
            <div class="accordion-body" style="background:#262a32; color:#fff;">
                <h6 style="color:#87ea97;"> CORRECTO:</h6>
                <ul>
                    <li><code>(x + 2) / (x - 1)</code></li>
                    <li><code>math.sin(x + 1)</code></li>
                </ul>
                <h6 style="color:#ffd54f;"> INCORRECTO:</h6>
                <ul>
                    <li><code>x + 2 / x - 1</code></li>
                    <li><code>2x + 5</code> (falta *)</li>
                </ul>
            </div>
        </div>
    </div>
        
        <div class="accordion-item bg-info">
            <h2 class="accordion-header">
                <button class="accordion-button collapsed bg-info text-dark fw-bold" type="button" data-bs-toggle="collapse" data-bs-target="#collapse-parametros">
                     Parámetros de Secante
                </button>
            </h2>
            <div id="collapse-parametros" class="accordion-collapse collapse" data-bs-parent="#helpAccordion">
                <div class="accordion-body bg-dark text-white">
                    <h6>1. FUNCIÓN f(x):</h6>
                    <p><code>x**3 - 2*x - 5</code></p>
                    
                    <h6 class="mt-3">2. VALORES INICIALES:</h6>
                    <p>x₀ = <code>1</code>, x₁ = <code>2</code></p>
                    <p class="text-info">No requieren cambio de signo</p>
                    
                    <h6 class="mt-3">3. TOLERANCIA:</h6>
                    <p><code>5e-5</code></p>
                </div>
            </div>
        </div>
    ''',
    
    'punto_fijo': '''
        <h4 style="color:#ffc107;" class="mb-3">GUÍA PARA INGRESAR LOS PARÁMETROS</h4>
    <!-- Acordeón Item 1: Operadores -->
    <div class="accordion-item" style="background:#232d3e; color:#fff; border:1.5px solid #343a40;">
        <h2 class="accordion-header">
            <button class="accordion-button collapsed"
                    style="background:#232d3e; color:#ffd54f; font-weight:bold;"
                    type="button" data-bs-toggle="collapse" data-bs-target="#collapse-operadores">
                 Operadores Matemáticos
            </button>
        </h2>
        <div id="collapse-operadores" class="accordion-collapse collapse" data-bs-parent="#helpAccordion">
            <div class="accordion-body" style="background:#262a32; color:#fff;">
                <table class="table table-dark table-sm" style="border-radius:7px;overflow:hidden;">
                    <thead>
                        <tr><th>Operación</th><th>Símbolo</th><th>Ejemplo</th></tr>
                    </thead>
                    <tbody>
                        <tr><td>Suma</td><td><code>+</code></td><td><code>x + 5</code></td></tr>
                        <tr><td>Resta</td><td><code>-</code></td><td><code>x - 3</code></td></tr>
                        <tr><td>Multiplicación</td><td><code>*</code></td><td><code>3*x</code></td></tr>
                        <tr><td>División</td><td><code>/</code></td><td><code>x/2</code></td></tr>
                        <tr><td>Potencia</td><td><code>**</code></td><td><code>x**2</code>, <code>x**3</code></td></tr>
                    </tbody>
                </table>
            </div>
        </div>
    </div>

    <!-- Acordeón Item 2: Funciones -->
    <div class="accordion-item" style="background:#232d3e; color:#fff; border:1.5px solid #343a40;">
        <h2 class="accordion-header">
            <button class="accordion-button collapsed"
                    style="background:#232d3e; color:#ffd54f;"
                    type="button" data-bs-toggle="collapse" data-bs-target="#collapse-funciones">
                 Funciones Matemáticas
            </button>
        </h2>
        <div id="collapse-funciones" class="accordion-collapse collapse" data-bs-parent="#helpAccordion">
            <div class="accordion-body" style="background:#262a32; color:#fff;">
                <ul>
                    <li><code>math.sin(x)</code> → Seno</li>
                    <li><code>math.cos(x)</code> → Coseno</li>
                    <li><code>math.tan(x)</code> → Tangente</li>
                    <li><code>math.log(x)</code> → Logaritmo natural</li>
                    <li><code>math.log10(x)</code> → Log base 10</li>
                    <li><code>math.exp(x)</code> → Exponencial</li>
                    <li><code>math.sqrt(x)</code> → Raíz cuadrada</li>
                </ul>
            </div>
        </div>
    </div>

    <!-- Acordeón Item 3: Paréntesis -->
    <div class="accordion-item" style="background:#232d3e; color:#fff; border:1.5px solid #343a40;">
        <h2 class="accordion-header">
            <button class="accordion-button collapsed"
                    style="background:#232d3e; color:#ffd54f;"
                    type="button" data-bs-toggle="collapse" data-bs-target="#collapse-parentesis">
                Uso de Paréntesis
            </button>
        </h2>
        <div id="collapse-parentesis" class="accordion-collapse collapse" data-bs-parent="#helpAccordion">
            <div class="accordion-body" style="background:#262a32; color:#fff;">
                <h6 style="color:#87ea97;"> CORRECTO:</h6>
                <ul>
                    <li><code>(x + 2) / (x - 1)</code></li>
                    <li><code>math.sin(x + 1)</code></li>
                </ul>
                <h6 style="color:#ffd54f;"> INCORRECTO:</h6>
                <ul>
                    <li><code>x + 2 / x - 1</code></li>
                    <li><code>2x + 5</code> (falta *)</li>
                </ul>
            </div>
        </div>
    </div>
        
        <div class="accordion-item bg-info">
            <h2 class="accordion-header">
                <button class="accordion-button collapsed bg-info text-dark fw-bold" type="button" data-bs-toggle="collapse" data-bs-target="#collapse-parametros">
                     Parámetros de Punto Fijo
                </button>
            </h2>
            <div id="collapse-parametros" class="accordion-collapse collapse" data-bs-parent="#helpAccordion">
                <div class="accordion-body bg-dark text-white">
                    <h6>1. FUNCIÓN g(x):</h6>
                    <p>Debe ser reformulación de f(x) = 0 como x = g(x)</p>
                    <p><strong>Ejemplo:</strong> Si f(x) = x² - 4 → g(x) = <code>4/x</code></p>
                    
                    <h6 class="mt-3">2. VALOR INICIAL x₀:</h6>
                    <p><code>1.5</code></p>
                    
                    <h6 class="mt-3">3. TOLERANCIA:</h6>
                    <p><code>5e-5</code></p>
                    
                    <p class="text-warning mt-3"><strong></strong> Debe cumplir |g'(x)| &lt; 1</p>
                </div>
            </div>
        </div>
    ''',
    
    'multiple_roots': '''
        <h4 style="color:#ffc107;" class="mb-3">GUÍA PARA INGRESAR LOS PARÁMETROS</h4>
    <!-- Acordeón Item 1: Operadores -->
    <div class="accordion-item" style="background:#232d3e; color:#fff; border:1.5px solid #343a40;">
        <h2 class="accordion-header">
            <button class="accordion-button collapsed"
                    style="background:#232d3e; color:#ffd54f; font-weight:bold;"
                    type="button" data-bs-toggle="collapse" data-bs-target="#collapse-operadores">
                 Operadores Matemáticos
            </button>
        </h2>
        <div id="collapse-operadores" class="accordion-collapse collapse" data-bs-parent="#helpAccordion">
            <div class="accordion-body" style="background:#262a32; color:#fff;">
                <table class="table table-dark table-sm" style="border-radius:7px;overflow:hidden;">
                    <thead>
                        <tr><th>Operación</th><th>Símbolo</th><th>Ejemplo</th></tr>
                    </thead>
                    <tbody>
                        <tr><td>Suma</td><td><code>+</code></td><td><code>x + 5</code></td></tr>
                        <tr><td>Resta</td><td><code>-</code></td><td><code>x - 3</code></td></tr>
                        <tr><td>Multiplicación</td><td><code>*</code></td><td><code>3*x</code></td></tr>
                        <tr><td>División</td><td><code>/</code></td><td><code>x/2</code></td></tr>
                        <tr><td>Potencia</td><td><code>**</code></td><td><code>x**2</code>, <code>x**3</code></td></tr>
                    </tbody>
                </table>
            </div>
        </div>
    </div>

    <!-- Acordeón Item 2: Funciones -->
    <div class="accordion-item" style="background:#232d3e; color:#fff; border:1.5px solid #343a40;">
        <h2 class="accordion-header">
            <button class="accordion-button collapsed"
                    style="background:#232d3e; color:#ffd54f;"
                    type="button" data-bs-toggle="collapse" data-bs-target="#collapse-funciones">
                 Funciones Matemáticas
            </button>
        </h2>
        <div id="collapse-funciones" class="accordion-collapse collapse" data-bs-parent="#helpAccordion">
            <div class="accordion-body" style="background:#262a32; color:#fff;">
                <ul>
                    <li><code>math.sin(x)</code> → Seno</li>
                    <li><code>math.cos(x)</code> → Coseno</li>
                    <li><code>math.tan(x)</code> → Tangente</li>
                    <li><code>math.log(x)</code> → Logaritmo natural</li>
                    <li><code>math.log10(x)</code> → Log base 10</li>
                    <li><code>math.exp(x)</code> → Exponencial</li>
                    <li><code>math.sqrt(x)</code> → Raíz cuadrada</li>
                </ul>
            </div>
        </div>
    </div>

    <!-- Acordeón Item 3: Paréntesis -->
    <div class="accordion-item" style="background:#232d3e; color:#fff; border:1.5px solid #343a40;">
        <h2 class="accordion-header">
            <button class="accordion-button collapsed"
                    style="background:#232d3e; color:#ffd54f;"
                    type="button" data-bs-toggle="collapse" data-bs-target="#collapse-parentesis">
                Uso de Paréntesis
            </button>
        </h2>
        <div id="collapse-parentesis" class="accordion-collapse collapse" data-bs-parent="#helpAccordion">
            <div class="accordion-body" style="background:#262a32; color:#fff;">
                <h6 style="color:#87ea97;"> CORRECTO:</h6>
                <ul>
                    <li><code>(x + 2) / (x - 1)</code></li>
                    <li><code>math.sin(x + 1)</code></li>
                </ul>
                <h6 style="color:#ffd54f;"> INCORRECTO:</h6>
                <ul>
                    <li><code>x + 2 / x - 1</code></li>
                    <li><code>2x + 5</code> (falta *)</li>
                </ul>
            </div>
        </div>
    </div>
        
        <div class="accordion-item bg-info">
            <h2 class="accordion-header">
                <button class="accordion-button collapsed bg-info text-dark fw-bold" type="button" data-bs-toggle="collapse" data-bs-target="#collapse-parametros">
                     Parámetros de Raíces Múltiples
                </button>
            </h2>
            <div id="collapse-parametros" class="accordion-collapse collapse" data-bs-parent="#helpAccordion">
                <div class="accordion-body bg-dark text-white">
                    <h6>1. FUNCIÓN f(x):</h6>
                    <p><strong>Ejemplo raíz triple:</strong> <code>(x - 2)**3</code></p>
                    
                    <h6 class="mt-3">2. DERIVADAS:</h6>
                    <p>Usa los botones automáticos:</p>
                    <ul>
                        <li><span class="badge bg-warning"> Calcular f'(x)</span></li>
                        <li><span class="badge bg-info"> Calcular f''(x)</span></li>
                    </ul>
                    
                    <h6 class="mt-3">3. VALOR INICIAL x₀:</h6>
                    <p><code>1</code></p>
                    
                    <h6 class="mt-3">4. TOLERANCIA:</h6>
                    <p><code>5e-5</code></p>
                </div>
            </div>
        </div>
    ''',
    
    # ==========================================
    # CAPÍTULO 2
    # ==========================================


'jacobi': '''
    <h4 style="color:#ffc107;">GUÍA PARA INGRESAR LOS PARÁMETROS</h4>
    <div class="card mb-3" style="background: #232d3e; color: #fff; border: 1.5px solid #343a40;">
        <div class="card-header" style="background: rgba(255,193,7,0.13); color: #ffd54f; font-weight: bold; border-bottom: 1px solid #282828;">
            PARÁMETROS PARA SISTEMAS LINEALES
        </div>
        <div class="card-body" style="color:#e5e5e5;">
            <b>TAMAÑO DE LA MATRIZ:</b>
            <p>Selecciona de 2x2 hasta 7x7</p>
            <b>MATRIZ A (COEFICIENTES):</b>
            <p>Separa columnas con espacios y filas con saltos de línea</p>
            <pre style="background:#282c34; color:#ffd54f; padding:7px 12px; border-radius:7px;">4 -1 0
-1 4 -1
0 -1 4</pre>
            <b>VECTOR B:</b>
            <span class="badge" style="background: #383f51; color: #ffc107; margin-left:8px;">15 10 10</span>
            <br><b>VECTOR INICIAL x₀:</b>
            <span class="badge" style="background: #383f51; color:#ffc107; margin-left:8px;">0 0 0</span>
            <br><b>TOLERANCIA:</b>
            <code style="color:#ffd54f; background:#212121; padding:2px 6px; border-radius:5px;">5e-5</code>
            <div style="margin-top:1em;color:#ffc107;"><b> La matriz debe ser diagonalmente dominante para garantizar convergencia</b></div>
        </div>
    </div>
''',

'gauss_seidel': '''
    <h4 style="color:#ffc107;">GUÍA PARA INGRESAR LOS PARÁMETROS</h4>
    <div class="card mb-3" style="background: #232d3e; color: #fff; border: 1.5px solid #343a40;">
        <div class="card-header" style="background: rgba(255,193,7,0.13); color: #ffd54f; font-weight: bold; border-bottom: 1px solid #282828;">
            PARÁMETROS (IGUAL QUE JACOBI)
        </div>
        <div class="card-body" style="color:#e5e5e5;">
            <b>MATRIZ A:</b>
            <pre style="background:#282c34; color:#ffd54f; padding:7px 12px; border-radius:7px;">4 -1 0
-1 4 -1
0 -1 4</pre>
            <b>VECTOR B:</b><span class="badge" style="background: #383f51; color: #ffc107; margin-left:8px;">15 10 10</span>
            <br><b>VECTOR x₀:</b><span class="badge" style="background: #383f51; color: #ffc107; margin-left:8px;">0 0 0</span>
            <br><b>TOLERANCIA:</b><code style="color:#ffd54f; background:#212121; padding:2px 6px; border-radius:5px;">5e-5</code>
            <div style="margin-top:1em;color:#03e37d;"><b> Converge ~2x más rápido que Jacobi</b></div>
        </div>
    </div>
''',

'sor': '''
    <h4 style="color:#ffc107;">GUÍA PARA INGRESAR LOS PARÁMETROS</h4>
    <div class="card mb-3" style="background: #232d3e; color: #fff; border: 1.5px solid #343a40;">
        <div class="card-header" style="background: rgba(255,193,7,0.13); color: #ffd54f; font-weight: bold; border-bottom: 1px solid #282828;">
            PARÁMETROS DE SOR (Sobre-Relajación)
        </div>
        <div class="card-body" style="color:#e5e5e5;">
            <b>Todos los anteriores +</b>
            <br><b>FACTOR DE RELAJACIÓN ω (OMEGA):</b>
            <span style="color:#ffd54f">Debe estar entre 1 y 2</span>
            <div class="mt-1" style="font-size:0.97em;color:#bbb">
                Valores recomendados: 1.2, 1.25, 1.5
            </div>
            <div class="alert" style="margin-top:12px; color:#ffc107; background:rgba(255,193,7,0.14); border:none;">
                <ul style="margin-bottom:0px; padding-left:17px;">
                    <li>ω = 1 → Gauss-Seidel normal</li>
                    <li>1 &lt; ω &lt; 2 → Más rápido</li>
                    <li>ω ≥ 2 → Puede diverger</li>
                </ul>
            </div>
            <b>Ejemplo x₀:</b>
            <span class="badge" style="background: #383f51; color: #ffc107; margin-left:8px;">0 0 0</span>
            <br><b>TOLERANCIA:</b>
            <code style="color:#ffd54f; background:#212121; padding:2px 6px; border-radius:5px;">5e-5</code>
        </div>
    </div>
''',
    # ==========================================
    # CAPÍTULO 3
    # ==========================================

'lagrange': '''
    <h4 style="color:#ffc107;">GUÍA PARA INGRESAR LOS PARÁMETROS</h4>
    <div class="card mb-3" style="background: #232d3e; color: #fff; border: 1.5px solid #343a40;">
        <div class="card-header" style="background: rgba(255,193,7,0.13); color: #ffd54f; font-weight: bold; border-bottom: 1px solid #282828;">
            PUNTOS (X, Y)
        </div>
        <div class="card-body" style="color:#e5e5e5;">
            <b>VALORES X:</b> <span class="badge" style="background: #383f51; color: #ffc107; margin-left:8px;">1 2 3 4 5</span>
            <br><b>VALORES Y:</b> <span class="badge" style="background: #383f51; color: #ffc107; margin-left:8px;">6 7 8 9 10</span>
            <div style="margin-top:7px;color:#ffc107;"><b>RECUERDA:</b> Mismo tamaño de X e Y</div>
        </div>
    </div>
''',

'newton_interpol': '''
    <h4 style="color:#ffc107;">GUÍA PARA INGRESAR LOS PARÁMETROS</h4>
    <div class="card mb-3" style="background: #232d3e; color: #fff; border: 1.5px solid #343a40;">
        <div class="card-header" style="background: rgba(255,193,7,0.13); color: #ffd54f; font-weight: bold; border-bottom: 1px solid #282828;">
            PUNTOS PARA NEWTON
        </div>
        <div class="card-body" style="color:#e5e5e5;">
            <b>VALORES X:</b> <span class="badge" style="background: #383f51; color: #ffc107; margin-left:8px;">0 1 2 3</span>
            <br><b>VALORES Y:</b> <span class="badge" style="background: #383f51; color: #ffc107; margin-left:8px;">0 1 4 9</span>
            <div class="mt-2" style="color:#87ea97;"><b> Fácil agregar puntos nuevos</b></div>
        </div>
    </div>
''',

'vandermonde': '''
    <h4 style="color:#ffc107;">GUÍA PARA INGRESAR LOS PARÁMETROS</h4>
    <div class="card mb-3" style="background: #232d3e; color:#fff;border: 1.5px solid #343a40;">
        <div class="card-header" style="background: rgba(255,193,7,0.13); color: #ffd54f; font-weight: bold; border-bottom: 1px solid #282828;">
            PUNTOS PARA VANDERMONDE
        </div>
        <div class="card-body" style="color:#e5e5e5;">
            <b>VALORES X:</b> <span class="badge" style="background:#383f51; color: #ffc107; margin-left:8px;">0 1 2</span>
            <br><b>VALORES Y:</b> <span class="badge" style="background:#383f51; color: #ffc107; margin-left:8px;">0 1 4</span>
            <div style="margin-top:10px; color:#ffc107;">
                 Evitar más de 8 puntos
            </div>
        </div>
    </div>
''',

'spline_linear': '''
    <h4 style="color:#ffc107;">GUÍA PARA INGRESAR LOS PARÁMETROS</h4>
    <div class="card mb-3" style="background: #232d3e; color: #fff; border: 1.5px solid #343a40;">
        <div class="card-header" style="background: rgba(255,193,7,0.13); color: #ffd54f; font-weight: bold; border-bottom: 1px solid #282828;">
            PUNTOS PARA SPLINE LINEAL
        </div>
        <div class="card-body" style="color:#e5e5e5;">
            <b>VALORES X:</b> <span class="badge" style="background: #383f51; color: #ffc107; margin-left:8px;">0 1 2 3 4</span>
            <br><b>VALORES Y:</b> <span class="badge" style="background: #383f51; color: #ffc107; margin-left:8px;">0 1 4 9 16</span>
            <div class="mt-2" style="color:#87ea97;"><b> Conecta con líneas rectas</b></div>
        </div>
    </div>
''',

'spline_cubic': '''
    <h4 style="color:#ffc107;">GUÍA PARA INGRESAR LOS PARÁMETROS</h4>
    <div class="card mb-3" style="background: #232d3e; color: #fff; border: 1.5px solid #343a40;">
        <div class="card-header" style="background: rgba(255,193,7,0.13); color: #ffd54f; font-weight: bold; border-bottom: 1px solid #282828;">
            PUNTOS PARA SPLINE CÚBICO
        </div>
        <div class="card-body" style="color:#e5e5e5;">
            <b>VALORES X:</b> <span class="badge" style="background: #383f51; color: #ffc107; margin-left:8px;">0 1 2 3 4</span>
            <br><b>VALORES Y:</b> <span class="badge" style="background: #383f51; color: #ffc107; margin-left:8px;">0 1 4 9 16</span>
            <div class="mt-2" style="color:#87ea97;"><b> Curva muy suave (C² continuo)</b></div>
        </div>
    </div>
''',
}
