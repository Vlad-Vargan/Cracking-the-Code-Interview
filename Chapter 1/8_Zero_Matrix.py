import unittest

def zero_matrix(matrix):
    r = len(matrix)
    t = len(matrix[0])
    zero_r = set()
    zero_t = set()
    for row in range(r):
        for table in range(t):
            if not matrix[row][table]:
                zero_r.add(row)
                zero_t.add(table)
    
    if zero_r:
        for row in zero_r:
            matrix[row] = [0]*t
    if zero_t:
        for t in zero_t:
            for row in range(r):
                matrix[row][t] = 0
    return matrix

class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ([
            [1,  2,  3,  4,  0],
            [6,  0,  8,  9,  10],
            [11, 12, 13, 14, 15],
            [16, 0,  18, 19, 20],
            [21, 22, 23, 24, 25]
        ], [
            [0,  0, 0,  0,  0],
            [0,  0, 0,  0,  0],
            [11, 0, 13, 14, 0],
            [0,  0, 0,  0,  0],
            [21, 0, 23, 24, 0]
        ])
    ]

    def test_zero_matrix(self):
        for [test_matrix, expected] in self.data:
            actual = zero_matrix(test_matrix)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()