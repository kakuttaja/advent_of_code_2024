from time import perf_counter
import numpy as np

def score(grid):
    res = 0
    for (r, c) in list(zip(*np.where((grid == "O") | (grid == "[")))):
       res += 100 * r + c
    return res

def move(y0, x0, dy, dx, grid):
    y0,x0 = y0+dy,x0+dx
    if all([grid[y0,x0] != '[' or move(y0,x0+1,dy,dx,grid) and move(y0,x0,dy,dx,grid),
        grid[y0,x0] != ']' or move(y0,x0-1,dy,dx,grid) and move(y0,x0,dy,dx,grid),
        grid[y0,x0] != 'O' or move(y0,x0,dy,dx,grid), grid[y0,x0] != '#']):
        grid[y0,x0], grid[y0-dy,x0-dx] = grid[y0-dy,x0-dx], grid[y0,x0]
        return True
    return False

def do_move(m: str, pos: tuple, grid: list, boxes = None):
    dy, dx = {"^": (-1, 0), "v": (1, 0), "<": (0, -1), ">": (0, 1)}[m]
    y0, x0 = pos
    if move(y0, x0, dy, dx, grid):
        return y0+dy, x0+dx
    return y0, x0

def main():
    g1, moves = open("15.txt").read().strip().split("\n\n")
    g2 = g1.replace(".", "..").replace("O", "[]").replace("#", "##").replace("@", "@.")
    moves = moves.replace("\n", "")
    g1, g2= np.array([[j for j in i] for i in g1.split('\n')]), np.array([[j for j in i] for i in g2.split('\n')])
    pos, pos2 = np.where(g1 == "@"), np.where(g2 == "@")
    for move in moves:
        old_grid = g1.copy()
        old_pos = pos
        old_grid2 = g2.copy()
        old_pos2 = pos2
        pos = do_move(move, pos, g1)
        pos2 = do_move(move, pos2, g2)
        if pos == old_pos:
            g1 = old_grid
        if pos2 == old_pos2:
            g2 = old_grid2
    return score(g1), score(g2)

if __name__ == '__main__':
    start = perf_counter()
    print(*main())
    print(f"This took {round(perf_counter() - start, 2)}s")
    