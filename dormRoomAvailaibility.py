class DormRoomAvailability:
    def solve(self, rooms: list[list[int]]) -> int:
        """
        Counts the number of dorm rooms that have at least two available spots.
        """
        total = 0
        for room in rooms:
            if (
                isinstance(room, (list, tuple)) and
                len(room) == 2 and
                all(isinstance(x, int) for x in room)
            ):
                available_spots = room[1] - room[0]
                # Check if the room has at least two available spots
                if available_spots >= 2:
                    total += 1
            else:
                # Skip invalid room entry and optionally log a warning
                print(f"Warning: Skipping invalid room entry: {room}")
        return total

if __name__ == "__main__":
    # Example usage:
    obj = DormRoomAvailability()
    rooms1 = [[1.1, 3], [2, 5], [4, 6]]
    rooms2 = [[1], [2, 3], [3, 4]]
    result1 = obj.solve(rooms1)
    result2 = obj.solve(rooms2)
    print(f"Result 1: {result1}")
    print(f"Result 2: {result2}")