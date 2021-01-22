class Barbell:
    def __init__(self, profile):
        self.profile = profile    # tuple
        self.unit = profile[0]    # str
        self.bar = profile[1]     # int
        self.plates = profile[2]  # lst
        print(f"Welcome to Barbell Calculator! The bar weighs {self.bar}{self.unit}.")
        while True:
            self.pick_plates()

    def get_weight(self):
        weight = input("How much weight would you like to lift? ")

        if self.valid_input(weight):
            return (int(weight) - self.bar) / 2
        else:
            return self.get_weight()

    def valid_input(self, str_number):
        try:
            number = int(str_number)
        except ValueError:
            print("Please enter a numeric value.\n")
            return False
        if number < self.bar:
            print("Oops, the bar is heavier than that!\n")
            return False
        elif number % 5 != 0:
            print("Please enter a number divisible by 5.\n")
            return False
        else:
            return True

    def pick_plates(self):
        plates_on_bar = []
        weight_to_add = self.get_weight()

        for plate in self.plates:
            while weight_to_add >= plate:
                plates_on_bar.append(plate)
                weight_to_add -= plate

        print("Here are the plates you should add to each side:\n",
              plates_on_bar, "\n")

