from app.database.connection import get_connection

def get_all_bookings():
    connection = get_connection()
    try:
        cursor = connection.cursor()
        try:
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
            return cursor.fetchall()
        finally:
            cursor.close()
    finally:
        connection.close()

def get_booking_by_id(booking_id):
    connection = get_connection()
    try:
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT id, pet_id, room_id, check_in, check_out, status FROM bookings WHERE id = ?", (booking_id,))
            return cursor.fetchone()
        finally:
            cursor.close()
    finally:
        connection.close()

def create_booking(pet_id, room_id, check_in, check_out, status="confirmed"):
    connection = get_connection()
    try:
        cursor = connection.cursor()
        try:
            cursor.execute("""
                INSERT INTO bookings (pet_id, room_id, check_in, check_out, status)
                VALUES (?, ?, ?, ?, ?)
            """, (pet_id, room_id, check_in, check_out, status))
            booking_id = cursor.lastrowid
            connection.commit()
            return booking_id
        except Exception:
            connection.rollback()
            raise
        finally:
            cursor.close()
    finally:
        connection.close()

def cancel_booking(booking_id):
    connection = get_connection()
    try:
        cursor = connection.cursor()
        try:
            cursor.execute("UPDATE bookings SET status = 'cancelled' WHERE id = ?", (booking_id,))
            rows = cursor.rowcount
            connection.commit()
            return rows
        except Exception:
            connection.rollback()
            raise
        finally:
            cursor.close()
    finally:
        connection.close()

def delete_booking(booking_id):
    connection = get_connection()
    try:
        cursor = connection.cursor()
        try:
            cursor.execute("DELETE FROM bookings WHERE id = ?", (booking_id,))
            rows = cursor.rowcount
            connection.commit()
            return rows
        except Exception:
            connection.rollback()
            raise
        finally:
            cursor.close()
    finally:
        connection.close()
