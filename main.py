from parked_car import ParkedCar
from parking_meter import ParkingMeter
from police_officer import PoliceOfficer


def scenario_separator(title):
    print("\n" + "=" * 50)
    print(title)
    print("=" * 50)


def main():


    scenario_separator("Scenario 1: Legally Parked")

    car1 = ParkedCar("Toyota", "Camry", "Red", "XYZ123", 30)
    meter1 = ParkingMeter(40)
    officer1 = PoliceOfficer("John Doe", "5678")

    ticket1 = officer1.inspect_car(car1, meter1)

    if ticket1:
        print(ticket1)
    else:
        print("No ticket issued. The car is legally parked.")

   
    scenario_separator("Scenario 2: Less Than 1 Hour Over")

    car2 = ParkedCar("Honda", "Accord", "Blue", "ABC987", 70)
    meter2 = ParkingMeter(60)
    officer2 = PoliceOfficer("Jane Smith", "1234")

    ticket2 = officer2.inspect_car(car2, meter2)

    if ticket2:
        print(ticket2)
    else:
        print("No ticket issued.")

  
    scenario_separator("Scenario 3: Multiple Hours Over")

    car3 = ParkedCar("Ford", "Mustang", "Black", "LMN456", 190)
    meter3 = ParkingMeter(60)
    officer3 = PoliceOfficer("James Brown", "4321")

    ticket3 = officer3.inspect_car(car3, meter3)

    if ticket3:
        print(ticket3)
    else:
        print("No ticket issued.")

  
    scenario_separator("Scenario 4: Multiple Cars in Parking Lot")

    officer4 = PoliceOfficer("Sarah Green", "9999")

    cars = [
        (ParkedCar("Nissan", "Altima", "White", "JKL321", 60), ParkingMeter(60)),
        (ParkedCar("Chevy", "Malibu", "Silver", "QWE789", 80), ParkingMeter(60)),
        (ParkedCar("BMW", "X5", "Black", "BMW999", 500), ParkingMeter(60)),
        (ParkedCar("Mazda", "3", "Blue", "MAZ321", 45), ParkingMeter(60)),
    ]

    for car, meter in cars:
        ticket = officer4.inspect_car(car, meter)
        print(f"\nInspecting: {car.make} {car.model} ({car.license_number})")

        if ticket:
            print(ticket)
        else:
            print("No ticket issued. Car is legally parked.")


if __name__ == "__main__":
    main()