def load_grid(filename):
    with open(filename) as f:
        return [list(line.strip()) for line in f if line.strip()]

def count_word(grid, word):
    rows = len(grid)
    cols = max((len(r) for r in grid), default=0)
    N = len(word)
    count = 0

    # Fast path: single-character word -> count occurrences of that character
    if N == 1:
        ch = word
        return sum(1 for r in grid for e in r if e == ch)

    # Directions: (dx, dy)
    directions = [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1),          (0, 1),
                  (1, -1),  (1, 0), (1, 1)]

    for row in range(rows):
        row_len = len(grid[row])
        for col in range(row_len):
            for dx, dy in directions:
                i, j = row, col
                matched = True
                for k in range(N):
                    # Check row bounds and per-row column bounds before indexing
                    if not (0 <= i < rows):
                        matched = False
                        break
                    if not (0 <= j < len(grid[i])):
                        matched = False
                        break
                    if grid[i][j] != word[k]:
                        matched = False
                        break
                    i += dx
                    j += dy
                if matched:
                    count += 1
    return count

if __name__ == "__main__":
    
    grid = load_grid("/Users/tej/Downloads/input.txt")  # Put your puzzle input in a file named input.txt
    print(count_word(grid, "XMAS"))
