"""
51. N-Queens

The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.

For example,
There exist two distinct solutions to the 4-queens puzzle:

[
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
"""


class Solution:

    # 判断同一列和同一斜线上是否存在 Queue
    def is_valid(self, row, column, queen_record):
        c_left = column
        c_right = column
        for r in range(row, -1, -1):
            if queen_record[r] == column or queen_record[r] == c_left or queen_record[r] == c_right:
                return False
            c_left -= 1
            c_right += 1
        return True

    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """

        chess_board = [['.' for x in range(n)] for y in range(n)]

        # 初始化为 - 1，表示当前行还未放 Queue
        queen_record = [-1 for x in range(n)]
        solutions = []

        row = 0
        column = 0
        has_solution = True
        while has_solution:

            while row in range(n):

                while column < n or queen_record[row] == -1:

                    if column < n and self.is_valid(row, column, queen_record):
                        chess_board[row][column] = 'Q'
                        queen_record[row] = column
                        break
                    else:
                        column += 1

                        if column >= n:
                            # 当前行无法放置 Queue 开始回溯
                            row = row - 1
                            if row < 0:
                                has_solution = False
                                break

                            chess_board[row][queen_record[row]] = '.'
                            column = queen_record[row] + 1
                            queen_record[row] = -1

                if has_solution:
                    column = 0
                    row += 1

            if has_solution:
                solution = []
                for e in chess_board:
                    solution.append("".join(e))
                solutions.append(solution)

                # 回溯
                row -= 1
                chess_board[row][queen_record[row]] = '.'
                column = queen_record[row] + 1
                queen_record[row] = -1

        return solutions


if __name__ == '__main__':
    solution = Solution()
    result = solution.solveNQueens(4)
