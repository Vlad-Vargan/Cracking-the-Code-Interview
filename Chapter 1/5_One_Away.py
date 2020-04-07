import unittest

def one_away(s1,s2):
    if len(s1) == len(s2):
        return equalLenght(s1,s2)
    elif len(s1)-1 == len(s2):
        return oneLenght(s1,s2)
    elif len(s1)+1 == len(s2):
        return oneLenght(s2,s1)
    else:
        return False

def equalLenght(s1,s2):
    flag = False
    for index in range(len(s1)):
        if s1[index] != s2[index]:
            if flag:
                return False
            else:
                flag = True
    return True

def oneLenght(s1,s2):
    p1, p2 = 0, 0
    flag = False
    while p1<len(s1) and p2<len(s2):
        if s1[p1] != s2[p2]:
            if flag:
                return False
            else:
                p1+=1
                flag = True
                continue
        else:
            p1+=1
            p2+=1
    return True
            



class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ('pale', 'ple', True),
        ('pales', 'pale', True),
        ('pale', 'bale', True),
        ('paleabc', 'pleabc', True),
        ('pale', 'ble', False),
        ('a', 'b', True),
        ('', 'd', True),
        ('d', 'de', True),
        ('pale', 'pale', True),
        ('pale', 'ple', True),
        ('ple', 'pale', True),
        ('pale', 'bale', True),
        ('pale', 'bake', False),
        ('pale', 'pse', False),
        ('ples', 'pales', True),
        ('pale', 'pas', False),
        ('pas', 'pale', False),
        ('pale', 'pkle', True),
        ('pkle', 'pable', False),
        ('pal', 'palks', False),
        ('palks', 'pal', False)
    ]

    def test_one_away(self):
        for [test_s1, test_s2, expected] in self.data:
            actual = one_away(test_s1, test_s2)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()