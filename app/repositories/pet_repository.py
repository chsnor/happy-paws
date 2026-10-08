from app.database.connection import get_connection

# --------------------------------------------------
# 1. Get all pets
# --------------------------------------------------
def get_all_pets():
    connection = get_connection()
    try:
        cursor = connection.cursor()
        try:
            cursor.execute("""
                SELECT
                    id,
                    name,
                    type,
                    breed,
                    age,
                    owner_name
                FROM pets
                ORDER BY id
            """)
            pets = cursor.fetchall()
            return pets
        finally:
            cursor.close()
    finally:
        connection.close()


# --------------------------------------------------
# 2. Get one pet by ID
# --------------------------------------------------
def get_pet_by_id(pet_id):
    connection = get_connection()
    try:
        cursor = connection.cursor()
        try:
            cursor.execute(
                """
                SELECT
                    id,
                    name,
                    type,
                    breed,
                    age,
                    owner_name
                FROM pets
                WHERE id = ?
                """,
                (pet_id,),
            )
            pet = cursor.fetchone()
            return pet
        finally:
            cursor.close()
    finally:
        connection.close()


# --------------------------------------------------
# 3. Add a new pet
# --------------------------------------------------
def add_pet(name, pet_type, breed, age, owner_name):
    connection = get_connection()
    try:
        cursor = connection.cursor()
        try:
            cursor.execute(
                """
                INSERT INTO pets (
                    name,
                    type,
                    breed,
                    age,
                    owner_name
                )
                VALUES (?, ?, ?, ?, ?)
                """,
                (name, pet_type, breed, age, owner_name),
            )
            new_pet_id = cursor.lastrowid
            connection.commit()
            return new_pet_id
        except Exception:
            connection.rollback()
            raise
        finally:
            cursor.close()
    finally:
        connection.close()


# --------------------------------------------------
# 4. Update a pet
# --------------------------------------------------
def update_pet(
    pet_id,
    name,
    pet_type,
    breed,
    age,
    owner_name,
):
    connection = get_connection()
    try:
        cursor = connection.cursor()
        try:
            cursor.execute(
                """
                UPDATE pets
                SET
                    name = ?,
                    type = ?,
                    breed = ?,
                    age = ?,
                    owner_name = ?
                WHERE id = ?
                """,
                (
                    name,
                    pet_type,
                    breed,
                    age,
                    owner_name,
                    pet_id,
                ),
            )
            rows_updated = cursor.rowcount
            connection.commit()
            return rows_updated
        except Exception:
            connection.rollback()
            raise
        finally:
            cursor.close()
    finally:
        connection.close()


# --------------------------------------------------
# 5. Delete a pet
# --------------------------------------------------
def delete_pet(pet_id):
    connection = get_connection()
    try:
        cursor = connection.cursor()
        try:
            cursor.execute(
                """
                DELETE FROM pets
                WHERE id = ?
                """,
                (pet_id,),
            )
            rows_deleted = cursor.rowcount
            connection.commit()
            return rows_deleted
        except Exception:
            connection.rollback()
            raise
        finally:
            cursor.close()
    finally:
        connection.close()
