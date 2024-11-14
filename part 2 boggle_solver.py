class Boggle:
    def __init__(self, grid, dictionary):
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0]) if self.rows > 0 else 0
        self.dictionary = set(word.upper() for word in dictionary)
        self.prefix_set = self.build_prefix_set(self.dictionary)
        self.solutions = set()

    def build_prefix_set(self, dictionary):
        prefix_set = set()
        for word in dictionary:
            for i in range(len(word)):
                prefix_set.add(word[:i+1])
        return prefix_set

    def isValidGrid(self):
        """Check if the grid is valid"""
        try:
            if not isinstance(self.grid, list):
                return False
            if len(self.grid) == 0:
                return False
            if not all(isinstance(row, list) for row in self.grid):
                return False
            if not all(len(row) == self.cols for row in self.grid):
                return False
            # Check all cells contain strings
            for row in self.grid:
                for cell in row:
                    if not isinstance(cell, str):
                        return False
            return True
        except:
            return False

    def explore(self, row, col, word, visited):
        try:
            if (row, col) in visited or not (0 <= row < self.rows and 0 <= col < self.cols):
                return

            current = self.grid[row][col].upper()
            new_word = word
            
            if current == 'Q':
                new_word += 'QU'
            elif current == 'S' and len(word) > 0 and word[-1] == 'T':
                new_word = word[:-1] + 'ST'
            else:
                new_word += current

            if new_word not in self.prefix_set:
                return

            if (len(new_word) >= 3 and 
                new_word in self.dictionary and 
                not new_word.endswith('Q') and 
                not new_word.endswith('S')):
                self.solutions.add(new_word)

            visited.add((row, col))

            for dr, dc in [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]:
                self.explore(row + dr, col + dc, new_word, visited)

            visited.remove((row, col))
        except IndexError:
            return

    def solve(self):
        if not self.isValidGrid():
            return []
            
        self.solutions.clear()
        for row in range(self.rows):
            for col in range(self.cols):
                self.explore(row, col, "", set())
        return sorted(list(self.solutions))

    def getSolution(self):
        return self.solve()