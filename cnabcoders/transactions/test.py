import re
import unittest
from datetime import datetime

line = '5201903010000013200556418150633123****7687145607MARIA JOSEFINALOJA DO Ó - MATRIZ'
line_error_data = '52019ma010000013200556418150633123****7687145607MARIA JOSEFINALOJA DO Ó - MATRIZ'
line_error_type = 'a201903010000013200556418150633123****7687145607MARIA JOSEFINALOJA DO Ó - MATRIZ'
line_error_card = '52019ma010000013200556418150633123****a687145607MARIA JOSEFINALOJA DO Ó - MATRIZ'

class CardCase(unittest.TestCase):
    def test_type(self):
        match = re.fullmatch(r'[0-9]', line[0])
        self.assertEqual(match.group(0),  '5')

    def test_datetime(self):
        assert (datetime.strptime(line[1:9] + ' ' + line[42:48], '%Y%m%d %H%M%S'))

    def test_card_isvalid(self):
        match = re.fullmatch(r'[0-9][0-9][0-9][0-9]\*\*\*\*[0-9][0-9][0-9][0-9]', line[30:42])
        self.assertEqual(match.group(0),  '3123****7687')

    def test_cpf(self):
        assert re.fullmatch(r'[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]', line[19:30])

if __name__ == '__main__':
    unittest.main()