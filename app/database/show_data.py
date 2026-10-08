from app.database.connection import get_connection

def show_data():
    connection = get_connection()
    cursor = connection.cursor()

    print("\n=== PETS ===")
    cursor.execute("""
        SELECT id, name, type, breed, age, owner_name
        FROM pets
        ORDER BY id
    """)
    for pet in cursor.fetchall():
        print(pet)

    print("\n=== ROOMS ===")
    cursor.execute("""
        SELECT id, room_number, room_type, daily_rate, status
        FROM rooms
        ORDER BY id
    """)
    for room in cursor.fetchall():
        print(room)

    print("\n=== BOOKINGS ===")
    cursor.execute("""
        SELECT
            bookings.id,
            pets.name,
            rooms.room_number,
            bookings.check_in,
            bookings.check_out,
            bookings.status
        FROM bookings
        JOIN pets ON bookings.pet_id = pets.id
        JOIN rooms ON bookings.room_id = rooms.id
        ORDER BY bookings.id
    """)
    for booking in cursor.fetchall():
        print(booking)

    cursor.close()
    connection.close()

if __name__ == "__main__":
    show_data()
