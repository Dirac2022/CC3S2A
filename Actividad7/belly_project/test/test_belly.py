import pytest
import sys
import os
# Importaremos la clase belly.py que se encuentra en la carpeta src
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from belly import Belly

def test_belly_comer_pepinos_fraccionarios():
    """Test para verificar que se pueden comer pepinos en fracciones.
    """
    belly = Belly()
    belly.comer(2.5)
    assert belly.pepinos_comidos == 2.5

def test_belly_comer_pepinos_negativos():
    """Test para verificar que se lanza una excepción al intentar comer una
    cantidad negativa de pepinos.
    """
    belly = Belly()
    with pytest.raises(ValueError) as error:
        belly.comer(-2)
    assert str(error.value) == "La cantidad ingresada (negativa) no es válida."