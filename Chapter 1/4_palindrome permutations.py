import unittest
from collections import Counter

def pal_perm(string):
    string = Counter(string.lower().replace(" ", ""))
    flag = False
    for value in string.values():
        if value % 2:
            if flag:
                return False
            else:
                flag = True
    return True

class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ('Tact Coa', True),
        ('jhsabckuj ahjsbckj', True),
        ('Able was I ere I saw Elba', True),
        ('So patient a nurse to nurse a patient so', False),
        ('Random Words', False),
        ('Not a Palindrome', False),
        ('no x in nixon', True),
        ('azAZ', True)]

    def test_pal_perm(self):
        for [test_string, expected] in self.data:
            actual = pal_perm(test_string)
            try:
                self.assertEqual(actual, expected)
            except:
                print(test_string, actual)

if __name__ == "__main__":
    unittest.main()