import pytest
from Recursao.meus_exercicios import encontra_impar_2

class TestaImpar:
    @pytest.mark.parametrize('entrada, esperado', [([1, 2, 3, 4, 5],[1, 3, 5]),
                                                   ([1],[1]),
                                                   ([2],[]),
                                                   ([4, 4],[]),
                                                   ([3, 7],[3, 7])
                                                   ])
    def test_impar(self, entrada, esperado):
        assert encontra_impar_2.encontra_impares(entrada) == esperado