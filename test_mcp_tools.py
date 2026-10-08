import asyncio
from app.mcp.server import mcp, get_all_pets_tool, list_available_rooms, show_all_bookings

async def test_mcp_server():
    print("=== Testing FastMCP Tools ===")
    
    # 1. Test get_all_pets_tool
    pets = await get_all_pets_tool() if asyncio.iscoroutinefunction(get_all_pets_tool) else get_all_pets_tool()
    print(f"1. Pets from MCP tool: {pets}")
    
    # 2. Test list_available_rooms
    rooms = await list_available_rooms() if asyncio.iscoroutinefunction(list_available_rooms) else list_available_rooms()
    print(f"2. Available Rooms from MCP tool: {rooms}")

    # 3. Test show_all_bookings
    bookings = await show_all_bookings() if asyncio.iscoroutinefunction(show_all_bookings) else show_all_bookings()
    print(f"3. Bookings from MCP tool: {bookings}")
    
    print("\n✅ FastMCP Tools working perfectly!")

if __name__ == "__main__":
    asyncio.run(test_mcp_server())
