import random

def generate_grid(rows,cols, obstacle_probability):
    grid = []
    for _ in range(rows):
        row = []
        for _ in range(cols):
            if random.random() < obstacle_probability:
                row.append(1)
            else:
                row.append(0)
        grid.append(row)
    return grid
obs_prob = float(input("Enter the obstacle probability: "))
grid = generate_grid(10,10, obs_prob)
for row in grid:
    print(row)