# https://www.hackerrank.com/challenges/count-luck/problem

class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)

def countLuck(matrix, k):
    rows = len(matrix)
    cols = len(matrix[0])
    sr = None
    sc = None
    fr = None
    fc = None
    path = None
    neighbours = {}
    counter = 0

    for row in range(rows):
        for col in range(cols):
            if matrix[row][col] == 'M':
                sr = row
                sc = col
            elif matrix[row][col] == '*':
                fr = row
                fc = col
            neighbours[(row, col)] = neighbour_counter(matrix, row, col, rows, cols)
    path = dfs(matrix, sr, sc, fr, fc, rows, cols)
    if neighbours[(sr, sc)] > 1:
      counter += 1
    for coordinates in path:
      if neighbours[coordinates] > 2 and coordinates != (sr, sc) and coordinates != (fr, fc):
        counter += 1

    if counter == k:
        return 'Impressed'
    else:
        return 'Oops!' 



def dfs(matrix, sr, sc, fr, fc, rows, cols):
    stack = Stack()
    stack.push([(sr, sc)])
    visited = set([(sr, sc)])
    while stack.size():
        path = stack.pop()
        row, col = path[-1]
        if row == fr and col == fc:
            return path
        for row2, col2 in ((row + 1, col), (row, col + 1), (row - 1, col), (row, col - 1)):
            if 0 <= row2 < rows and 0 <= col2 < cols and matrix[row2][col2] != 'X' and (row2, col2) not in visited:
                stack.push(path + [(row2, col2)])
                visited.add((row2, col2))

def neighbour_counter(matrix, row, col, rows, cols):
  counter = 0
  if row > 0 and matrix[row - 1][col] != 'X':
    counter += 1
  if row < rows - 1 and matrix[row + 1][col] != 'X':
    counter += 1
  if col > 0 and matrix[row][col - 1] != 'X':
    counter += 1
  if col < cols - 1 and matrix[row][col + 1] != 'X':
    counter += 1
  return counter