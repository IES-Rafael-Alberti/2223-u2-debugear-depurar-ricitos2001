import pytest
from src.actividad1 import argoritmo_burbuja
@pytest.mark.parametrize(
    "lista",
    [
        (0, 1, 2, 3, 4, 5)
    ]
)
def test_argoritmo_burbuja_params(lista):
    assert argoritmo_burbuja(lista)==0, 1