import unittest
from SymbolInput import SymbolInput
from ChartTypeInput import ChartTypeInput
from TimeSeriesInput import TimeSeriesInput
from startDateInput import StartDateInput
from EndDateInput import EndDateInput

class TestInputs(unittest.TestCase):

    def test_symbolInput(self):
        si = SymbolInput()
        self.assertTrue(si.isInputValid("GOOGL"))
        self.assertFalse(si.isInputValid("1"))
        self.assertFalse(si.isInputValid(""))
        self.assertFalse(si.isInputValid("googl1"))

    def test_chart_type(self):
        cti = ChartTypeInput()
        self.assertTrue(cti.isInputValid('1'), "Value 1 should be valid")
        self.assertTrue(cti.isInputValid('2'), "Value 2 should be valid")
        self.assertFalse(cti.isInputValid('4'), "Value 4 should be invalid")
        self.assertFalse(cti.isInputValid('-8'), "Value -8 should be invalid")
        self.assertFalse(cti.isInputValid('-18'), "Value -18 should be invalid")
        self.assertFalse(cti.isInputValid('a'), "Value 'a' should be invalid")
        self.assertFalse(cti.isInputValid(' '), "Whitespace should be invalid")
        self.assertFalse(cti.isInputValid(''), "Empty string should be invalid")

    def test_timeSeries_input(self):
        tsi = TimeSeriesInput()
        self.assertTrue(tsi.isInputValid('1'), "Value 1 should be valid")
        self.assertTrue(tsi.isInputValid('2'), "Value 2 should be valid")
        self.assertTrue(tsi.isInputValid('3'), "Value 3 should be valid")
        self.assertTrue(tsi.isInputValid('4'), "Value 4 should be valid")
        self.assertFalse(tsi.isInputValid('0'), "Value 0 should be invalid")
        self.assertFalse(tsi.isInputValid('-3'), "Value -3 should be invalid")
        self.assertFalse(tsi.isInputValid('16'), "Value 16 should be invalid")
        self.assertFalse(tsi.isInputValid('2.5'), "Value 2.5 should be invalid")
        self.assertFalse(tsi.isInputValid(''), "User must enter an input")
        self.assertFalse(tsi.isInputValid(' '), "User must enter an input")

    def test_startDate_input(self):
        sdi = StartDateInput()
        self.assertTrue(sdi.isInputValid("1999-01-15"))
        self.assertTrue(sdi.isInputValid("1980-12-12"))
        self.assertFalse(sdi.isInputValid("1999/01/15"))
        self.assertFalse(sdi.isInputValid("08/12/2006"))
        self.assertFalse(sdi.isInputValid("2001-09-56"))
        self.assertFalse(sdi.isInputValid("2001-13-31"))
        self.assertFalse(sdi.isInputValid("March 10, 2001"))

    def test_endDate_input(self):
        sdi = StartDateInput()
        sdi.value = "1960-01-31"
        edi = EndDateInput(sdi)
        self.assertTrue(edi.isInputValid("1999-01-15"))
        self.assertTrue(edi.isInputValid("1980-12-12"))
        self.assertFalse(edi.isInputValid("1999/01/15"))
        self.assertFalse(edi.isInputValid("08/12/2006"))
        self.assertFalse(edi.isInputValid("2001-09-56"))
        self.assertFalse(edi.isInputValid("2001-13-31"))
        self.assertFalse(edi.isInputValid("March 10, 2001"))
        self.assertFalse(edi.isInputValid("1960-01-30"))
        
if __name__ == "__main__":
    unittest.main()