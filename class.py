class Phone:
    def set_color(self,color):
        self.color=color
    def set_cost (self,cost):
        self.cost=cost
    def show_color(color):
        return color
    def show_cost(cost):
        return cost
    def play_games(self):
        print("playing a game")
    def play_cost(self):
        print("cost of game")
p2 = Phone()
p2.set_color('blue')
p2.set_cost(300)
p2.show_color()
p2.show_cost()
p2.play_games()
p2.play_cost