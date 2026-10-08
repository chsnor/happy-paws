# app/services/pet_service.py

# --------------------------------------------------
# 1. Import Repository Layer functions
# --------------------------------------------------
from app.repositories.pet_repository import (
    get_all_pets,
    get_pet_by_id,
    add_pet,
    update_pet,
    delete_pet,
)

# --------------------------------------------------
# 2. Get all pets through the Service Layer
# --------------------------------------------------
def list_pets():
    pets = get_all_pets()
    return pets

# --------------------------------------------------
# 3. Get one pet through the Service Layer
# --------------------------------------------------
def get_pet(pet_id):
    if not isinstance(pet_id, int) or pet_id <= 0:
        raise ValueError("Invalid pet_id: must be a positive integer")
    pet = get_pet_by_id(pet_id)
    return pet

# --------------------------------------------------
# 4. Add a pet through the Service Layer
# --------------------------------------------------
def create_pet(
    name,
    pet_type,
    breed,
    age,
    owner_name,
):
    if not name or not name.strip():
        raise ValueError("Pet name cannot be empty")
    if not pet_type or not pet_type.strip():
        raise ValueError("Pet type cannot be empty")
    if age is not None and age < 0:
        raise ValueError("Pet age cannot be negative")

    new_pet_id = add_pet(
        name.strip(),
        pet_type.strip(),
        breed.strip() if breed else None,
        age,
        owner_name.strip() if owner_name else None,
    )
    return new_pet_id

# --------------------------------------------------
# 5. Update a pet through the Service Layer
# --------------------------------------------------
def update_pet_service(
    pet_id,
    name,
    pet_type,
    breed,
    age,
    owner_name,
):
    if not isinstance(pet_id, int) or pet_id <= 0:
        raise ValueError("Invalid pet_id: must be a positive integer")
    if not name or not name.strip():
        raise ValueError("Pet name cannot be empty")
    if not pet_type or not pet_type.strip():
        raise ValueError("Pet type cannot be empty")

    rows_updated = update_pet(
        pet_id,
        name.strip(),
        pet_type.strip(),
        breed.strip() if breed else None,
        age,
        owner_name.strip() if owner_name else None,
    )
    return rows_updated

# --------------------------------------------------
# 6. Delete a pet through the Service Layer
# --------------------------------------------------
def delete_pet_service(pet_id):
    if not isinstance(pet_id, int) or pet_id <= 0:
        raise ValueError("Invalid pet_id: must be a positive integer")
    rows_deleted = delete_pet(pet_id)
    return rows_deleted
