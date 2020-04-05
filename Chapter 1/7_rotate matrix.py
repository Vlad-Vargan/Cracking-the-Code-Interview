# O(n)

import unittest

def print_matrix(matrix):
    for i in matrix:
        for j in i:
            print(str(j)+"\t", end="")
        print("\n"*2)

def rotate_matrix(matrix):
    # print_matrix(matrix)
    # print("_"*50)
    # print()

    demension = len(matrix)
    
    for i in range(0, demension//2):
        end = demension-1-i
        x = 0+i
        for j in range(0+i, end):
            y = 0+j
            end2 = demension-1-j
            matrix[x][y], matrix[y][end], matrix[end][end2], matrix[end2][i] =\
                matrix[end2][i], matrix[x][y], matrix[y][end], matrix[end][end2]
            # 0 0 -> 0 4 -> 4 4 -> 4 0 -> 0 0
            # 0 1 -> 1 4 -> 4 3 -> 3 0 -> 0 1
            # 0 2 -> 2 4 -> 4 2 -> 2 0 -> 0 2
            # 0 3 -> 3 4 -> 4 1 -> 1 0 -> 0 3

            # 1 1 -> 1 3 -> 3 3 -> 3 1 -> 1 1
            # 1 2 -> 2 3 -> 3 2 -> 2 1 -> 1 2
    # print_matrix(matrix)
    return matrix



class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ([
            [1,  2,  3,  4,  5],
            [6,  7,  8,  9,  10],
            [11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20],
            [21, 22, 23, 24, 25]
        ], [
            [21, 16, 11, 6,  1],
            [22, 17, 12, 7,  2],
            [23, 18, 13, 8,  3],
            [24, 19, 14, 9,  4],
            [25, 20, 15, 10, 5]
        ])
    ]

    def test_rotate_matrix(self):
        for [test_matrix, expected] in self.data:
            actual = rotate_matrix(test_matrix)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()