class ParkingMeter:
    def __init__(self, minutes_purchased=60):
        self._minutes_purchased = None
        self.minutes_purchased = minutes_purchased  # Use setter validation

    @property
    def minutes_purchased(self):
        return self._minutes_purchased

    @minutes_purchased.setter
    def minutes_purchased(self, minutes):
        if minutes <= 0:
            raise ValueError("Minutes purchased must be greater than 0.")
        self._minutes_purchased = minutes