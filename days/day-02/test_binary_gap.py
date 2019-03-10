from unittest import TestCase

from binary_gap import get_binary_gap


class TestBinaryGap(TestCase):
    def test_gap_recebe_valor_diferente_de_int(self):
        self.assertEqual(404, get_binary_gap("valor"))
        self.assertEqual(404, get_binary_gap([1]))
        self.assertEqual(404, get_binary_gap({1: 1}))

    def test_gap_retornando_um_inteiro(self):
        self.assertIs(int, type(get_binary_gap(1)))

    def test_gap_recebe_1_retorna_0(self):
        self.assertEqual(0, get_binary_gap(1))

    def test_gap_recebe_10_retorna_1(self):
        self.assertEqual(1, get_binary_gap(10))

    def test_gap_recebe_11_retorna_1(self):
        self.assertEqual(1, get_binary_gap(11))

    def test_gap_recebe_32_retorna_0(self):
        self.assertEqual(0, get_binary_gap(32))

    def test_gap_recebe_20_retorna_1(self):
        self.assertEqual(1, get_binary_gap(20))

    def test_gap_recebe_529_retorna_4(self):
        self.assertEqual(4, get_binary_gap(529))

    def test_gap_recebe_15_retorna_0(self):
        self.assertEqual(0, get_binary_gap(15))

    def test_gap_recebe_1041_retorna_5(self):
        self.assertEqual(5, get_binary_gap(1041))