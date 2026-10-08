# 🐾 Happy Paws Pet Hotel — Full-Stack AI Application with FastMCP & MariaDB

Full-Stack AI Application with FastMCP, MariaDB, and Docker for managing the Happy Paws Pet Hotel.

## 🏗️ Architecture

```
AI Assistant (FastMCP / Claude / Antigravity)
         │
         ▼
    FastMCP Server
         │
         ▼
   Service Layer (Business Logic & Validation)
         │
         ▼
  Repository Layer (SQL Queries)
         │
         ▼
MariaDB 11+ (Docker Container)
```

## 🚀 Quick Start

### 1. Start MariaDB in Docker
```powershell
docker compose up -d
```

### 2. Install Dependencies
```powershell
uv sync
```

### 3. Run and Verify the Full Application
```powershell
powershell -ExecutionPolicy Bypass -File .\run_project.ps1
```

### 4. Test FastMCP Tools for AI Integration
```powershell
powershell -ExecutionPolicy Bypass -File .\test_mcp.ps1
```

## 🛠️ Tech Stack
- **Database:** MariaDB 11+ in Docker
- **Backend:** Python 3.14+, uv, mariadb-connector
- **AI Integration:** FastMCP
- **Future Layers:** FastAPI (HTTP API), NiceGUI (Web UI)
