from app.database.connection import get_connection

def get_all_rooms():
    connection = get_connection()
    try:
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT id, room_number, room_type, daily_rate, status FROM rooms ORDER BY id")
            return cursor.fetchall()
        finally:
            cursor.close()
    finally:
        connection.close()

def get_available_rooms():
    connection = get_connection()
    try:
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT id, room_number, room_type, daily_rate, status FROM rooms WHERE status = 'available' ORDER BY id")
            return cursor.fetchall()
        finally:
            cursor.close()
    finally:
        connection.close()

def get_room_by_id(room_id):
    connection = get_connection()
    try:
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT id, room_number, room_type, daily_rate, status FROM rooms WHERE id = ?", (room_id,))
            return cursor.fetchone()
        finally:
            cursor.close()
    finally:
        connection.close()

def update_room_status(room_id, status):
    connection = get_connection()
    try:
        cursor = connection.cursor()
        try:
            cursor.execute("UPDATE rooms SET status = ? WHERE id = ?", (status, room_id))
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
