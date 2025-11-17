from django.shortcuts import render
from django.views.generic import TemplateView


# --- Página principal del módulo numérico ---
def index(request):
    return render(request, 'home/index.html')


# --- Capítulo 1 - Página Índice ---
def chapter1_index(request):
    return render(request, 'numerical/cap1/index.html')


# --- Métodos Capítulo 1 ---
def bisection(request):
    return render(request, 'numerical/cap1/bisection.html')

def regula_falsi(request):
    return render(request, 'numerical/cap1/regula_falsi.html')

def secant(request):
    return render(request, 'numerical/cap1/secant.html')

def multiple_roots(request):
    return render(request, 'numerical/cap1/multiple_roots.html')

def fixed_point(request):
    return render(request, 'numerical/cap1/fixed_point.html')

def newton_raphson(request):
    return render(request, 'numerical/cap1/newton_raphson.html')


# --- Capítulo 2 - Página Índice ---
def chapter2_index(request):
    return render(request, 'numerical/cap2/index.html')

# --- Métodos Capítulo 2 ---
def jacobi(request):
    return render(request, 'numerical/cap2/jacobi.html')

def gauss_seidel(request):
    return render(request, 'numerical/cap2/gauss_seidel.html')

def sor(request):
    return render(request, 'numerical/cap2/sor.html')


# --- Capítulo 3 - Página Índice ---
def chapter3_index(request):
    return render(request, 'numerical/cap3/index.html')

# --- Métodos Capítulo 3 ---
def lagrange(request):
    return render(request, 'numerical/cap3/lagrange.html')

def newton_interpol(request):
    return render(request, 'numerical/cap3/newton_interpol.html')

def spline_linear(request):
    return render(request, 'numerical/cap3/spline_linear.html')

def spline_cubic(request):
    return render(request, 'numerical/cap3/spline_cubic.html')

def vandermonde(request):
    return render(request, 'numerical/cap3/vandermonde.html')
