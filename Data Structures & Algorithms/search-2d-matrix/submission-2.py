class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        start_row, end_row = 0, len(matrix) - 1
        target_list = []

        while start_row <= end_row:
            mid_row = (end_row + start_row) // 2
            
            if matrix[mid_row][0] <= target and matrix[mid_row][-1] >= target:
                target_list = matrix[mid_row]
                break
            if matrix[mid_row][0] > target:
                end_row = mid_row - 1
            if matrix[mid_row][-1] < target:
                start_row = mid_row + 1

        start, end = 0, len(target_list) - 1

        while start <= end:
            mid = (start + end) // 2

            if target < target_list[mid]:
                end = mid - 1 
            elif target > target_list[mid]:
                start = mid + 1
            else:
                return True
        return False