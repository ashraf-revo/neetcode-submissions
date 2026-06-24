class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        cols = len(matrix[0])

        rows = len(matrix)

        total = cols * rows

        print(f"rows={rows} , cols={cols} , total={total} , target={target} ")

        def map_2d(n) -> tuple[int, int]:
            x = n // cols
            y = n % cols
            return (x, y)

        low = 0
        high = total - 1
        while low <= high:
            med = low + ((high - low) // 2)
            x, y = map_2d(med)
            print(f"{med} >>> {x},{y} value={matrix[x][y]}")

            if matrix[x][y] == target:
                return True
            elif matrix[x][y] < target:
                low = med + 1
            else:
                high = med - 1
        return False
