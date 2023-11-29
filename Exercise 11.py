def is_valid(grid, x, y, m, n):
    return m > x >= 0 == grid[x][y] and 0 <= y < n


def isDestinationReachable(grid, sx, sy, dx, dy, k, m, n):

    queue = []

    distances = [[-1 for j in range(n)] for i in range(m)]

    queue.append((sx, sy))
    distances[sx][sy] = 0

    while queue:

        x, y = queue.pop(0)
        if x == dx and y == dy and distances[x][y] < k :
            return True

        if distances[x][y] >= k:
            return False

        for i, j in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            new_x = x + i
            new_y = y + j

            if is_valid(grid, new_x, new_y, m, n) and distances[new_x][new_y] == -1:

                queue.append((new_x, new_y))
                distances[new_x][new_y] = distances[x][y] + 1



    return False


grid = [[0, 0, 0],
        [1, 1, 0],
        [0, 0, 0],
        ]

sx = 0
sy = 0
dx = 0
dy = 2
K = 7
m = 3
n = 3

# Function call
print(isDestinationReachable(grid, sx, sy, dx, dy, K, m, n))
