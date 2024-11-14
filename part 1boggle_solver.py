class Boggle:
    def __init__(self, grid, dictionary):
        self.grid = grid
        self.dictionary = dictionary

    def findAllSolutions(self):
        solutions = set()
        
        # Edge case: return empty list if grid or dictionary is invalid
        if not self.grid or not self.dictionary or len(self.grid) == 0 or len(self.grid[0]) == 0:
            return []

        # Convert dictionary to a set for quick lookup
        dict_set = set(word.lower() for word in self.dictionary)

        # Helper to determine if a word is valid
        def is_valid_word(word):
            return len(word) >= 3 and word in dict_set

        # Rows and columns of the grid
        rows = len(self.grid)
        cols = len(self.grid[0])

        # Directions for exploring adjacent cells (8 possible directions)
        directions = [
            (-1, 0), (1, 0), (0, -1), (0, 1),
            (-1, -1), (-1, 1), (1, -1), (1, 1)
        ]

        # DFS helper function to explore the grid
        def dfs(row, col, visited, current_word):
            # Add the current letter to the word
            letter = self.grid[row][col].lower()
            current_word += "qu" if letter == "qu" else letter

            # If the word is valid, add it to the solution set
            if is_valid_word(current_word):
                solutions.add(current_word)

            # Mark this cell as visited
            visited[row][col] = True

            # Explore all 8 possible directions
            for dx, dy in directions:
                new_row, new_col = row + dx, col + dy

                # Check if the new position is within bounds and not visited
                if 0 <= new_row < rows and 0 <= new_col < cols and not visited[new_row][new_col]:
                    dfs(new_row, new_col, visited, current_word)

            # Unmark the current cell (backtrack)
            visited[row][col] = False

        # Main loop: Start DFS from each cell in the grid
        for i in range(rows):
            for j in range(cols):
                visited = [[False] * cols for _ in range(rows)]
                dfs(i, j, visited, "")

        # Return the solutions as a list
        return list(solutions)

    def getSolution(self):
        return self.findAllSolutions()
