# https://www.algoexpert.io/questions/River%20Sizes
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
	
def riverSizes(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    size_rivers = []
    for row in range(rows):
        for col in range(cols):
            if matrix[row][col] == 1:
                size_rivers, matrix = river_counter(matrix,row,col,rows,cols, size_rivers)
    return size_rivers

def river_counter(matrix, row, col, rows, cols, size_rivers):
    queue = Queue()
    counter = 1
    matrix[row][col] = 0
    queue.enqueue((row, col))
    while queue.size():
        row, col = queue.dequeue()
        for row2, col2 in ((row + 1, col), (row, col + 1), (row, col - 1), (row - 1, col)):
            if 0 <= row2 < rows and 0 <= col2 < cols and matrix[row2][col2] == 1:
                queue.enqueue((row2, col2))
                matrix[row2][col2] = 0
                counter += 1
    
    size_rivers.append(counter)
    return size_rivers, matrix