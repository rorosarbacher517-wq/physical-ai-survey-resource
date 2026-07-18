from __future__ import annotations

from examples.operator_learning_toy import main as operator_main
from examples.physics_constrained_series import main as series_main
from examples.pinn_toy import main as pinn_main

def test_pinn_residual_zero() -> None:
    assert pinn_main() == 0.0

def test_operator_toy() -> None:
    assert operator_main() == [0.0, 2.0, 4.0]

def test_conservation_toy() -> None:
    assert abs(series_main()) < 1e-12
