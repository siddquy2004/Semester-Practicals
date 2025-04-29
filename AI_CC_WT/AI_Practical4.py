n = 8

def print_solution(board):
    for i in range(n):
        for j in range(n):
            print(board[i][j], end=" ")
        print()

def is_safe(row, col, slash_code, backslash_code,
            row_lookup, slash_code_lookup, backslash_code_lookup):
    if (slash_code_lookup[slash_code[row][col]] or
        backslash_code_lookup[backslash_code[row][col]] or
        row_lookup[row]):
        return False
    return True

def solve_n_queens_util(board, col, slash_code, backslash_code,
                        row_lookup, slash_code_lookup, backslash_code_lookup):
    if col >= n:
        return True

    for i in range(n):
        if is_safe(i, col, slash_code, backslash_code,
                   row_lookup, slash_code_lookup, backslash_code_lookup):
            board[i][col] = 1
            row_lookup[i] = True
            slash_code_lookup[slash_code[i][col]] = True
            backslash_code_lookup[backslash_code[i][col]] = True

            if solve_n_queens_util(board, col + 1, slash_code, backslash_code,
                                   row_lookup, slash_code_lookup, backslash_code_lookup):
                return True

            board[i][col] = 0
            row_lookup[i] = False
            slash_code_lookup[slash_code[i][col]] = False
            backslash_code_lookup[backslash_code[i][col]] = False

    return False

def solve_n_queens():
    board = [[0 for _ in range(n)] for _ in range(n)]
    slash_code = [[0 for _ in range(n)] for _ in range(n)]
    backslash_code = [[0 for _ in range(n)] for _ in range(n)]

    row_lookup = [False] * n
    slash_code_lookup = [False] * (2 * n - 1)
    backslash_code_lookup = [False] * (2 * n - 1)

    for r in range(n):
        for c in range(n):
            slash_code[r][c] = r + c
            backslash_code[r][c] = r - c + (n - 1)

    if not solve_n_queens_util(board, 0, slash_code, backslash_code,
                                row_lookup, slash_code_lookup, backslash_code_lookup):
        print("solution does not exist")
        return False

    print_solution(board)
    return True

# driver code
solve_n_queens()
