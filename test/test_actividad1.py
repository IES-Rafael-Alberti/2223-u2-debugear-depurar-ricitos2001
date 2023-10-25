import pytest
from src.actividad1 import argoritmo_burbuja
@pytest.mark.parametrize(
    "listafinal",
    [
        (0, 1, 2, 3, 4, 5)
    ]
)
def test_argoritmo_burbuja_params(listafinal):
    assert argoritmo_burbuja(listafinal)==0, 1