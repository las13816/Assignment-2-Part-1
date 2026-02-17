class ParkedCar:
    def __init__(self, make, model, color, license_number, minutes_parked=60):
        self.make = make
        self.model = model
        self.color = color
        self.license_number = license_number
        self._minutes_parked = None
        self.minutes_parked = minutes_parked  # Use setter validation

    @property
    def minutes_parked(self):
        return self._minutes_parked

    @minutes_parked.setter
    def minutes_parked(self, minutes):
        if minutes <= 0:
            raise ValueError("Minutes parked must be greater than 0.")
        self._minutes_parked = minutes

    def __str__(self):
        return (f"{self.make} {self.model}, {self.color}, "
                f"License: {self.license_number}, "
                f"Minutes Parked: {self.minutes_parked}")