from app.repositories.booking_repository import (
    get_all_bookings,
    get_booking_by_id,
    create_booking,
    cancel_booking,
)
from app.repositories.room_repository import get_available_rooms, get_room_by_id, update_room_status
from app.repositories.pet_repository import get_pet_by_id

def list_bookings():
    return get_all_bookings()

def book_room(pet_id, room_id, check_in, check_out):
    pet = get_pet_by_id(pet_id)
    if not pet:
        raise ValueError(f"Pet with id {pet_id} does not exist")

    room = get_room_by_id(room_id)
    if not room:
        raise ValueError(f"Room with id {room_id} does not exist")
    if room[4] != "available":
        raise ValueError(f"Room {room[1]} is currently {room[4]}")

    booking_id = create_booking(pet_id, room_id, check_in, check_out, status="confirmed")
    update_room_status(room_id, "occupied")
    return booking_id

def cancel_room_booking(booking_id):
    booking = get_booking_by_id(booking_id)
    if not booking:
        raise ValueError(f"Booking {booking_id} not found")

    cancel_booking(booking_id)
    update_room_status(booking[2], "available")
    return True
