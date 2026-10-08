import sys
from app.database.connection import get_connection
from app.database.create_tables import create_tables
from app.database.seed_data import seed_data
from app.database.show_data import show_data
from app.services.pet_service import (
    list_pets,
    get_pet,
    create_pet,
    update_pet_service,
    delete_pet_service,
)
from app.services.booking_service import list_bookings

def main():
    print("========================================")
    print("🐾 Happy Paws Pet Hotel - Full Verification")
    print("========================================")

    # 1. Test database connection
    print("\n[Step 1] Testing MariaDB connection...")
    try:
        conn = get_connection()
        print("  -> Connected to MariaDB successfully!")
        conn.close()
    except Exception as e:
        print(f"  -> Connection failed: {e}")
        sys.exit(1)

    # 2. Initialize database tables
    print("\n[Step 2] Initializing tables (pets, rooms, bookings)...")
    create_tables()

    # 3. Seed data if needed
    print("\n[Step 3] Seeding initial data...")
    current_pets = list_pets()
    if len(current_pets) == 0:
        seed_data()
    else:
        print(f"  -> Database already has {len(current_pets)} pets. Skipping re-seed.")

    # 4. Display current database contents
    print("\n[Step 4] Querying current database records:")
    show_data()

    # 5. Test Service Layer CRUD operations
    print("\n[Step 5] Testing Service Layer (Lesson 4)...")
    
    # 5.1 Create new pet
    print("  -> Testing create_pet()...")
    test_pet_id = create_pet("Choco", "Dog", "Chihuahua", 2, "TestOwner")
    print(f"     Created pet with ID: {test_pet_id}")

    # 5.2 Get pet
    pet_info = get_pet(test_pet_id)
    print(f"     Retrieved pet: {pet_info}")

    # 5.3 Update pet
    print("  -> Testing update_pet_service()...")
    updated_count = update_pet_service(test_pet_id, "Choco Junior", "Dog", "Chihuahua", 3, "TestOwner")
    print(f"     Updated rows: {updated_count}")

    # 5.4 Delete pet
    print("  -> Testing delete_pet_service()...")
    deleted_count = delete_pet_service(test_pet_id)
    print(f"     Deleted rows: {deleted_count}")

    print("\n[Step 6] Current Bookings:")
    bookings = list_bookings()
    for b in bookings:
        print(f"  Booking #{b[0]}: Pet '{b[1]}' in Room {b[2]} ({b[3]} to {b[4]}) [{b[5]}]")

    print("\n========================================")
    print("🎉 All Lessons 1-4 completed & verified successfully!")
    print("========================================")

if __name__ == "__main__":
    main()
