import urllib.request
import unittest

class TestAPIMethods(unittest.TestCase):

    def test1(self):
        try:
            a = urllib.request.urlopen("http://localhost/1").getcode()
            self.assertEqual(a, 200, 'Тест на целое число: запрос не обработан')
        except urllib.error.HTTPError as e:
            self.assertEqual(e, 200, 'Тест на целое число: запрос не обработан')

    def test2(self):
        try:
            a = urllib.request.urlopen("http://localhost/1A").getcode()
            self.assertEqual(a, 200, 'Тест на число с буквой: запрос не обработан')
        except urllib.error.HTTPError as e:
            self.assertEqual(e, 200, 'Тест на число с буквой: запрос не обработан')

    def test3(self):
        try:
            a = urllib.request.urlopen("http://localhost/A").getcode()
            self.assertEqual(a, 200, 'Тест на букву: запрос не обработан')
        except urllib.error.HTTPError as e:
            self.assertEqual(e, 200, 'Тест на букву: запрос не обработан')

    def test4(self):
        try:
            a = urllib.request.urlopen("http://localhost/0").getcode()
            self.assertEqual(a, 200, 'Тест на ноль: запрос не обработан')
        except urllib.error.HTTPError as e:
            self.assertEqual(e, 200, 'Тест на ноль: запрос не обработан')

    def test5(self):
        try:
            a = urllib.request.urlopen("http://localhost/-5").getcode()
            self.assertEqual(a, 200, 'Тест на отрицательное число: запрос не обработан')
        except urllib.error.HTTPError as e:
            self.assertEqual(e, 200, 'Тест на отрицательное число: запрос не обработан')

    def test6(self):
        try:
            a = urllib.request.urlopen("http://localhost/").getcode()
            self.assertEqual(a, 200, 'Тест если значение на введено: запрос не обработан')
        except urllib.error.HTTPError as e:
            self.assertEqual(e, 200, 'Тест если значение на введено: запрос не обработан')

    def test7(self):
        try:
            a = urllib.request.urlopen("http://localhost/1,2").getcode()
            self.assertEqual(a, 200, 'Тест если введена запятая: запрос не обработан')
        except urllib.error.HTTPError as e:
            self.assertEqual(e, 200, 'Тест если введена запятая: запрос не обработан')

    def test8(self):
        try:
            a = urllib.request.urlopen("http://localhost/1.2").getcode()
            self.assertEqual(a, 200, 'Тест если введена точка: запрос не обработан')
        except urllib.error.HTTPError as e:
            self.assertEqual(e, 200, 'Тест если введена точка: запрос не обработан')      

if __name__ == '__main__':
    unittest.main()

