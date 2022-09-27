# given a matrix filled with pixel values 0 & 1. replace all the connected pixels from a given starting point with a given value
# [[1,1,1
# [1,1,0]
# [1,0,1]]

def flood_fill(img, row, col, val):
    start = img[row][col]
    queue = [(row, col)]
    visited = set()
    while queue:
        row, col = queue.pop(0)
        visited.add((row, col))
        img[row][col] = val
        for row, col in neighbours(img, row, col, start):
            if (row, col) not in visited:
                queue.append((row, col))
    return img


def neighbours(img, row, col, start):
    valid_neighbours = [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]
    return [(row, col) for row, col in valid_neighbours if isValid(img, row, col) and img[row][col] == start]


def isValid(img, row, col):
    return row >= 0 and col >= 0 and row < len(img) and col < len(img[0])


img = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
print(flood_fill(img, 0, 0, 2))
