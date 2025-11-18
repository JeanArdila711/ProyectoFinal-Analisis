from django.urls import path
from numerical.views import views
from numerical.views.newton_interpol_view import NewtonInterpolView
from numerical.views.bisection_view import BisectionView
from numerical.views.regula_falsi_view import RegulaFalsiView
from numerical.views.secant_view import SecantView
from numerical.views.newton_raphson_view import NewtonRaphsonView
from numerical.views.fixed_point_view import FixedPointView
from numerical.views.multiple_roots_2_view import MultipleRoots2View
from numerical.views.jacobi_view import JacobiView
from numerical.views.gauss_seidel_view import GaussSeidelView
from numerical.views.sor_view import SORView
from numerical.views.lagrange_view import LagrangeView
from numerical.views.spline_linear_view import SplineLinearView
from numerical.views.spline_cubic_view import SplineCubicView
from numerical.views.vandermonde_view import VandermondeView
from numerical.views.comparison_view import ComparisonView
from numerical.views.comparison_view2 import ComparisonLinearView
from numerical.views.comparison3_view import ComparisonViewInterpol
from numerical.views.file_download_view import FileDownloadView





urlpatterns = [
    # Índices de capítulos
    path('cap1/', views.chapter1_index, name='chapter1'),
    path('cap2/', views.chapter2_index, name='chapter2'),
    path('cap3/', views.chapter3_index, name='chapter3'),
    
    # Métodos Capítulo 1
    path('cap1/bisection/', BisectionView.as_view(), name='bisection'),
    path('cap1/regula-falsi/', RegulaFalsiView.as_view(), name='regula_falsi'),
    path('cap1/secant/', SecantView.as_view(), name='secant'),
    path('cap1/multiple-roots/', MultipleRoots2View.as_view(), name='multiple_roots'),
    path('cap1/fixed-point/', FixedPointView.as_view(), name='fixed_point'),
    path('cap1/newton-raphson/', NewtonRaphsonView.as_view(), name='newton_raphson'),
    path('cap1/comparison/', ComparisonView.as_view(), name='comparison'),
    
    # Métodos Capítulo 2
    path('cap2/jacobi/', JacobiView.as_view(), name='jacobi'),
    path('cap2/gauss-seidel/', GaussSeidelView.as_view(), name='gauss_seidel'),
    path('cap2/sor/', SORView.as_view(), name='sor'),
    path('cap2/comparison/', ComparisonLinearView.as_view(), name='comparison_linear'),
    
    # Métodos Capítulo 3
    path('cap3/lagrange/', LagrangeView.as_view(), name='lagrange'),
    path('cap3/newton-interpol/', NewtonInterpolView.as_view(), name='newton_interpol'),
    path('cap3/spline-linear/', SplineLinearView.as_view(), name='spline_linear'),
    path('cap3/spline-cubic/', SplineCubicView.as_view(), name='spline_cubic'),
    path('cap3/vandermonde/', VandermondeView.as_view(), name='vandermonde'),
    path('cap3/comparison/', ComparisonViewInterpol.as_view(), name='comparison_interpol'),
    
    # Descarga de archivos
    path('download/<str:filename>/', FileDownloadView.as_view(), name='download_file'),
]
