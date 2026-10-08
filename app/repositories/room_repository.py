from app.database.connection import get_connection

def get_all_rooms():
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT id, room_number, room_type, daily_rate, status FROM rooms ORDER BY id")
    rooms = cursor.fetchall()
    cursor.close()
    connection.close()
    return rooms

def get_available_rooms():
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT id, room_number, room_type, daily_rate, status FROM rooms WHERE status = 'available' ORDER BY id")
    rooms = cursor.fetchall()
    cursor.close()
    connection.close()
    return rooms

def get_room_by_id(room_id):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT id, room_number, room_type, daily_rate, status FROM rooms WHERE id = ?", (room_id,))
    room = cursor.fetchone()
    cursor.close()
    connection.close()
    return room

def update_room_status(room_id, status):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("UPDATE rooms SET status = ? WHERE id = ?", (status, room_id))
    connection.commit()
    rows = cursor.rowcount
    cursor.close()
    connection.close()
    return rows
