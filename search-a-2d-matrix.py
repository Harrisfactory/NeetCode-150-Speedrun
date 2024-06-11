class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        #first binary search for correct row
        left, right = 0, len(matrix) - 1

        target_row = None

        while left <= right:
            middle = (left + right) // 2
            if target >= matrix[middle][0] and target <= matrix[middle][-1]:
                target_row = middle
                break
            elif target > matrix[middle][-1]:
                left = middle + 1
            else:
                right = middle - 1
        
        #no target found, so we can already return False before searching further
        if target_row == None:
            return False

        left, right = 0, len(matrix[target_row]) - 1

        while left <= right:
            middle = (left + right) // 2

            if target == matrix[target_row][middle]:
                return True
            elif target > matrix[target_row][middle]:
                left = middle + 1
            else:
                right = middle - 1

        return False

        #O(log(m * n))     