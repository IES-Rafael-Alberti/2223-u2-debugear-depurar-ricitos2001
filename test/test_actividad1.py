import pytest
from src.actividad1 import argoritmo_burbuja
@pytest.mark.parametrize(
    "lista, listafinal",
    [
        ([5, 3, 1, 2, 4],[1, 2, 3, 4, 5])
    ]
)
def test_argoritmo_burbuja_params(lista,listafinal):
    assert argoritmo_burbuja(lista)==listafinal