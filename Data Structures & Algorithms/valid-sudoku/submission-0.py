from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_dict_map = defaultdict(list)
        column_dict_map = defaultdict(list)
        box_dict_map = defaultdict(list)
        for i, row in enumerate(board):
            for j, cell in enumerate(row):
                if cell != ".":   
                    row_dict_map[i].append(cell)
                    column_dict_map[j].append(cell)
                    box_dict_map[(i//3)*3+(j//3)].append(cell)
        for i in range(len(board)):
            if len(row_dict_map[i]) != len(set(row_dict_map[i])):
                return False
            if len(column_dict_map[i]) != len(set(column_dict_map[i])):
                return False
            if len(box_dict_map[i]) != len(set(box_dict_map[i])):
                return False
        return True
        