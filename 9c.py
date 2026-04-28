class GridWorld:
    def __init__(self, size=4):
        self.size = size
        self.agent_pos = [0, 0]

        # Environment setup
        self.wumpus = (2, 2)
        self.gold = (3, 3)
        self.pits = [(1, 1), (3, 0)]

        self.game_over = False

    
    def is_valid(self, x, y):
        return 0 <= x < self.size and 0 <= y < self.size

    def move(self, direction):
        if self.game_over:
            print("Game already ended.")
            return

        x, y = self.agent_pos

        if direction == "up":
            new_pos = (x - 1, y)
        elif direction == "down":
            new_pos = (x + 1, y)
        elif direction == "left":
            new_pos = (x, y - 1)
        elif direction == "right":
            new_pos = (x, y + 1)
        else:
            print("Invalid move")
            return

        if self.is_valid(*new_pos):
            self.agent_pos = list(new_pos)
            self.check_status()
        else:
            print("Bump! Hit a wall.")

    # ---------------- Game Logic ----------------
    def check_status(self):
        x, y = self.agent_pos

        if (x, y) == self.wumpus:
            self.display_grid()
            print("💀 You were eaten by the Wumpus! Game Over.")
            self.game_over = True

        elif (x, y) in self.pits:
            self.display_grid()
            print("🕳️ You fell into a pit! Game Over.")
            self.game_over = True

        elif (x, y) == self.gold:
            self.display_grid()
            print("🏆 You found the gold! You win!")
            self.game_over = True

        else:
            self.percepts()

    # ---------------- Perception ----------------
    def percepts(self):
        x, y = self.agent_pos

        adj = [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]

        for cell in adj:
            if cell == self.wumpus:
                print("👃 You smell a stench!")
            if cell in self.pits:
                print("💨 You feel a breeze!")

    # ---------------- Grid Display ----------------
    def display_grid(self):
        print("\nGrid World:")
        for i in range(self.size):
            for j in range(self.size):
                if [i, j] == self.agent_pos:
                    print("A", end=" ")
                elif (i, j) == self.wumpus:
                    print("W", end=" ")
                elif (i, j) == self.gold:
                    print("G", end=" ")
                elif (i, j) in self.pits:
                    print("P", end=" ")
                else:
                    print(".", end=" ")
            print()
        print()

    # ---------------- Utility ----------------
    def show_position(self):
        print(f"Agent position: {tuple(self.agent_pos)}")


env = GridWorld()

print("🎮 Welcome to Grid World (Wumpus-like)")
print("Commands: up, down, left, right, exit\n")

while True:
    env.display_grid()

    action = input("Enter move: ").lower()

    if action == "exit":
        print("Game exited.")
        break
    else:
        env.move(action)

    if env.game_over:
        break