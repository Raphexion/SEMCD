from rules import rule1
import unittest


class TestRule1(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_dont_handle(self):
        S, E, M, C, D = range(5)
        try:
            rule1(S, E, C, M, D)
            self.fail()
        except ValueError:
            pass

    def test_handle(self):
        S, E, M = object(), object(), object()
        C = None
        Ep, Cp, Dp = object(), object(), object()
        D = (Ep, Cp, Dp)

        (Sr, Er, Mr, Cr, Dr) = rule1(S, E, M, C, D)

        self.assertIs(Sr, S)
        self.assertIs(Er, Ep)
        self.assertIs(Mr, M)
        self.assertIs(Cr, Cp)
        self.assertIs(Dr, Dp)
