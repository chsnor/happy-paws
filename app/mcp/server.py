from fastmcp import FastMCP
from app.services.pet_service import (
    list_pets,
    get_pet,
    create_pet,
    update_pet_service,
    delete_pet_service,
)
from app.repositories.room_repository import get_available_rooms, get_all_rooms
from app.services.booking_service import book_room, list_bookings, cancel_room_booking

mcp = FastMCP("Happy Paws Pet Hotel")

@mcp.tool()
def get_all_pets_tool() -> list:
    """Retrieve all pets registered in Happy Paws Pet Hotel."""
    pets = list_pets()
    return [
        {
            "id": p[0],
            "name": p[1],
            "type": p[2],
            "breed": p[3],
            "age": p[4],
            "owner_name": p[5],
        }
        for p in pets
    ]

@mcp.tool()
def get_pet_details(pet_id: int) -> dict:
    """Get details of a specific pet by ID."""
    p = get_pet(pet_id)
    if not p:
        return {"error": f"Pet with ID {pet_id} not found"}
    return {
        "id": p[0],
        "name": p[1],
        "type": p[2],
        "breed": p[3],
        "age": p[4],
        "owner_name": p[5],
    }

@mcp.tool()
def register_new_pet(name: str, pet_type: str, breed: str, age: int, owner_name: str) -> dict:
    """Register a new pet in Happy Paws Pet Hotel."""
    pet_id = create_pet(name, pet_type, breed, age, owner_name)
    return {
        "status": "success",
        "pet_id": pet_id,
        "message": f"Pet '{name}' successfully registered",
    }

@mcp.tool()
def update_pet_info(
    pet_id: int,
    name: str,
    pet_type: str,
    breed: str,
    age: int,
    owner_name: str,
) -> dict:
    """Update existing pet information."""
    updated = update_pet_service(pet_id, name, pet_type, breed, age, owner_name)
    return {"status": "success", "rows_updated": updated}

@mcp.tool()
def remove_pet(pet_id: int) -> dict:
    """Delete a pet from the database."""
    deleted = delete_pet_service(pet_id)
    return {"status": "success", "rows_deleted": deleted}

@mcp.tool()
def list_available_rooms() -> list:
    """List all hotel rooms currently available for booking."""
    rooms = get_available_rooms()
    return [
        {
            "id": r[0],
            "room_number": r[1],
            "room_type": r[2],
            "daily_rate": float(r[3]),
            "status": r[4],
        }
        for r in rooms
    ]

@mcp.tool()
def book_pet_stay(pet_id: int, room_id: int, check_in: str, check_out: str) -> dict:
    """Book a room stay for a pet."""
    booking_id = book_room(pet_id, room_id, check_in, check_out)
    return {"status": "success", "booking_id": booking_id}

@mcp.tool()
def show_all_bookings() -> list:
    """Show all confirmed bookings."""
    bookings = list_bookings()
    return [
        {
            "id": b[0],
            "pet_name": b[1],
            "room_number": b[2],
            "check_in": str(b[3]),
            "check_out": str(b[4]),
            "status": b[5],
        }
        for b in bookings
    ]

if __name__ == "__main__":
    mcp.run()
