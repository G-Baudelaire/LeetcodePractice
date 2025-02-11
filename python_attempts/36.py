class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """

        for i in range(9):
            if not self.isRowValid(i, board):
                return False

            if not self.isColumnValid(i, board):
                return False

            if not self.isSquareValid(i, board):
                return False
        return True

    def isRowValid(self, row, board):
        for number in set(board[row]).difference({"."}):
            if 1 != board[row].count(number):
                return False

        return True

    def isColumnValid(self, column, board):
        column_numbers = [board[i][column] for i in range(9)]

        for number in set(column_numbers).difference({"."}):
            if 1 != column_numbers.count(number):
                return False

        return True

    def isSquareValid(self, square, board):
        starting_column = (square % 3) * 3
        starting_row = (square // 3) * 3
        square_numbers = [-1] * 9

        for i in range(9):
            square_numbers[i] = board[starting_row + i // 3][starting_column + i % 3]

        for number in set(square_numbers).difference({"."}):
            if 1 != square_numbers.count(number):
                return False

        return True


board = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
         ["6", ".", ".", "1", "9", "5", ".", ".", "."],
         [".", "9", "8", ".", ".", ".", ".", "6", "."],
         ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
         ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
         ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
         [".", "6", ".", ".", ".", ".", "2", "8", "."],
         [".", ".", ".", "4", "1", "9", ".", ".", "5"],
         [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

print(Solution().isValidSudoku(board))
