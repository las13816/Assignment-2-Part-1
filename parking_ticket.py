import math

class ParkingTicket:
    def __init__(self, car, officer, illegal_minutes):
        self.car = car  # Composition (retain reference)
        self.officer_name = officer.name
        self.badge_number = officer.badge_number
        self.illegal_minutes = illegal_minutes
        self.fine = self.calculate_fine()

    def calculate_fine(self):
        hours = math.ceil(self.illegal_minutes / 60)
        fine = 25  # First hour (or part)
        if hours > 1:
            fine += (hours - 1) * 10
        return fine

    def __str__(self):
        return (
            "\n--- Parking Ticket ---\n"
            f"Car: {self.car.make} {self.car.model}\n"
            f"Color: {self.car.color}\n"
            f"License: {self.car.license_number}\n"
            f"Minutes Over: {self.illegal_minutes}\n"
            f"Fine: ${self.fine:.2f}\n"
            f"Issued By: Officer {self.officer_name}, "
            f"Badge #{self.badge_number}\n"
        )