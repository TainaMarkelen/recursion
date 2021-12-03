import pytest
from Recursao.meus_exercicios import soma_2

class TestSoma:
    @pytest.mark.parametrize('entrada, esperado', [([2, 3, 10], 15),
                                                    ([5, 60, 2], 67),
                                                    ([9], 9),
                                                    ([20, 10], 30)])
    def test_soma_recurs(self, entrada, esperado):
        assert soma_2.soma_lista(entrada) == esperado
        
                                                    
                                                    
