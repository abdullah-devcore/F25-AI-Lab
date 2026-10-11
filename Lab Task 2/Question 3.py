class Smart_AC:
    def __init__(self):
        self.current_mode = None

    def check_room(self, room_status, temperature):
        if not room_status:
            new_mode = "OFF"
        elif temperature < 18:
            new_mode = "HEAT"
        elif temperature > 28:
            new_mode = "COOL"
        else:
            new_mode = "OFF"

        old_mode = self.current_mode

        if old_mode != new_mode:
            action = "Send Command"
        else:
            action = "No Command"

        self.current_mode = new_mode

        return old_mode, new_mode, action


room = Smart_AC()

ac_readings = [
    (True, 16),
    (True, 16),
    (True, 26),
    (True, 28),
    (True, 30),
    (True, 23),
    (False, 23)
]

for room_status, temperature in ac_readings:
    old_mode, new_mode, action = room.check_room(room_status, temperature)

    print(f"Previous Mode: {old_mode} | Temperature: {temperature} | Occupied: {room_status} | Target Mode: {new_mode} | Action: {action}")
