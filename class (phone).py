class Phone :


    def set_colour(self, colour) :
        self.colour = colour

    def set_cost(self, cost) :
        self.cost = cost

    def show_cost(self) :
        return self.cost


    def show_colour(self) :
        return self.colour



    def Make_call(self) :
        print("making phone call")

    def Play_game(self) :
        print("opening game")

p1 = Phone()

p1.Make_call()