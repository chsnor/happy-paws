# Happy Paws Full-Stack AI & MCP Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build the complete Happy Paws Pet Hotel application from Lessons 1-4 including MariaDB Docker setup, Database/Repository/Service layers, FastMCP AI server, and verification.

**Architecture:** A layered architecture with MariaDB containerized via Docker Compose, Python repository/service layers for clean separation of concerns, and FastMCP exposing pet hotel operations to AI assistants.

**Tech Stack:** Docker, MariaDB 11+, Python 3.11+, uv, mariadb-connector-python, python-dotenv, FastMCP.

---

### Task 1: Docker Compose & MariaDB Container Setup
**Files:**
- Create: `compose.yaml`
- Create: `.env`

- [ ] **Step 1: Create compose.yaml with MariaDB service**
- [ ] **Step 2: Create .env file with MariaDB credentials**
- [ ] **Step 3: Start Docker container using docker compose up -d**
- [ ] **Step 4: Verify MariaDB health & connectivity**

---

### Task 2: Project Dependencies & Database Layer
**Files:**
- Create: `pyproject.toml`
- Create: `app/database/__init__.py`
- Create: `app/database/connection.py`
- Create: `app/database/create_tables.py`
- Create: `app/database/seed_data.py`
- Create: `app/database/show_data.py`

- [ ] **Step 1: Initialize pyproject.toml with uv dependencies**
- [ ] **Step 2: Implement app/database/connection.py**
- [ ] **Step 3: Implement app/database/create_tables.py**
- [ ] **Step 4: Implement app/database/seed_data.py**
- [ ] **Step 5: Implement app/database/show_data.py**
- [ ] **Step 6: Run table creation and seeding**

---

### Task 3: Repository Layer
**Files:**
- Create: `app/repositories/__init__.py`
- Create: `app/repositories/pet_repository.py`
- Create: `app/repositories/room_repository.py`
- Create: `app/repositories/booking_repository.py`

- [ ] **Step 1: Implement pet_repository.py with full CRUD**
- [ ] **Step 2: Implement room_repository.py and booking_repository.py**
- [ ] **Step 3: Test repository functions**

---

### Task 4: Service Layer & Main Entrypoint
**Files:**
- Create: `app/services/__init__.py`
- Create: `app/services/pet_service.py`
- Create: `app/services/booking_service.py`
- Create: `main.py`

- [ ] **Step 1: Implement pet_service.py with business validations**
- [ ] **Step 2: Implement booking_service.py**
- [ ] **Step 3: Implement main.py demonstrating the complete workflow**
- [ ] **Step 4: Execute main.py and verify output**

---

### Task 5: FastMCP AI Server
**Files:**
- Create: `app/mcp/__init__.py`
- Create: `app/mcp/server.py`

- [ ] **Step 1: Implement FastMCP server with tools for pets, rooms, and bookings**
- [ ] **Step 2: Verify MCP server tools execution**
- [ ] **Step 3: Document how to connect AI assistants (Antigravity / Claude Code / Cline)**
