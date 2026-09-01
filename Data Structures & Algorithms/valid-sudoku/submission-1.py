class Solution:
    def _are_rows_valid(self, board: List[List[str]]):
        for row in board:
            cels_dict = {}
            for cel in row:
                if cel != '.':
                    if not cels_dict.get(cel): 
                        cels_dict[cel] = 1
                        continue
                else:
                    continue
                return False
        return True

        
    def _are_cols_valid(self, board: List[List[str]]):
        for i in range(len(board)):
            cols_dict = {}
            for j in range(len(board[0])):
                if board[j][i] != '.':
                    if not cols_dict.get(board[j][i]):
                        cols_dict[board[j][i]] = 1
                        continue
                else:
                    continue
                return False
        return True

    def _are_boxes_valid(self, board: List[List[str]]):
        for box in range(9):
            box_dict = {}

            start_row = (box // 3) * 3
            start_col = (box % 3) * 3

            for i in range(3):
                for j in range(3):
                    cel = board[start_row + i][start_col + j]

                    if cel != '.':
                        if not box_dict.get(cel):
                            box_dict[cel] = 1
                            continue
                    else:
                        continue

                    return False

        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return self._are_boxes_valid(board) and self._are_cols_valid(board) and self._are_rows_valid(board)

    

    
