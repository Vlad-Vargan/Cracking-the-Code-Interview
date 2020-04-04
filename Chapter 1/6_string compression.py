import unittest

def string_compression(text):
    answer = []
    occurances = 0
    unique = text[0]
    for index, letter in enumerate(text):
        if letter == unique:
            occurances += 1
        else:
            answer.append(text[index-1])
            unique = letter

            answer.append(str(occurances))
            occurances = 1
    answer.append(unique)
    answer.append(str(occurances))

    answer = "".join(answer)
    if len(answer) > len(text):
        return text
    else:
        return "".join(answer)

class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ('aabcccccaaa', 'a2b1c5a3'),
        ('abcdef', 'abcdef')
    ]

    def test_string_compression(self):
        for [test_string, expected] in self.data:
            actual = string_compression(test_string)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()
