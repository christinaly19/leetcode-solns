# 36. Valid Sudoku
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        rowMap = {}
        # checking each row 
        for row in board:
            rowMap = {}
            for num in row:
                if num == ".": 
                    continue
                elif num in rowMap:
                    return False
                else:
                    rowMap[num] = 1
         # checking each column 
        columnMap = {}
        for i in range(9):
            columnMap = {}
            for row in board:
                if row[i] == ".": 
                    continue
                elif row[i] in columnMap:
                    return False
                else:
                    columnMap[row[i]] = 1

        # Checking each 3x3 subgrid
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                subgridMap = {}
                for x in range(3):
                    for y in range(3):
                        num = board[i + x][j + y]
                        if num != '.':
                            if num in subgridMap:
                                return False
                            else:
                                subgridMap[num] = 1
            
        return True
'''
Kind of brute forced Suduko... 
Had separate checking for columns, rows, and then subgrids... 
'''