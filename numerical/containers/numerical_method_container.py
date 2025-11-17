from dependency_injector import containers, providers
from numerical.services.bisection_service import BisectionService
from numerical.services.regula_falsi_service import (
    RegulaFalsiService,
)
from numerical.services.fixed_point_service import (
    FixedPointService,
)
from numerical.services.newton_raphson_service import (
    NewtonService,
)
from numerical.services.secant_service import (
    SecantService,
)
from numerical.services.multiple_roots_1_service import (
    MultipleRoots1Service,
)
from numerical.services.multiple_roots_2_service import (
    MultipleRoots2Service,
)
from numerical.services.jacobi_service import JacobiService

from numerical.services.gauss_seidel_service import (
    GaussSeidelService,
)
from numerical.services.sor_service import (
    SORService,
)
from numerical.services.vandermonde_service import (
    VandermondeService,
)
from numerical.services.spline_linear_service import (
    SplineLinearService,
)
from numerical.services.spline_cubic_service import (
    SplineCubicService,
)
from numerical.services.lagrange_service import (
  LagrangeService,
)
from numerical.services.newton_interpol_service import (
  NewtonInterpolService,
)
from numerical.services.comparison_service import (
    ComparisonService,
)
from numerical.services.comparison_service2 import (
    ComparisonService as ComparisonLinearService,
)
from numerical.services.comparison3_service import (
    Comparison3Service,
)


class NumericalMethodContainer(containers.DeclarativeContainer):
    bisection_service = providers.Factory(BisectionService)
    regula_falsi_service = providers.Factory(RegulaFalsiService)
    fixed_point_service = providers.Factory(FixedPointService)
    newton_service = providers.Factory(NewtonService)
    secant_service = providers.Factory(SecantService)
    multiple_roots_1_service = providers.Factory(MultipleRoots1Service)
    multiple_roots_2_service = providers.Factory(MultipleRoots2Service)
    jacobi_service = providers.Factory(JacobiService)
    gauss_seidel_service = providers.Factory(GaussSeidelService)
    sor_service = providers.Factory(SORService)
    vandermonde_service = providers.Factory(VandermondeService)
    spline_linear_service = providers.Factory(SplineLinearService)
    spline_cubic_service = providers.Factory(SplineCubicService)
    lagrange_service = providers.Factory(LagrangeService)
    newton_interpol_service = providers.Factory(NewtonInterpolService)
    comparison_service = providers.Factory(ComparisonService)
    comparison_linear_service = providers.Factory(ComparisonLinearService)
    comparison3_service = providers.Factory(Comparison3Service)