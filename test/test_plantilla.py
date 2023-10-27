import pytest
from src.plantilla import crear_funcion
@pytest.mark.parametrize(
    #valores
    "funcion1, funcion2, funcion3",
    [
        #lo que queremos escribir
        (1,1,"la funcion es: 2")
    ]  
)
#valores
def test_crear_funcion_params(funcion1,funcion2,funcion3):
    #la funcion de procesamiento y el valor que devuelve
    assert crear_funcion(funcion1,funcion2) == funcion3