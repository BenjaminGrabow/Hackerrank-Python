# https://www.hackerrank.com/challenges/connected-cell-in-a-grid/problem?isFullScreen=false
class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size():
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)
def connectedCell(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    biggest_island = 0
    for row in range(rows):
        for col in range(cols):
            if matrix[row][col] == 1:
                biggest_island, matrix = island_counter(matrix,row,col,rows,cols, biggest_island)
    return biggest_island
def island_counter(matrix, row, col, rows, cols, biggest_island):
    queue = Queue()
    counter = 1
    matrix[row][col] = 0
    queue.enqueue((row, col))
    while queue.size():
        row, col = queue.dequeue()
        for row2, col2 in ((row + 1, col), (row, col + 1), (row, col - 1), (row - 1, col),(row + 1, col + 1), (row - 1, col - 1), (row + 1, col - 1), (row - 1, col + 1)):
            if 0 <= row2 < rows and 0 <= col2 < cols and matrix[row2][col2] == 1:
                queue.enqueue((row2, col2))
                matrix[row2][col2] = 0
                counter += 1
    if biggest_island > counter:
        counter = biggest_island
    return counter, matrix