class Passenger:

    def __init__(self, name):
        self.name = name


class Flight:

    counter = 1

    def __init__(self, origin, destination, duration):

        # keep recording flight_if
        self.id = Flight.counter
        Flight.counter += 1

        # keep recording for passengers
        self.passengers = []

        # records about flight
        self.origin = origin
        self.destination = destination
        self.duration = duration

    def print_info(self):
        print(f"Flight origin: {self.origin}")
        print(f"Flight destination: {self.destination}")
        print(f"Flight duration: {self.duration}")

        print("Passengers in that flight:")
        for passenger in self.passengers:
            print(f"{passenger.name}")

    def add_passenger(self, p):
        self.passengers.append(p)
        p.flight_id = self.id

    def delay(self, amount):
        self.duration += amount


def main():
    f1 = Flight('New York', 'London', 490)
    f1.delay(10)

    p1 = Passenger("Kamol")
    p2 = Passenger("Odil")

    f1.add_passenger(p1)
    f1.add_passenger(p2)

    f1.print_info()


if __name__ == '__main__':
    main()
