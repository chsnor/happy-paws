from app.database.connection import get_connection

def get_all_bookings():
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("""
        SELECT
            b.id,
            p.name,
            r.room_number,
            b.check_in,
            b.check_out,
            b.status
        FROM bookings b
        JOIN pets p ON b.pet_id = p.id
        JOIN rooms r ON b.room_id = r.id
        ORDER BY b.id
    """)
    bookings = cursor.fetchall()
    cursor.close()
    connection.close()
    return bookings

def get_booking_by_id(booking_id):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT id, pet_id, room_id, check_in, check_out, status FROM bookings WHERE id = ?", (booking_id,))
    booking = cursor.fetchone()
    cursor.close()
    connection.close()
    return booking

def create_booking(pet_id, room_id, check_in, check_out, status="confirmed"):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("""
        INSERT INTO bookings (pet_id, room_id, check_in, check_out, status)
        VALUES (?, ?, ?, ?, ?)
    """, (pet_id, room_id, check_in, check_out, status))
    connection.commit()
    booking_id = cursor.lastrowid
    cursor.close()
    connection.close()
    return booking_id

def cancel_booking(booking_id):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("UPDATE bookings SET status = 'cancelled' WHERE id = ?", (booking_id,))
    connection.commit()
    rows = cursor.rowcount
    cursor.close()
    connection.close()
    return rows
