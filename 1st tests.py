class Boggle:
    def findAllSolutions(self):
        solutions = set()

        def dfs(row, col, word, visited):
            # Base case checks
            if not (0 <= row < self.rows and 0 <= col < self.cols):
                return
            if (row, col) in visited:
                return

            # Add current cell to visited
            visited.add((row, col))
            
            # Process current cell
            letter = self.grid[row][col].lower()
            current_word = word + letter

            if not self.trie.is_prefix(current_word):
                visited.remove((row, col))
                return

            if current_word in self.dictionary:
                solutions.add(current_word)

            # Recursive exploration
            for dr, dc in [(-1, -1), (-1, 0), (-1, 1), 
                          (0, -1),           (0, 1),
                          (1, -1),  (1, 0),  (1, 1)]:
                new_row, new_col = row + dr, col + dc
                dfs(new_row, new_col, current_word, visited)

            # Backtrack
            visited.remove((row, col))

        # Start DFS from each cell
        for i in range(self.rows):
            for j in range(self.cols):
                dfs(i, j, "", set())

        return list(solutions)