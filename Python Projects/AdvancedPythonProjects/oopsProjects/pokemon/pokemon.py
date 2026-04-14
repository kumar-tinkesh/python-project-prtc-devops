# creating a pokemon
# viewing pokemon
# feed them for health
# battle between pokemon

class Pokemon:
    def __init__(self, name, primary_type, max_hp):
        self.name = name
        self.primary_type = primary_type
        self.hp = max_hp
        self.max_hp = max_hp

    def __str__(self):
        return f"{self.name} ({self.primary_type} : {self.hp} / {self.max_hp})"

    def feed(self):
        if self.hp < self.max_hp:
            self.hp += 10
            print(f"{self.name} has now {self.hp} Power!")
        else:
            print(f"{self.name} got full Power!")

    def battle(self, other):
        print(f"Battle:: {self.name} --Vs-- {other.name}")
        result = self.typewheel(self.primary_type, other.primary_type)
        if result == 'lose':
            self.hp -= 20
            print(f"{self.name} lost and now power is {self.hp}")
        print("")
        print(f"{self.name} Vs {other.name} and result is {result}")
        print("")
        #call typewheel

    @staticmethod
    def typewheel(type1, type2):
        result = {
            0: "lose",
            1: "Win",
            -1: "Tie"
        }
        # mapping between types and result
        game_map = {
            'water': 0,
            'fire': 1,
            'grass': 2
        }


        # win - lose matrix when fighting with each other
        wl_matrix = [
            [-1, 1, 0],  # water
            [0, -1, 1],  # fire
            [1, 0, -1],  # grass
        ]

        wl_result = wl_matrix[game_map[type1]][game_map[type2]]
        return result[wl_result]

        # a winner

if __name__ == '__main__':
    print(Pokemon('danasur', 'fire', 100))
    print(Pokemon('bulbasur', 'grass', 150))








