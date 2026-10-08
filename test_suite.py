import unittest
import os
from app.database.connection import get_connection
from app.repositories.pet_repository import (
    get_all_pets,
    get_pet_by_id,
    add_pet,
    update_pet,
    delete_pet,
)
from app.repositories.room_repository import (
    get_all_rooms,
    get_available_rooms,
    get_room_by_id,
)
from app.services.pet_service import (
    list_pets,
    get_pet,
    create_pet,
    update_pet_service,
    delete_pet_service,
)
from app.services.booking_service import (
    list_bookings,
    book_room,
    cancel_room_booking,
)
from app.mcp.server import (
    get_all_pets_tool,
    list_available_rooms,
    show_all_bookings,
)

class TestHappyPawsEndToEnd(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Verify connection
        conn = get_connection()
        cls.assertIsNotNone(cls, conn)
        conn.close()

    def test_01_database_connectivity(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT DATABASE()")
        db_name = cursor.fetchone()[0]
        cursor.close()
        conn.close()
        self.assertEqual(db_name, "happy_paws")

    def test_02_pet_service_crud(self):
        # 1. Create
        pet_id = create_pet("TestDog", "Dog", "Husky", 3, "Alice")
        self.assertIsInstance(pet_id, int)
        self.assertGreater(pet_id, 0)

        # 2. Read
        pet = get_pet(pet_id)
        self.assertIsNotNone(pet)
        self.assertEqual(pet[1], "TestDog")
        self.assertEqual(pet[2], "Dog")
        self.assertEqual(pet[3], "Husky")

        # 3. Update
        updated = update_pet_service(pet_id, "TestDog Updated", "Dog", "Husky", 4, "Alice")
        self.assertEqual(updated, 1)
        pet_updated = get_pet(pet_id)
        self.assertEqual(pet_updated[1], "TestDog Updated")
        self.assertEqual(pet_updated[4], 4)

        # 4. Delete
        deleted = delete_pet_service(pet_id)
        self.assertEqual(deleted, 1)
        pet_after = get_pet(pet_id)
        self.assertIsNone(pet_after)

    def test_03_room_availability(self):
        rooms = get_all_rooms()
        self.assertGreaterEqual(len(rooms), 1)
        avail = get_available_rooms()
        for r in avail:
            self.assertEqual(r[4], "available")

    def test_04_booking_workflow(self):
        # Create temp pet and book standard room (103 is available)
        pet_id = create_pet("BookingPet", "Cat", "Persian", 2, "Bob")
        avail_rooms = get_available_rooms()
        self.assertGreater(len(avail_rooms), 0)
        target_room_id = avail_rooms[0][0]

        # Book
        b_id = book_room(pet_id, target_room_id, "2026-11-01", "2026-11-05")
        self.assertIsInstance(b_id, int)

        # Check room status updated to occupied
        room = get_room_by_id(target_room_id)
        self.assertEqual(room[4], "occupied")

        # Verify cannot delete pet while booking exists (foreign key protection)
        with self.assertRaises(ValueError):
            delete_pet_service(pet_id)

        # Cancel booking
        cancel_success = cancel_room_booking(b_id)
        self.assertTrue(cancel_success)

        # Room should be available again
        room_after = get_room_by_id(target_room_id)
        self.assertEqual(room_after[4], "available")

        # Now delete booking first, then delete pet
        from app.repositories.booking_repository import delete_booking
        delete_booking(b_id)
        deleted = delete_pet_service(pet_id)
        self.assertEqual(deleted, 1)

    def test_05_fastmcp_tools(self):
        # Test tool outputs
        pets = get_all_pets_tool()
        self.assertIsInstance(pets, list)
        self.assertGreater(len(pets), 0)
        self.assertIn("name", pets[0])

        rooms = list_available_rooms()
        self.assertIsInstance(rooms, list)

        bookings = show_all_bookings()
        self.assertIsInstance(bookings, list)

if __name__ == "__main__":
    unittest.main()
