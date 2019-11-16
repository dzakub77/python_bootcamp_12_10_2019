
class ElectricCar:

    def __init__(self, energy):
        self.energy = energy
        self.traveled_distance = 0

    def drive(self, distance):
        if distance + self.traveled_distance > self.energy:
            distance = self.energy - self.traveled_distance
            self.traveled_distance = self.energy

        else:
            self.traveled_distance += distance
        return distance
    def charge(self):
        self.traveled_distance = 0



def test_ElectricCar_drive():
    car = ElectricCar(100)
    assert car.drive(70) == 70
    assert car.drive(50) == 30

def test_ElectricCar_drive_over_energy_in_one_travel():
    car = ElectricCar(100)
    assert car.drive(120) == 100

def test_ElectricCar_charge():
    car = ElectricCar(100)
    assert car.drive(100) == 100
    assert car.drive(30) == 0
    assert car.energy == 100
    assert car.traveled_distance == 100
    car.charge()
    assert car.energy == 100
    assert car.drive(30) == 30
    assert car.traveled_distance == 30