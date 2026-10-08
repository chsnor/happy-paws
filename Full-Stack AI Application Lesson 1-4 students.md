docker exec -it happy_paws_db mariadb -u happyuser -phappypassword happy_paws



AI Application Architecture with MCP

Building a Full-Stack AI Application with FastMCP, FastAPI, NiceGUI, MariaDB, and Docker


A particularly important idea in this tutorial is that FastMCP, FastAPI, and NiceGUI are different interfaces that share the Service Layer, rather than each implementing the business logic separately. The document explicitly describes the Service Layer as the heart of the application.



| Lesson 1 — Architecture & Project Setup <br> Lesson 2 — MariaDB + Docker <br> Lesson 3 — Python + MariaDB <br> Lesson 4 — Service Layer <br> Lesson 5 — FastAPI <br> Lesson 6 — NiceGUI <br> Lesson 7 — Our FastMCP <br> Lesson 8 — MariaDB MCP Server <br> Lesson 9 — Our FastMCP vs MariaDB MCP <br> Lesson 10 — Connect the AI Assistant <br> Lesson 11 — Docker Compose Integration <br> Lesson 12 — Security & Safe AI Access <br> Lesson 13 — Final Integrated Mini Project |
| --- |




| AI Assistant              Software                 Human <br> │                       │                       │ <br> ┌────┴────┐                  │                       │ <br> ▼         ▼                  ▼                       ▼ <br> Our FastMCP   MariaDB MCP        FastAPI                 NiceGUI <br> │           Server              │                       │ <br> │             │                 │                       │ <br> │             │                 │                       │ <br> └─────────────│─────────────────┼───────────────────────┘ <br> │                 │ <br> │          Service Layer <br> │                 │ <br> │                 ▼ <br> │         Repository Layer <br> │                 │ <br> │                 ▼ <br> └──────────────► MariaDB |
| --- |




AI Application Architecture with MCP


| Lesson 1 — Architecture & Project Setup <br> Step 1 — Understand the Target Architecture       ◄── YOU ARE HERE <br> Step 2 — Understand the Role of Each Technology <br> Step 3 — Create the Project with uv <br> Step 4 — Create the Virtual Environment <br> Step 5 — Install the Initial Packages <br> Step 6 — Create the Basic Application <br> Step 7 — Create the Project Structure <br> Step 8 — Run and Verify the Lesson 1 Project |
| --- |



Step 1 of 8 — Understand the Target Architecture


| AI Assistant              Software                 Human <br> │                       │                       │ <br> ┌────┴────┐                  │                       │ <br> ▼         ▼                  ▼                       ▼ <br> Our FastMCP   MariaDB MCP        FastAPI                 NiceGUI <br> │           Server              │                       │ <br> │             │                 │                       │ <br> │             │                 │                       │ <br> └─────────────│─────────────────┼───────────────────────┘ <br> │                 │ <br> │          Service Layer <br> │                 │ <br> │                 ▼ <br> │         Repository Layer <br> │                 │ <br> │                 ▼ <br> └──────────────► MariaDB |
| --- |



Lesson 1 — Step 3 of 8— Create the Project with uvNiceGUI

| 🐾 Happy Paws Pet Hotel <br> Pets <br> -------------------------------- <br> 🐶 Milo       Dog <br> 🐱 Luna       Cat <br> 🐶 Coco       Dog <br> [ Add Pet ] <br> Rooms <br> -------------------------------- <br> Room 1        Available <br> Room 2        Occupied <br> [ New Booking ] |
| --- |



Service Layer — Shared Application Logic

This is the heart of our application.


| get_all_pets() <br> get_pet() <br> add_pet() <br> get_available_rooms() <br> create_booking() <br> cancel_booking() |
| --- |



Lesson 1 — Architecture & Project Setup

Step 3 of 8 — Create the Project with uv


PS C:\> cd alongkot_299

PS C:\alongkot_299> uv init happy-paws





Lesson 1 — Architecture & Project Setup

Step 4 of 8 — Create the Virtual Environment with uv


| Lesson 1 — Architecture & Project Setup <br> Step 1 of 8 — Understand the Target Architecture        ✅ <br> Step 2 of 8 — Understand the Role of Each Technology    ✅ <br> Step 3 of 8 — Create the Project with uv                 ✅ <br> Step 4 of 8 — Create the Virtual Environment   ◄── YOU ARE HERE <br> Step 5 of 8 — Install the Initial Packages <br> Step 6 of 8 — Create the Basic Application <br> Step 7 of 8 — Create the Project Structure <br> Step 8 of 8 — Run and Verify the Lesson 1 Project |
| --- |



PS C:\alongkot_299> cd happy-paws

PS C:\alongkot_299\happy-paws> uv venv

| happy-paws/ <br> │ <br> ├── .venv/          ◄── Virtual environment <br> ├── main.py <br> ├── pyproject.toml <br> └── ... |
| --- |




PS C:\alongkot_299\happy-paws> .venv\Scripts\Activate.ps1

(happy-paws) PS C:\alongkot_299\happy-paws>

(happy-paws) C:\alongkot_299\happy-paws>uv run python main.py

Hello from happy-paws!Hello from happy-paws!




Lesson 1 — Architecture & Project Setup

Step 5 of 8 — Install the Initial Packages with uv


(happy-paws) PS C:\alongkot_299\happy-paws> uv add fastapi uvicorn nicegui fastmcp


(happy-paws) PS C:\alongkot_299\happy-paws> uv add mariadb






Each package corresponds to part of our architecture:

| fastmcp <br> │ <br> └── AI Assistant ↔ MCP <br> fastapi <br> │ <br> └── Software ↔ HTTP API <br> uvicorn <br> │ <br> └── Runs our FastAPI web server <br> nicegui <br> │ <br> └── Human ↔ User Interface <br> mariadb <br> │ <br> └── Python ↔ MariaDB |
| --- |





Quick test

(happy-paws) PS C:\alongkot_299\happy-paws> uv run python -c "import fastapi, fastmcp, nicegui, mariadb; print('Happy Paws packages OK!')"

Happy Paws packages OK!




Lesson 1 — Architecture & Project Setup

Step 6 of 8 — Create the Basic Application


| Lesson 1 — Architecture & Project Setup <br> Step 1 of 8 — Understand the Target Architecture        ✅ <br> Step 2 of 8 — Understand the Role of Each Technology    ✅ <br> Step 3 of 8 — Create the Project with uv                 ✅ <br> Step 4 of 8 — Create the Virtual Environment             ✅ <br> Step 5 of 8 — Install the Initial Packages               ✅ <br> Step 6 of 8 — Create the Basic Application               ◄── YOU ARE HERE <br> Step 7 of 8 — Create the Project Structure <br> Step 8 of 8 — Run and Verify the Lesson 1 Project |
| --- |


main.py

def main():

    print("🐾 Happy Paws Pet Hotel")

    print("AI Application Architecture with MCP")

    print("Project is running successfully!")


if __name__ == "__main__":

    main()


(happy-paws) PS C:\alongkot_299\happy-paws> uv run main.py

🐾 Happy Paws Pet Hotel

AI Application Architecture with MCP

Project is running successfully!



Lesson 1 — Architecture & Project Setup

Step 7 of 8 — Create the Project Structure


| Lesson 1 — Architecture & Project Setup <br> Step 1 of 8 — Understand the Target Architecture        ✅ <br> Step 2 of 8 — Understand the Role of Each Technology    ✅ <br> Step 3 of 8 — Create the Project with uv                 ✅ <br> Step 4 of 8 — Create the Virtual Environment             ✅ <br> Step 5 of 8 — Install the Initial Packages               ✅ <br> Step 6 of 8 — Create the Basic Application               ✅ <br> Step 7 of 8 — Create the Project Structure               ◄── YOU ARE HERE <br> Step 8 of 8 — Run and Verify the Lesson 1 Project |
| --- |


create this project structure:

| happy-paws/ <br> │ <br> ├── app/ <br> │   │ <br> │   ├── database/ <br> │   │ <br> │   ├── repositories/ <br> │   │ <br> │   ├── services/ <br> │   │ <br> │   ├── api/ <br> │   │ <br> │   ├── mcp/ <br> │   │ <br> │   └── ui/ <br> │ <br> ├── main.py <br> ├── pyproject.toml <br> ├── README.md <br> └── .venv/ |
| --- |




Lesson 1 — Architecture & Project Setup

Step 8 of 8 — Run and Verify the Lesson 1 Project


| Lesson 1 — Architecture & Project Setup <br> Step 1 of 8 — Understand the Target Architecture        ✅ <br> Step 2 of 8 — Understand the Role of Each Technology    ✅ <br> Step 3 of 8 — Create the Project with uv                 ✅ <br> Step 4 of 8 — Create the Virtual Environment             ✅ <br> Step 5 of 8 — Install the Initial Packages               ✅ <br> Step 6 of 8 — Create the Basic Application               ✅ <br> Step 7 of 8 — Create the Project Structure               ✅ <br> Step 8 of 8 — Run and Verify the Lesson 1 Project        ◄── YOU ARE HERE |
| --- |






Lesson 1 — Architecture & Project Setup

Lesson 2 — MariaDB + Docker

Lesson 3 — Python + MariaDB

Lesson 4 — Service Layer

Lesson 5 — FastAPI

Lesson 6 — NiceGUI

Lesson 7 — Our FastMCP

Lesson 8 — MariaDB MCP Server

Lesson 9 — Our FastMCP vs MariaDB MCP

Lesson 10 — Connect the AI Assistant

Lesson 11 — Docker Compose Integration

Lesson 12 — Security & Safe AI Access

Lesson 13 — Final Integrated Mini Project


Lesson 2 — MariaDB + Docker

Step 1 of 10 Understand MariaDB and Docker


| Step 1 of 10  Understand MariaDB and Docker  ◄── YOU ARE HERE <br> Step 2 of 10  Create the Docker Compose File <br> Step 3 of 10  Start MariaDB with Docker <br> Step 4 of 10  Check the MariaDB Container <br> Step 5 of 10  Connect to MariaDB <br> Step 6 of 10  Create the Happy Paws Database <br> Step 7 of 10  Create the pets Table <br> Step 8 of 10  Create the rooms Table <br> Step 9 of 10  Create the bookings Table <br> Step 10 of 10 Insert and Verify Sample Data |
| --- |



The tutorial uses three main tables:

| pets <br> ├── Milo <br> ├── Luna <br> └── Coco <br> rooms <br> ├── Room 101 <br> ├── Room 102 <br> └── Room 103 <br> bookings <br> ├── Which pet? <br> ├── Which room? <br> └── Which dates? |
| --- |


Lesson 2 — MariaDB + Docker

Step 2 of 10 Create the Docker Compose File

| Step 1 of 10  Understand MariaDB and Docker          ✅ <br> Step 2 of 10  Create the Docker Compose File  ◄── YOU ARE HERE <br> Step 3 of 10  Start MariaDB with Docker <br> Step 4 of 10  Check the MariaDB Container <br> Step 5 of 10  Connect to MariaDB <br> Step 6 of 10  Create the Happy Paws Database <br> Step 7 of 10  Create the pets Table <br> Step 8 of 10  Create the rooms Table <br> Step 9 of 10  Create the bookings Table <br> Step 10 of 10 Insert and Verify Sample Data |
| --- |


(happy-paws) PS C:\alongkot_299\happy-paws> ni compose.yaml

services:

  mariadb:

    image: mariadb:latest


    container_name: happy_paws_db


    environment:

      MARIADB_ROOT_PASSWORD: rootpassword

      MARIADB_DATABASE: happy_paws

      MARIADB_USER: happyuser

      MARIADB_PASSWORD: happypassword


    ports:

      - "3333:3306"


    volumes:

      - happy_paws_data:/var/lib/mysql

volumes:

  happy_paws_data:


Lesson 2 — MariaDB + Docker

Step 3 of 10 Start MariaDB with Docker 


| Lesson 2 — MariaDB + Docker <br> Step 1 of 10  Understand MariaDB and Docker          ✅ <br> Step 2 of 10  Create the Docker Compose File         ✅ <br> Step 3 of 10  Start MariaDB with Docker    ◄── YOU ARE HERE <br> Step 4 of 10  Check the MariaDB Container <br> Step 5 of 10  Connect to MariaDB <br> Step 6 of 10  Create the Happy Paws Database <br> Step 7 of 10  Create the pets Table <br> Step 8 of 10  Create the rooms Table <br> Step 9 of 10  Create the bookings Table <br> Step 10 of 10 Insert and Verify Sample Data |
| --- |


Make Sure Docker Desktop Is Running


(happy-paws) PS C:\alongkot_299\happy-paws> docker compose up -d





Lesson 2 — MariaDB + Docker

Step 4 of 10 Check the MariaDB Container


| Step 1 of 10  Understand MariaDB and Docker          ✅ <br> Step 2 of 10  Create the Docker Compose File         ✅ <br> Step 3 of 10  Start MariaDB with Docker              ✅ <br> Step 4 of 10  Check the MariaDB Container   ◄── YOU ARE HERE <br> Step 5 of 10  Connect to MariaDB <br> Step 6 of 10  Create the Happy Paws Database <br> Step 7 of 10  Create the pets Table <br> Step 8 of 10  Create the rooms Table <br> Step 9 of 10  Create the bookings Table <br> Step 10 of 10 Insert and Verify Sample Data |
| --- |


(happy-paws) PS C:\alongkot_299\happy-paws> docker ps

CONTAINER ID   IMAGE            COMMAND                  CREATED         STATUS         PORTS                                         NAMES

ed880097f38d   mariadb:latest   "docker-entrypoint.s…"   7 minutes ago   Up 7 minutes   0.0.0.0:3333->3306/tcp, [::]:3333->3306/tcp   happy_paws_db


(happy-paws) PS C:\alongkot_299\happy-paws> docker compose logs mariadb


(happy-paws) PS C:\alongkot_299\happy-paws> docker exec -it happy_paws_db mariadb -u happyuser -phappypassword happy_paws

Welcome to the MariaDB monitor.  Commands end with ; or \g.

Your MariaDB connection id is 3

Server version: 12.3.3-MariaDB-ubu2404 mariadb.org binary distribution


Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

MariaDB [happy_paws]>



MariaDB [happy_paws]> show tables;

Empty set (0.000 sec)


MariaDB [happy_paws]> show databases;

+--------------------+

| Database           |

+--------------------+

| happy_paws         |

| information_schema |

+--------------------+

MariaDB [happy_paws]> exit;

Bye

At this point, Docker and MariaDB are working correctly.



Lesson 2 — MariaDB + Docker

Step 5 of 10 Connect to MariaDB

| Step 1 of 10  Understand MariaDB and Docker          ✅ <br> Step 2 of 10  Create the Docker Compose File         ✅ <br> Step 3 of 10  Start MariaDB with Docker              ✅ <br> Step 4 of 10  Check the MariaDB Container            ✅ <br> Step 5 of 10  Connect to MariaDB                     ◄── YOU ARE HERE <br> Step 6 of 10  Select and Verify Happy Paws Database <br> Step 7 of 10  Create the pets Table <br> Step 8 of 10  Create the rooms Table <br> Step 9 of 10  Create the bookings Table <br> Step 10 of 10 Insert and Verify Sample Data |
| --- |


(happy-paws) PS C:\alongkot_299\happy-paws> docker exec -it happy_paws_db mariadb -u happyuser -phappypassword happy_paws 

Welcome to the MariaDB monitor.  Commands end with ; or \g.

Your MariaDB connection id is 4

Server version: 13.0.2-MariaDB-ubu2604 mariadb.org binary distribution




Lesson 2 — MariaDB + Docker

Step 6 of 10 Select and Verify Happy Paws Database


| Step 1 of 10  Understand MariaDB and Docker          ✅ <br> Step 2 of 10  Create the Docker Compose File         ✅ <br> Step 3 of 10  Start MariaDB with Docker              ✅ <br> Step 4 of 10  Check the MariaDB Container            ✅ <br> Step 5 of 10  Connect to MariaDB                     ✅ <br> Step 6 of 10  Select and Verify Happy Paws Database  ◄── YOU HERE <br> Step 7 of 10  Create the pets Table <br> Step 8 of 10  Create the rooms Table <br> Step 9 of 10  Create the bookings Table <br> Step 10 of 10 Insert and Verify Sample Data |
| --- |


MariaDB [happy_paws]> select database();

+------------+

| database() |

+------------+

| happy_paws |

+------------+

1 row in set (0.003 sec)


MariaDB [happy_paws]> select user();

+---------------------+

| user()              |

+---------------------+

| happyuser@localhost |

+---------------------+

1 row in set (0.001 sec)



MariaDB [happy_paws]> system clear


MariaDB [happy_paws]> show tables;

Empty set (0.001 sec)


MariaDB [happy_paws]> exit

Bye



Lesson 2 — MariaDB + Docker

Step 7 of 10 Create Python Database Connection

| Step 1 of 10  Understand MariaDB and Docker                ✅ <br> Step 2 of 10  Create the Docker Compose File               ✅ <br> Step 3 of 10  Start MariaDB with Docker                    ✅ <br> Step 4 of 10  Check the MariaDB Container                  ✅ <br> Step 5 of 10  Connect to MariaDB                           ✅ <br> Step 6 of 10  Select and Verify Happy Paws Database        ✅ <br> Step 7 of 10  Create Python Database Connection            ◄── YOU ARE HERE <br> Step 8 of 10  Create Database Tables and Relationships <br> Step 9 of 10  Insert Sample Data <br> Step 10 of 10 Query and Verify the Database |
| --- |



| .env <br> │ <br> │ database settings <br> ▼ <br> connection.py <br> │ <br> │ get_connection() <br> ▼ <br> MariaDB <br> │ <br> ▼ <br> happy_paws |
| --- |


(happy-paws) PS C:\alongkot_299\happy-paws> uv add python-dotenv

(happy-paws) PS C:\alongkot_299\happy-paws> ni .env

DB_HOST=localhost

DB_PORT=3333

DB_USER=happyuser

DB_PASSWORD=happypassword

DB_NAME=happy_paws


Add .env to .gitignore


Modify connection.py

import os


import mariadb

from dotenv import load_dotenv

# 1. Load variables from the .env file

load_dotenv()

def get_connection():

    # 2. Create and return a MariaDB connection

    return mariadb.connect(

        host=os.getenv("DB_HOST"),

        port=int(os.getenv("DB_PORT")),

        user=os.getenv("DB_USER"),

        password=os.getenv("DB_PASSWORD"),

        database=os.getenv("DB_NAME"),

    )


main.py

from app.database.connection import get_connection

def main():

    print("🐾 Happy Paws Pet Hotel")

    connection = get_connection()

    print("Connected to MariaDB successfully!")

    connection.close()


if __name__ == "__main__":

    main()

(happy-paws) PS C:\alongkot_299\happy-paws> uv run python main.py

🐾 Happy Paws Pet Hotel

Connected to MariaDB successfully!



Lesson 2 — MariaDB + Docker

Step 8 of 10 Create the Database Tables 

| Step 1 of 10  Understand MariaDB and Docker                ✅ <br> Step 2 of 10  Create the Docker Compose File               ✅ <br> Step 3 of 10  Start MariaDB with Docker                    ✅ <br> Step 4 of 10  Check the MariaDB Container                  ✅ <br> Step 5 of 10  Connect to MariaDB                           ✅ <br> Step 6 of 10  Select and Verify Happy Paws Database        ✅ <br> Step 7 of 10  Create Python Database Connection            ✅ <br> Step 8 of 10  Create the Database Tables and Relationships ◄── YOU ARE HERE <br> Step 9 of 10  Insert Sample Data <br> Step 10 of 10 Query and Verify the Database |
| --- |


**+-------------+       +-------------+       +-------------+**

**|    pets     |       ****|  bookings****   |       |    rooms    |**

**+-------------+       +-------------+       +-------------+**

**| PK id       | 1   M | PK id       | M   1 | PK id       |**

**| name        |------<| FK ****pet_id****   |       | ****room_number**** |**

**| type        |       | FK ****room_****id****  |****>------| ****room_type****   |**

**+-------------+       | ****check_in****    |       | status      |**

**                      | ****check_out****   |       +-------------+**

**                      ****+-****------------+**


(happy-paws) PS C:\alongkot_299\happy-paws> ni app\database\create_tables.py 

from app.database.connection import get_connection


def create_tables():

    # 1. Connect to MariaDB

    connection = get_connection()

    cursor = connection.cursor()


    # 2. Create pets table

    cursor.execute("""

        CREATE TABLE IF NOT EXISTS pets (

            id INT AUTO_INCREMENT PRIMARY KEY,

            name VARCHAR(100) NOT NULL,

            type VARCHAR(50) NOT NULL,

            breed VARCHAR(100),

            age INT,

            owner_name VARCHAR(100)

        )

    """)


    # 3. Create rooms table

    cursor.execute("""

        CREATE TABLE IF NOT EXISTS rooms (

            id INT AUTO_INCREMENT PRIMARY KEY,

            room_number VARCHAR(20) NOT NULL UNIQUE,

            room_type VARCHAR(50) NOT NULL,

            daily_rate DECIMAL(10, 2) NOT NULL,

            status VARCHAR(20) NOT NULL

        )

    """)


    # 4. Create bookings table

    cursor.execute("""

        CREATE TABLE IF NOT EXISTS bookings (

            id INT AUTO_INCREMENT PRIMARY KEY,

            pet_id INT NOT NULL,

            room_id INT NOT NULL,

            check_in DATE NOT NULL,

            check_out DATE NOT NULL,

            status VARCHAR(20) NOT NULL,


            FOREIGN KEY (pet_id)

                REFERENCES pets(id),


            FOREIGN KEY (room_id)

                REFERENCES rooms(id)

        )

    """)


    # 5. Save changes

    connection.commit()


    # 6. Close resources

    cursor.close()

    connection.close()


    print("pets, rooms, and bookings tables created successfully!")


if __name__ == "__main__":

    create_tables()

(happy-paws) PS C:\alongkot_299\happy-paws> uv run python -m app.database.create_tables

pets, rooms, and bookings tables created successfully!

(happy-paws) PS C:\alongkot_299\happy-paws> docker exec -it happy_paws_db mariadb -u happyuser -phappypassword happy_paws


MariaDB [happy_paws]> show tables;

+----------------------+

| Tables_in_happy_paws |

+----------------------+

| bookings             |

| pets                 |

| rooms                |

+----------------------+

3 rows in set (0.001 sec)


MariaDB [happy_paws]> system clear

MariaDB [happy_paws]> describe pets;

+------------+--------------+------+-----+---------+----------------+

| Field      | Type         | Null | Key | Default | Extra          |

+------------+--------------+------+-----+---------+----------------+

| id         | int(11)      | NO   | PRI | NULL    | auto_increment |

| name       | varchar(100) | NO   |     | NULL    |                |

| type       | varchar(50)  | NO   |     | NULL    |                |

| breed      | varchar(100) | YES  |     | NULL    |                |

| age        | int(11)      | YES  |     | NULL    |                |

| owner_name | varchar(100) | YES  |     | NULL    |                |

+------------+--------------+------+-----+---------+----------------+

6 rows in set (0.015 sec)


MariaDB [happy_paws]> describe rooms;

+-------------+---------------+------+-----+---------+----------------+

| Field       | Type          | Null | Key | Default | Extra          |

+-------------+---------------+------+-----+---------+----------------+

| id          | int(11)       | NO   | PRI | NULL    | auto_increment |

| room_number | varchar(20)   | NO   | UNI | NULL    |                |

| room_type   | varchar(50)   | NO   |     | NULL    |                |

| daily_rate  | decimal(10,2) | NO   |     | NULL    |                |

| status      | varchar(20)   | NO   |     | NULL    |                |

+-------------+---------------+------+-----+---------+----------------+

5 rows in set (0.005 sec)


MariaDB [happy_paws]> describe bookings;

+-----------+-------------+------+-----+---------+----------------+

| Field     | Type        | Null | Key | Default | Extra          |

+-----------+-------------+------+-----+---------+----------------+

| id        | int(11)     | NO   | PRI | NULL    | auto_increment |

| pet_id    | int(11)     | NO   | MUL | NULL    |                |

| room_id   | int(11)     | NO   | MUL | NULL    |                |

| check_in  | date        | NO   |     | NULL    |                |

| check_out | date        | NO   |     | NULL    |                |

| status    | varchar(20) | NO   |     | NULL    |                |

+-----------+-------------+------+-----+---------+----------------+

6 rows in set (0.003 sec)


MariaDB [happy_paws]>



Lesson 2 — MariaDB + Docker

Step 9 of 10 Insert Sample Data


| Lesson 1 — Architecture & Project Setup <br> Lesson 2 — MariaDB + Docker <br> Lesson 3 — Python + MariaDB <br> Lesson 4 — Service Layer <br> Lesson 5 — FastAPI <br> Lesson 6 — NiceGUI <br> Lesson 7 — Our FastMCP <br> Lesson 8 — MariaDB MCP Server <br> Lesson 9 — Our FastMCP vs MariaDB MCP <br> Lesson 10 — Connect the AI Assistant <br> Lesson 11 — Docker Compose Integration <br> Lesson 12 — Security & Safe AI Access <br> Lesson 13 — Final Integrated Mini Project |
| --- |


| Step 1 of 10  Understand MariaDB and Docker                ✅ <br> Step 2 of 10  Create the Docker Compose File               ✅ <br> Step 3 of 10  Start MariaDB with Docker                    ✅ <br> Step 4 of 10  Check the MariaDB Container                  ✅ <br> Step 5 of 10  Connect to MariaDB                           ✅ <br> Step 6 of 10  Select and Verify Happy Paws Database        ✅ <br> Step 7 of 10  Create Python Database Connection            ✅ <br> Step 8 of 10  Create Database Tables and Relationships     ✅ <br> Step 9 of 10  Insert Sample Data                           ◄── YOU ARE HERE <br> Step 10 of 10 Query and Verify the Database |
| --- |


| pets <br> Milo   Dog   Golden Retriever   3   Somchai <br> Luna   Cat   British Shorthair  2   Nok <br> Coco   Dog   Poodle             4   Mali <br> rooms <br> 101   Standard   500.00   available <br> 102   Deluxe     800.00   occupied <br> 103   Deluxe     800.00   available |
| --- |





(happy-paws) PS C:\alongkot_299\happy-paws> ni app\database\seed_data.py

from app.database.connection import get_connection


def seed_data():

    # 1. Connect to MariaDB

    connection = get_connection()

    cursor = connection.cursor()


    # --------------------------------------------------

    # 2. Insert pets

    # --------------------------------------------------

    pets = [

        ("Milo", "Dog", "Golden Retriever", 3, "Somchai"),

        ("Luna", "Cat", "British Shorthair", 2, "Nok"),

        ("Coco", "Dog", "Poodle", 4, "Mali"),

    ]


    cursor.executemany(

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

        pets,

    )


    # --------------------------------------------------

    # 3. Insert rooms

    # --------------------------------------------------

    rooms = [

        ("101", "Standard", 500.00, "available"),

        ("102", "Deluxe", 800.00, "occupied"),

        ("103", "Deluxe", 800.00, "available"),

    ]


    cursor.executemany(

        """

        INSERT INTO rooms (

            room_number,

            room_type,

            daily_rate,

            status

        )

        VALUES (?, ?, ?, ?)

        """,

        rooms,

    )


    # --------------------------------------------------

    # 4. Get IDs we need for bookings

    # --------------------------------------------------

    cursor.execute(

        "SELECT id FROM pets WHERE name = ?",

        ("Milo",),

    )

    milo_id = cursor.fetchone()[0]


    cursor.execute(

        "SELECT id FROM pets WHERE name = ?",

        ("Luna",),

    )

    luna_id = cursor.fetchone()[0]


    cursor.execute(

        "SELECT id FROM rooms WHERE room_number = ?",

        ("102",),

    )

    room_102_id = cursor.fetchone()[0]


    cursor.execute(

        "SELECT id FROM rooms WHERE room_number = ?",

        ("101",),

    )

    room_101_id = cursor.fetchone()[0]


    # --------------------------------------------------

    # 5. Insert bookings

    # --------------------------------------------------

    bookings = [

        (

            milo_id,

            room_102_id,

            "2026-09-27",

            "2026-09-30",

            "confirmed",

        ),

        (

            luna_id,

            room_101_id,

            "2026-10-01",

            "2026-10-03",

            "confirmed",

        ),

    ]


    cursor.executemany(

        """

        INSERT INTO bookings (

            pet_id,

            room_id,

            check_in,

            check_out,

            status

        )

        VALUES (?, ?, ?, ?, ?)

        """,

        bookings,

    )


    # 6. Save everything

    connection.commit()


    # 7. Close resources

    cursor.close()

    connection.close()


    print("Sample data inserted successfully!")


if __name__ == "__main__":

    seed_data()


| pets <br> id   name <br> 1    Milo <br> 2    Luna <br> rooms <br> id   room_number <br> 1    101 <br> 2    102 |
| --- |


(happy-paws) PS C:\alongkot_299\happy-paws> uv run python -m app.database.seed_data

Sample data inserted successfully!


| happy_paws <br> │ <br> ├── pets <br> │   ├── Milo <br> │   ├── Luna <br> │   └── Coco <br> │ <br> ├── rooms <br> │   ├── 101 <br> │   ├── 102 <br> │   └── 103 <br> │ <br> └── bookings <br> ├── Milo → Room 102 <br> └── Luna → Room 101 |
| --- |



Lesson 2 — MariaDB + Docker

Step 10 of 10 Query and Verify the Database


| Lesson 1 — Architecture & Project Setup <br> Lesson 2 — MariaDB + Docker <br> Lesson 3 — Python + MariaDB <br> Lesson 4 — Service Layer <br> Lesson 5 — FastAPI <br> Lesson 6 — NiceGUI <br> Lesson 7 — Our FastMCP <br> Lesson 8 — MariaDB MCP Server <br> Lesson 9 — Our FastMCP vs MariaDB MCP <br> Lesson 10 — Connect the AI Assistant <br> Lesson 11 — Docker Compose Integration <br> Lesson 12 — Security & Safe AI Access <br> Lesson 13 — Final Integrated Mini Project |
| --- |


| Step 1 of 10  Understand MariaDB and Docker                ✅ <br> Step 2 of 10  Create the Docker Compose File               ✅ <br> Step 3 of 10  Start MariaDB with Docker                    ✅ <br> Step 4 of 10  Check the MariaDB Container                  ✅ <br> Step 5 of 10  Connect to MariaDB                           ✅ <br> Step 6 of 10  Select and Verify Happy Paws Database        ✅ <br> Step 7 of 10  Create Python Database Connection            ✅ <br> Step 8 of 10  Create Database Tables and Relationships     ✅ <br> Step 9 of 10  Insert Sample Data                           ✅ <br> Step 10 of 10 Query and Verify the Database                ◄── YOU ARE HERE |
| --- |


(happy-paws) PS C:\alongkot_299\happy-paws> ni app\database\show_data.py

from app.database.connection import get_connection


def show_data():

    # 1. Connect to MariaDB

    connection = get_connection()

    cursor = connection.cursor()


    # --------------------------------------------------

    # 2. Show pets

    # --------------------------------------------------

    print("\n=== PETS ===")


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


    for pet in pets:

        print(pet)


    # --------------------------------------------------

    # 3. Show rooms

    # --------------------------------------------------

    print("\n=== ROOMS ===")


    cursor.execute("""

        SELECT

            id,

            room_number,

            room_type,

            daily_rate,

            status

        FROM rooms

        ORDER BY id

    """)


    rooms = cursor.fetchall()


    for room in rooms:

        print(room)


    # --------------------------------------------------

    # 4. Show bookings with pet and room information

    # --------------------------------------------------

    print("\n=== BOOKINGS ===")


    cursor.execute("""

        SELECT

            bookings.id,

            pets.name,

            rooms.room_number,

            bookings.check_in,

            bookings.check_out,

            bookings.status

        FROM bookings

        JOIN pets

            ON bookings.pet_id = pets.id

        JOIN rooms

            ON bookings.room_id = rooms.id

        ORDER BY bookings.id

    """)


    bookings = cursor.fetchall()


    for booking in bookings:

        print(booking)


    # 5. Close resources

    cursor.close()

    connection.close()


if __name__ == "__main__":

    show_data()




| app/ <br> └── database/ <br> ├── __init__.py <br> ├── connection.py <br> ├── create_tables.py <br> ├── seed_data.py <br> └── show_data.py       ◄── NEW |
| --- |


(happy-paws) PS C:\alongkot_299\happy-paws> uv run python -m app.database.show_data


=== PETS ===

(1, 'Milo', 'Dog', 'Golden Retriever', 3, 'Somchai')

(2, 'Luna', 'Cat', 'British Shorthair', 2, 'Nok')

(3, 'Coco', 'Dog', 'Poodle', 4, 'Mali')


=== ROOMS ===

(1, '101', 'Standard', Decimal('500.00'), 'available')

(2, '102', 'Deluxe', Decimal('800.00'), 'occupied')

(3, '103', 'Deluxe', Decimal('800.00'), 'available')


=== BOOKINGS ===

(1, 'Milo', '102', datetime.date(2026, 9, 27), datetime.date(2026, 9, 30), 'confirmed')

(2, 'Luna', '101', datetime.date(2026, 10, 1), datetime.date(2026, 10, 3), 'confirmed')

(happy-paws) PS C:\alongkot_299\happy-paws> 


| connection.py      → connect to MariaDB <br> create_tables.py   → create the schema <br> seed_data.py       → insert sample data <br> show_data.py       → query and verify data |
| --- |



Lesson 3 — Python + MariaDB  


| AI Assistant              Software                 Human <br> │                       │                       │ <br> ┌────┴────┐                  │                       │ <br> ▼         ▼                  ▼                       ▼ <br> Our FastMCP   MariaDB MCP        FastAPI                 NiceGUI <br> │           Server              │                       │ <br> │             │                 │                       │ <br> │             │                 │                       │ <br> └─────────────│─────────────────┼───────────────────────┘ <br> │                 │ <br> │          Service Layer <br> │                 │ <br> │                 ▼ <br> │         Repository Layer <br> │                 │ <br> │                 ▼ <br> └──────────────► MariaDB |
| --- |


Now we can build a proper Repository Layer.

the main job of the Repository Layer is: Talk to the database

It also keeps the database code separate from business logic


SQL belongs in the Repository Layer 


| Lesson 1 — Architecture & Project Setup <br> Lesson 2 — MariaDB + Docker <br> Lesson 3 — Python + MariaDB <br> Lesson 4 — Service Layer <br> Lesson 5 — FastAPI <br> Lesson 6 — NiceGUI <br> Lesson 7 — Our FastMCP <br> Lesson 8 — MariaDB MCP Server <br> Lesson 9 — Our FastMCP vs MariaDB MCP <br> Lesson 10 — Connect the AI Assistant <br> Lesson 11 — Docker Compose Integration <br> Lesson 12 — Security & Safe AI Access <br> Lesson 13 — Final Integrated Mini Project |
| --- |


| Step 1 of 8  Create the Pet Repository          ◄── YOU ARE HERE <br> Step 2 of 8  Read All Pets <br> Step 3 of 8  Read One Pet by ID <br> Step 4 of 8  Add a New Pet <br> Step 5 of 8  Update a Pet <br> Step 6 of 8  Delete a Pet <br> Step 7 of 8  Test All CRUD Operations <br> Step 8 of 8  Review the Database Layer |
| --- |


Step 1 of 8 Create the Pet Repository

| Future Service Layer <br> │ <br> ▼ <br> +--------------------+ <br> \| Repository Layer   \|  ◄── WE ARE HERE <br> \| pet_repository.py  \| <br> +--------------------+ <br> │ <br> ▼ <br> connection.py <br> │ <br> ▼ <br> MariaDB |
| --- |

The repository's job is simple:

Put database SQL operations in one dedicated place.

Later, FastAPI, NiceGUI, and FastMCP will not need to write SQL themselves.



| app/ <br> ├── database/ <br> │   ├── connection.py <br> │   ├── create_tables.py <br> │   ├── seed_data.py <br> │   └── show_data.py <br> │ <br> └── repositories/ <br> └── pet_repository.py     ◄── NEW |
| --- |


(happy-paws) PS C:\alongkot_299\happy-paws> ni app\repositories\__init__.py

(happy-paws) PS C:\alongkot_299\happy-paws> ni app\repositories\pet_repository.py

from app.database.connection import get_connection


def get_all_pets():

    # 1. Connect to MariaDB

    connection = get_connection()

    cursor = connection.cursor()


    # 2. Query the pets table

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


    # 3. Get all rows

    pets = cursor.fetchall()


    # 4. Close database resources

    cursor.close()

    connection.close()


    # 5. Return the pets

    return pets




Lesson 3 — Python + MariaDB

Step 2 of 8 Read All Pets


| Lesson 1 — Architecture & Project Setup <br> Lesson 2 — MariaDB + Docker <br> Lesson 3 — Python + MariaDB <br> Lesson 4 — Service Layer <br> Lesson 5 — FastAPI <br> Lesson 6 — NiceGUI <br> Lesson 7 — Our FastMCP <br> Lesson 8 — MariaDB MCP Server <br> Lesson 9 — Our FastMCP vs MariaDB MCP <br> Lesson 10 — Connect the AI Assistant <br> Lesson 11 — Docker Compose Integration <br> Lesson 12 — Security & Safe AI Access <br> Lesson 13 — Final Integrated Mini Project |
| --- |


| Lesson 3 — Python + MariaDB <br> Step 1 of 8  Create the Pet Repository          ✅ <br> Step 2 of 8  Read All Pets                      ◄── YOU ARE HERE <br> Step 3 of 8  Read One Pet by ID <br> Step 4 of 8  Add a New Pet <br> Step 5 of 8  Update a Pet <br> Step 6 of 8  Delete a Pet <br> Step 7 of 8  Test All CRUD Operations <br> Step 8 of 8  Review the Database Layer |
| --- |



pet_repository.py

from app.database.connection import get_connection


def get_all_pets():

    # 1. Connect to MariaDB

    connection = get_connection()

    cursor = connection.cursor()


    # 2. Query the pets table

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


    # 3. Get all rows

    pets = cursor.fetchall()


    # 4. Close database resources

    cursor.close()

    connection.close()


    # 5. Return the pets

    return pets


main.py

from app.repositories.pet_repository import get_all_pets


def main():

    print("🐾 Happy Paws Pet Hotel")

    print("------------------------")


    # Get all pets from the repository

    pets = get_all_pets()


    # Display each pet

    for pet in pets:

        print(pet)


if __name__ == "__main__":

    main()


(happy-paws) PS C:\alongkot_299\happy-paws> uv run python main.py                        

🐾 Happy Paws Pet Hotel         

------------------------

(1, 'Milo', 'Dog', 'Golden Retriever', 3, 'Somchai')

(2, 'Luna', 'Cat', 'British Shorthair', 2, 'Nok')

(3, 'Coco', 'Dog', 'Poodle', 4, 'Mali')




Lesson 3 — Python + MariaDB

Step 3 of 8 Read One Pet by ID


| Step 1 of 8  Create the Pet Repository          ✅ <br> Step 2 of 8  Read All Pets                      ✅ <br> Step 3 of 8  Read One Pet by ID       ── YOU ARE HERE <br> Step 4 of 8  Add a New Pet <br> Step 5 of 8  Update a Pet <br> Step 6 of 8  Delete a Pet <br> Step 7 of 8  Test All CRUD Operations <br> Step 8 of 8  Review the Database Layer |
| --- |


pet_repository.py

from app.database.connection import get_connection


def get_all_pets():

    connection = get_connection()

    cursor = connection.cursor()


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


    cursor.close()

    connection.close()


    return pets


def get_pet_by_id(pet_id):

    # 1. Connect to MariaDB

    connection = get_connection()

    cursor = connection.cursor()


    # 2. Find one pet by ID

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


    # 3. Get one row

    pet = cursor.fetchone()


    # 4. Close database resources

    cursor.close()

    connection.close()


    # 5. Return the pet

    return pet


main.py

from app.repositories.pet_repository import get_pet_by_id


def main():

    print("🐾 Happy Paws Pet Hotel")

    print("------------------------")


    pet = get_pet_by_id(2)


    print(pet)


if __name__ == "__main__":

    main()



(happy-paws) PS C:\alongkot_299\happy-paws> uv run python main.py

🐾 Happy Paws Pet Hotel

------------------------

(2, 'Luna', 'Cat', 'British Shorthair', 2, 'Nok')


Lesson 3 — Python + MariaDB

Step 4 of 8 Add a New Pet


| Step 1 of 8  Create the Pet Repository          ✅ <br> Step 2 of 8  Read All Pets                      ✅ <br> Step 3 of 8  Read One Pet by ID                 ✅ <br> Step 4 of 8  Add a New Pet                      ◄── YOU ARE HERE <br> Step 5 of 8  Update a Pet <br> Step 6 of 8  Delete a Pet <br> Step 7 of 8  Test All CRUD Operations <br> Step 8 of 8  Review the Database Layer |
| --- |


pet_repository.py

from app.database.connection import get_connection


# --------------------------------------------------

# 1. Get all pets

# --------------------------------------------------

def get_all_pets():

    connection = get_connection()

    cursor = connection.cursor()


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


    cursor.close()

    connection.close()


    return pets


# --------------------------------------------------

# 2. Get one pet by ID

# --------------------------------------------------

def get_pet_by_id(pet_id):

    connection = get_connection()

    cursor = connection.cursor()


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


    cursor.close()

    connection.close()


    return pet


# --------------------------------------------------

# 3. Add a new pet

# --------------------------------------------------

def add_pet(name, pet_type, breed, age, owner_name):

    connection = get_connection()

    cursor = connection.cursor()


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


    connection.commit()


    new_pet_id = cursor.lastrowid


    cursor.close()

    connection.close()


    return new_pet_id


main.py

from app.repositories.pet_repository import add_pet


def main():

    print("🐾 Happy Paws Pet Hotel")

    print("------------------------")


    new_pet_id = add_pet(

        "Buddy",

        "Dog",

        "Beagle",

        2,

        "Anan",

    )


    print(f"New pet added with ID: {new_pet_id}")


if __name__ == "__main__":

    main()





Lesson 3 — Python + MariaDB

Step 5 of 8 Update a Pet


| Lesson 1 — Architecture & Project Setup <br> Lesson 2 — MariaDB + Docker <br> Lesson 3 — Python + MariaDB <br> Lesson 4 — Service Layer <br> Lesson 5 — FastAPI <br> Lesson 6 — NiceGUI <br> Lesson 7 — Our FastMCP <br> Lesson 8 — MariaDB MCP Server <br> Lesson 9 — Our FastMCP vs MariaDB MCP <br> Lesson 10 — Connect the AI Assistant <br> Lesson 11 — Docker Compose Integration <br> Lesson 12 — Security & Safe AI Access <br> Lesson 13 — Final Integrated Mini Project |
| --- |


| Step 1 of 8  Create the Pet Repository          ✅ <br> Step 2 of 8  Read All Pets                      ✅ <br> Step 3 of 8  Read One Pet by ID                 ✅ <br> Step 4 of 8  Add a New Pet                      ✅ <br> Step 5 of 8  Update a Pet                       ◄── YOU ARE HERE <br> Step 6 of 8  Delete a Pet <br> Step 7 of 8  Test All CRUD Operations <br> Step 8 of 8  Review the Database Layer |
| --- |


pet_repository.py

from app.database.connection import get_connection


# --------------------------------------------------

# 1. Get all pets

# --------------------------------------------------

def get_all_pets():

    connection = get_connection()

    cursor = connection.cursor()


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


    cursor.close()

    connection.close()


    return pets


# --------------------------------------------------

# 2. Get one pet by ID

# --------------------------------------------------

def get_pet_by_id(pet_id):

    connection = get_connection()

    cursor = connection.cursor()


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


    cursor.close()

    connection.close()


    return pet


# --------------------------------------------------

# 3. Add a new pet

# --------------------------------------------------

def add_pet(name, pet_type, breed, age, owner_name):

    connection = get_connection()

    cursor = connection.cursor()


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


    connection.commit()


    new_pet_id = cursor.lastrowid


    cursor.close()

    connection.close()


    return new_pet_id


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

    cursor = connection.cursor()


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


    connection.commit()


    rows_updated = cursor.rowcount


    cursor.close()

    connection.close()


    return rows_updated


main.py

from app.repositories.pet_repository import update_pet


def main():

    print("🐾 Happy Paws Pet Hotel")

    print("------------------------")


    rows_updated = update_pet(

        4,

        "Buddy",

        "Dog",

        "Beagle",

        3,

        "Anan",

    )


    print(f"Rows updated: {rows_updated}")


if __name__ == "__main__":

    main()




Lesson 3 — Python + MariaDB

Step 6 of 8 Delete a Pet


| Lesson 1 — Architecture & Project Setup <br> Lesson 2 — MariaDB + Docker <br> Lesson 3 — Python + MariaDB <br> Lesson 4 — Service Layer <br> Lesson 5 — FastAPI <br> Lesson 6 — NiceGUI <br> Lesson 7 — Our FastMCP <br> Lesson 8 — MariaDB MCP Server <br> Lesson 9 — Our FastMCP vs MariaDB MCP <br> Lesson 10 — Connect the AI Assistant <br> Lesson 11 — Docker Compose Integration <br> Lesson 12 — Security & Safe AI Access <br> Lesson 13 — Final Integrated Mini Project |
| --- |


| Step 1 of 8  Create the Pet Repository          ✅ <br> Step 2 of 8  Read All Pets                      ✅ <br> Step 3 of 8  Read One Pet by ID                 ✅ <br> Step 4 of 8  Add a New Pet                      ✅ <br> Step 5 of 8  Update a Pet                       ✅ <br> Step 6 of 8  Delete a Pet                       ◄── YOU ARE HERE <br> Step 7 of 8  Test All CRUD Operations <br> Step 8 of 8  Review the Database Layer |
| --- |


(happy-paws) PS C:\alongkot_299\happy-paws> uv run python -m app.database.show_data


pet_repository.py

from app.database.connection import get_connection


# --------------------------------------------------

# 1. Get all pets

# --------------------------------------------------

def get_all_pets():

    connection = get_connection()

    cursor = connection.cursor()


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


    cursor.close()

    connection.close()


    return pets


# --------------------------------------------------

# 2. Get one pet by ID

# --------------------------------------------------

def get_pet_by_id(pet_id):

    connection = get_connection()

    cursor = connection.cursor()


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


    cursor.close()

    connection.close()


    return pet


# --------------------------------------------------

# 3. Add a new pet

# --------------------------------------------------

def add_pet(name, pet_type, breed, age, owner_name):

    connection = get_connection()

    cursor = connection.cursor()


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


    connection.commit()


    new_pet_id = cursor.lastrowid


    cursor.close()

    connection.close()


    return new_pet_id


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

    cursor = connection.cursor()


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


    connection.commit()


    rows_updated = cursor.rowcount


    cursor.close()

    connection.close()


    return rows_updated


# --------------------------------------------------

# 5. Delete a pet

# --------------------------------------------------

def delete_pet(pet_id):

    connection = get_connection()

    cursor = connection.cursor()


    cursor.execute(

        """

        DELETE FROM pets

        WHERE id = ?

        """,

        (pet_id,),

    )


    connection.commit()


    rows_deleted = cursor.rowcount


    cursor.close()

    connection.close()


    return rows_deleted


main.py

from app.repositories.pet_repository import delete_pet


def main():

    print("🐾 Happy Paws Pet Hotel")

    print("------------------------")


    rows_deleted = delete_pet(4)


    print(f"Rows deleted: {rows_deleted}")


if __name__ == "__main__":

    main()




Lesson 3 — Python + MariaDB

Step 7 of 8 Test All CRUD Operations


| Lesson 1 — Architecture & Project Setup <br> Lesson 2 — MariaDB + Docker <br> Lesson 3 — Python + MariaDB <br> Lesson 4 — Service Layer <br> Lesson 5 — FastAPI <br> Lesson 6 — NiceGUI <br> Lesson 7 — Our FastMCP <br> Lesson 8 — MariaDB MCP Server <br> Lesson 9 — Our FastMCP vs MariaDB MCP <br> Lesson 10 — Connect the AI Assistant <br> Lesson 11 — Docker Compose Integration <br> Lesson 12 — Security & Safe AI Access <br> Lesson 13 — Final Integrated Mini Project |
| --- |


| Step 1 of 8  Create the Pet Repository          ✅ <br> Step 2 of 8  Read All Pets                      ✅ <br> Step 3 of 8  Read One Pet by ID                 ✅ <br> Step 4 of 8  Add a New Pet                      ✅ <br> Step 5 of 8  Update a Pet                       ✅ <br> Step 6 of 8  Delete a Pet                       ✅ <br> Step 7 of 8  Test All CRUD Operations           ◄── YOU ARE HERE <br> Step 8 of 8  Review the Database Layer |
| --- |


**docker exec -it ****happy_paws_db**** ****mariadb**** -u ****happyuser**** -****phappypassword**** ****happy_paws**

(happy-paws) PS C:\alongkot_299\happy-paws> ni test_pet_repository


test_pet_repository.py

from app.repositories.pet_repository import (

    get_all_pets,

    get_pet_by_id,

    add_pet,

    update_pet,

    delete_pet,

)


print("=== CREATE ===")


pet_id = add_pet(

    name="Mochi",

    pet_type="Dog",

    breed="Shiba Inu",

    age=3,

    owner_name="Alongkot",

)


print("Created pet ID:", pet_id)


print("\n=== READ ONE ===")


pet = get_pet_by_id(pet_id)


print(pet)


print("\n=== UPDATE ===")


rows_updated = update_pet(

    pet_id,

    name="Mochi",

    pet_type="Dog",

    breed="Shiba Inu",

    age=4,

    owner_name="Alongkot",

)


print("Rows updated:", rows_updated)


print("\n=== READ AFTER UPDATE ===")


pet = get_pet_by_id(pet_id)


print(pet)


print("\n=== READ ALL ===")


pets = get_all_pets()


for pet in pets:

    print(pet)


print("\n=== DELETE ===")


rows_deleted = delete_pet(pet_id)


print("Rows deleted:", rows_deleted)


print("\n=== VERIFY DELETE ===")


pet = get_pet_by_id(pet_id)


print("Pet after delete:", pet)


(happy-paws) PS C:\alongkot_299\happy-paws> uv run python test_pet_repository.py

=== CREATE ===

Created pet ID: 5


=== READ ONE ===

(5, 'Mochi', 'Dog', 'Shiba Inu', 3, 'Alongkot')


=== UPDATE ===

Rows updated: 0


=== READ AFTER UPDATE ===

(5, 'Mochi', 'Dog', 'Shiba Inu', 4, 'Alongkot')


=== READ ALL ===

(1, 'Milo', 'Dog', 'Golden Retriever', 3, 'Somchai')

(2, 'Luna', 'Cat', 'British Shorthair', 2, 'Nok')

(3, 'Coco', 'Dog', 'Poodle', 4, 'Mali')

(5, 'Mochi', 'Dog', 'Shiba Inu', 4, 'Alongkot')


=== DELETE ===

Rows deleted: 0


=== VERIFY DELETE ===

Pet after delete: None




Lesson 4 — Service Layer

Step 1 of 8 Create the Pet Service

| Lesson 1 — Architecture & Project Setup <br> Lesson 2 — MariaDB + Docker <br> Lesson 3 — Python + MariaDB <br> Lesson 4 — Service Layer <br> Lesson 5 — FastAPI <br> Lesson 6 — NiceGUI <br> Lesson 7 — Our FastMCP <br> Lesson 8 — MariaDB MCP Server <br> Lesson 9 — Our FastMCP vs MariaDB MCP <br> Lesson 10 — Connect the AI Assistant <br> Lesson 11 — Docker Compose Integration <br> Lesson 12 — Security & Safe AI Access <br> Lesson 13 — Final Integrated Mini Project |
| --- |


| Step 1 of 8  Create the Pet Service <br> Step 2 of 8  Get All Pets Through the Service <br> Step 3 of 8  Get One Pet Through the Service <br> Step 4 of 8  Add a Pet Through the Service <br> Step 5 of 8  Update a Pet Through the Service <br> Step 6 of 8  Delete a Pet Through the Service <br> Step 7 of 8  Add Business Rules <br> Step 8 of 8  Review the Service Layer |
| --- |


| FastAPI       NiceGUI       FastMCP <br> │             │             │ <br> └─────────────┼─────────────┘ <br> │ <br> ▼ <br> Service Layer        ◄── WE ARE HERE <br> │ <br> ▼ <br> Repository Layer <br> │ <br> ▼ <br> MariaDB |
| --- |

(happy-paws2) PS C:\alongkot_299\happy-paws2> ni app\services\__init__.py

(happy-paws2) PS C:\alongkot_299\happy-paws2> ni app\services\pet_service.py


| app/ <br> │ <br> ├── database/ <br> │   └── connection.py <br> │ <br> ├── repositories/ <br> │   ├── __init__.py <br> │   └── pet_repository.py <br> │ <br> └── services/ <br> ├── __init__.py <br> └── pet_service.py        ◄── NEW |
| --- |


pet_service.py

# Import a function from the Repository Layer

# get_all_pets is a FUNCTION

from app.repositories.pet_repository import get_all_pets


# This is a FUNCTION in the Service Layer

def list_pets():

    # Call the Repository Layer function

    pets = get_all_pets()


    # Return the result to whoever called the Service Layer

    return pets




Lesson 4 — Service Layer

Step 2 of 8 Get All Pets Through the Service


| Lesson 1 — Architecture & Project Setup <br> Lesson 2 — MariaDB + Docker <br> Lesson 3 — Python + MariaDB <br> Lesson 4 — Service Layer <br> Lesson 5 — FastAPI <br> Lesson 6 — NiceGUI <br> Lesson 7 — Our FastMCP <br> Lesson 8 — MariaDB MCP Server <br> Lesson 9 — Our FastMCP vs MariaDB MCP <br> Lesson 10 — Connect the AI Assistant <br> Lesson 11 — Docker Compose Integration <br> Lesson 12 — Security & Safe AI Access <br> Lesson 13 — Final Integrated Mini Project |
| --- |


| Step 1 of 8  Create the Pet Service                 ✅ <br> Step 2 of 8  Get All Pets Through the Service       ◄── YOU ARE HERE <br> Step 3 of 8  Get One Pet Through the Service <br> Step 4 of 8  Add a Pet Through the Service <br> Step 5 of 8  Update a Pet Through the Service <br> Step 6 of 8  Delete a Pet Through the Service <br> Step 7 of 8  Add Business Rules <br> Step 8 of 8  Review the Service Layer |
| --- |


The Service Layer does not contain SQL.

The Repository Layer contains the SQL.



pet_service.py

# IMPORT STATEMENT:

# Import the repository function into the Service Layer.

from app.repositories.pet_repository import get_all_pets


# FUNCTION DEFINITION:

# list_pets() is a Service Layer function.

def list_pets():


    # FUNCTION CALL:

    # Call the Repository Layer function.

    pets = get_all_pets()


    # VARIABLE:

    # pets stores the rows returned from MariaDB.


    # RETURN STATEMENT:

    # Send the result back to the caller.

    return pets



main.py

# IMPORT STATEMENT:

# Import list_pets() from the Service Layer.

from app.services.pet_service import list_pets


# FUNCTION DEFINITION:

# main() is our program's main function.

def main():


    # FUNCTION CALL:

    # print() displays text in the terminal.

    print("🐾 Happy Paws Pet Hotel")

    print("------------------------")


    # FUNCTION CALL:

    # list_pets() asks the Service Layer for all pets.

    #

    # VARIABLE:

    # pets stores the returned list of database rows.

    pets = list_pets()


    # FOR LOOP:

    # Go through each pet returned by the Service Layer.

    for pet in pets:


        # VARIABLE:

        # pet represents one row from the pets table.

        print(pet)


# SPECIAL PYTHON VARIABLE:

# __name__ tells Python how this file is being executed.

if __name__ == "__main__":


    # FUNCTION CALL:

    # Start our program.

    main()




(happy-paws2) PS C:\alongkot_299\happy-paws2> uv run python main.py

🐾 Happy Paws Pet Hotel

------------------------

(1, 'maew', 'thai', 'thai', 3, 'Dang')



Or 



| (happy-paws2) C:\alongkot_299\happy-paws2>docker exec -it happy_paws_db mariadb -u happyuser -phappypassword happy_paws <br> ariaDB [happy_paws]> select * from pets; <br> +----+------+------+-------+------+------------+ <br> \| id \| name \| type \| breed \| age  \| owner_name \| <br> +----+------+------+-------+------+------------+ <br> \|  1 \| maew \| thai \| thai  \|    3 \| Dang       \| <br> +----+------+------+-------+------+------------+ <br> 1 row in set (0.001 sec) |
| --- |


Lesson 4 — Service Layer

Step 3 of 8 Get One Pet Through the Service



| AI Assistant              Software                 Human <br> │                       │                       │ <br> ┌────┴────┐                  │                       │ <br> ▼         ▼                  ▼                       ▼ <br> Our FastMCP   MariaDB MCP        FastAPI                 NiceGUI <br> │           Server              │                       │ <br> │             │                 │                       │ <br> │             │                 │                       │ <br> └─────────────│─────────────────┼───────────────────────┘ <br> │                 │ <br> │          Service Layer <br> │                 │ <br> │                 ▼ <br> │         Repository Layer <br> │                 │ <br> │                 ▼ <br> └──────────────► MariaDB |
| --- |




| Lesson 1 — Architecture & Project Setup <br> Lesson 2 — MariaDB + Docker <br> Lesson 3 — Python + MariaDB <br> Lesson 4 — Service Layer <br> Lesson 5 — FastAPI <br> Lesson 6 — NiceGUI <br> Lesson 7 — Our FastMCP <br> Lesson 8 — MariaDB MCP Server <br> Lesson 9 — Our FastMCP vs MariaDB MCP <br> Lesson 10 — Connect the AI Assistant <br> Lesson 11 — Docker Compose Integration <br> Lesson 12 — Security & Safe AI Access <br> Lesson 13 — Final Integrated Mini Project |
| --- |


| Step 1 of 8  Create the Pet Service                 ✅ <br> Step 2 of 8  Get All Pets Through the Service       ✅ <br> Step 3 of 8  Get One Pet Through the Service        ◄── YOU ARE HERE <br> Step 4 of 8  Add a Pet Through the Service <br> Step 5 of 8  Update a Pet Through the Service <br> Step 6 of 8  Delete a Pet Through the Service <br> Step 7 of 8  Add Business Rules <br> Step 8 of 8  Review the Service Layer |
| --- |


| main.py <br> │ <br> ▼ <br> Service Layer <br> get_pet() <br> │ <br> ▼ <br> Repository Layer <br> get_pet_by_id() <br> │ <br> ▼ <br> MariaDB |
| --- |




pet_service.py

# app/services/pet_service.py


# --------------------------------------------------

# 1. Import Repository Layer functions

# --------------------------------------------------


# IMPORT STATEMENT:

# Import functions from pet_repository.py.

#

# get_all_pets

# → FUNCTION

# → gets all pets from the database

#

# get_pet_by_id

# → FUNCTION

# → gets one pet from the database by ID

from app.repositories.pet_repository import (

    get_all_pets,

    get_pet_by_id,

)


# --------------------------------------------------

# 2. Get all pets through the Service Layer

# --------------------------------------------------


# FUNCTION DEFINITION:

# list_pets() is a Service Layer function.

def list_pets():


    # FUNCTION CALL:

    # Call the Repository Layer.

    pets = get_all_pets()


    # RETURN STATEMENT:

    # Return the pets to the caller.

    return pets


# --------------------------------------------------

# 3. Get one pet through the Service Layer

# --------------------------------------------------


# FUNCTION DEFINITION:

# get_pet() is a Service Layer function.

#

# pet_id

# → PARAMETER

# → receives the ID of the pet we want

def get_pet(pet_id):


    # FUNCTION CALL:

    # Call the Repository Layer function.

    #

    # pet_id

    # → ARGUMENT

    #

    # pet

    # → VARIABLE

    # → stores the returned pet row

    pet = get_pet_by_id(pet_id)


    # RETURN STATEMENT:

    # Return the pet to whoever called get_pet().

    return pet



main.py

# main.py


# --------------------------------------------------

# 1. Import service function

# --------------------------------------------------


# get_pet

# → FUNCTION imported from the Service Layer

from app.services.pet_service import get_pet


# --------------------------------------------------

# 2. Choose a pet ID

# --------------------------------------------------


# pet_id

# → VARIABLE

pet_id = 1


# --------------------------------------------------

# 3. Ask the Service Layer for the pet

# --------------------------------------------------


# get_pet()

# → FUNCTION CALL

#

# pet_id

# → ARGUMENT

pet = get_pet(pet_id)


# --------------------------------------------------

# 4. Display the result

# --------------------------------------------------


print(pet)



(happy-paws2) PS C:\alongkot_299\happy-paws2> uv run python main.py

(1, 'maew', 'thai', 'thai', 3, 'Dang')



Lesson 4 — Service Layer

Step 4 of 8 — Add a Pet Through the Service


| Lesson 1 — Architecture & Project Setup <br> Lesson 2 — MariaDB + Docker <br> Lesson 3 — Python + MariaDB <br> Lesson 4 — Service Layer <br> Lesson 5 — FastAPI <br> Lesson 6 — NiceGUI <br> Lesson 7 — Our FastMCP <br> Lesson 8 — MariaDB MCP Server <br> Lesson 9 — Our FastMCP vs MariaDB MCP <br> Lesson 10 — Connect the AI Assistant <br> Lesson 11 — Docker Compose Integration <br> Lesson 12 — Security & Safe AI Access <br> Lesson 13 — Final Integrated Mini Project |
| --- |


| Step 1 of 8  Create the Pet Service                  ✅ <br> Step 2 of 8  Get All Pets Through the Service        ✅ <br> Step 3 of 8  Get One Pet Through the Service         ✅ <br> Step 4 of 8  Add a Pet Through the Service           ◄── YOU ARE HERE <br> Step 5 of 8  Update a Pet Through the Service <br> Step 6 of 8  Delete a Pet Through the Service <br> Step 7 of 8  Add Business Rules <br> Step 8 of 8  Review the Service Layer |
| --- |


| main.py <br> │ <br> ▼ <br> Service Layer <br> add_pet_service() <br> │ <br> ▼ <br> Repository Layer <br> add_pet() <br> │ <br> ▼ <br> MariaDB |
| --- |

pet_service.py

# app/services/pet_service.py


# --------------------------------------------------

# 1. Import Repository Layer functions

# --------------------------------------------------


# IMPORT STATEMENT:

# Import functions from pet_repository.py.

#

# get_all_pets

# → FUNCTION

#

# get_pet_by_id

# → FUNCTION

#

# add_pet

# → FUNCTION

from app.repositories.pet_repository import (

    get_all_pets,

    get_pet_by_id,

    add_pet,

)


# --------------------------------------------------

# 2. Get all pets through the Service Layer

# --------------------------------------------------


# FUNCTION DEFINITION:

# list_pets() is a Service Layer function.

def list_pets():


    # FUNCTION CALL:

    # Call the Repository Layer.

    pets = get_all_pets()


    # RETURN STATEMENT:

    return pets


# --------------------------------------------------

# 3. Get one pet through the Service Layer

# --------------------------------------------------


# FUNCTION DEFINITION:

# get_pet() is a Service Layer function.

#

# pet_id

# → PARAMETER

def get_pet(pet_id):


    # FUNCTION CALL:

    # Call the Repository Layer.

    pet = get_pet_by_id(pet_id)


    # RETURN STATEMENT:

    return pet


# --------------------------------------------------

# 4. Add a pet through the Service Layer

# --------------------------------------------------


# FUNCTION DEFINITION:

# create_pet() is a Service Layer function.

#

# name, pet_type, breed, age, owner_name

# → PARAMETERS

def create_pet(name, pet_type, breed, age, owner_name):


    # FUNCTION CALL:

    # Call the Repository Layer's add_pet() function.

    #

    # name, pet_type, breed, age, owner_name

    # → ARGUMENTS

    #

    # new_pet_id

    # → VARIABLE

    # → stores the ID of the newly created pet

    new_pet_id = add_pet(

        name,

        pet_type,

        breed,

        age,

        owner_name,

    )


    # RETURN STATEMENT:

    # Return the new pet ID to the caller.

    return new_pet_id



main.py 

# main.py


# --------------------------------------------------

# 1. Import Service Layer function

# --------------------------------------------------


# IMPORT STATEMENT:

# Import create_pet() from pet_service.py.

from app.services.pet_service import create_pet


# --------------------------------------------------

# 2. Main function

# --------------------------------------------------


# FUNCTION DEFINITION:

# main() is our program's main function.

def main():


    print("🐾 Happy Paws Pet Hotel")

    print("------------------------")


    # FUNCTION CALL:

    # Ask the Service Layer to create a new pet.

    #

    # The values below are ARGUMENTS.

    #

    # new_pet_id

    # → VARIABLE

    # → stores the ID returned by create_pet()

    new_pet_id = create_pet(

        "Buddy",

        "Dog",

        "Beagle",

        2,

        "Anan",

    )


    # FUNCTION CALL:

    # Display the new pet ID.

    print(f"New pet added with ID: {new_pet_id}")


# --------------------------------------------------

# 3. Run the program

# --------------------------------------------------


if __name__ == "__main__":

    main()


(happy-paws2) PS C:\alongkot_299\happy-paws2> uv run python main.py

🐾 Happy Paws Pet Hotel

------------------------

New pet added with ID: 2




Lesson 4 — Service Layer

Step 5 of 8 — Update a Pet Through the Service


| Lesson 1 — Architecture & Project Setup <br> Lesson 2 — MariaDB + Docker <br> Lesson 3 — Python + MariaDB <br> Lesson 4 — Service Layer <br> Lesson 5 — FastAPI <br> Lesson 6 — NiceGUI <br> Lesson 7 — Our FastMCP <br> Lesson 8 — MariaDB MCP Server <br> Lesson 9 — Our FastMCP vs MariaDB MCP <br> Lesson 10 — Connect the AI Assistant <br> Lesson 11 — Docker Compose Integration <br> Lesson 12 — Security & Safe AI Access <br> Lesson 13 — Final Integrated Mini Project |
| --- |


| Step 1 of 8  Create the Pet Service                  ✅ <br> Step 2 of 8  Get All Pets Through the Service        ✅ <br> Step 3 of 8  Get One Pet Through the Service         ✅ <br> Step 4 of 8  Add a Pet Through the Service           ✅ <br> Step 5 of 8  Update a Pet Through the Service        ◄── YOU ARE HERE <br> Step 6 of 8  Delete a Pet Through the Service <br> Step 7 of 8  Add Business Rules <br> Step 8 of 8  Review the Service Layer |
| --- |


| main.py <br> │ <br> ▼ <br> Service Layer <br> update_pet_service() <br> │ <br> ▼ <br> Repository Layer <br> update_pet() <br> │ <br> ▼ <br> MariaDB |
| --- |


pet_service.py

# app/services/pet_service.py


# --------------------------------------------------

# 1. Import Repository Layer functions

# --------------------------------------------------


# IMPORT STATEMENT:

# Import functions from pet_repository.py.

#

# get_all_pets

# → FUNCTION in the Repository Layer

#

# get_pet_by_id

# → FUNCTION in the Repository Layer

#

# add_pet

# → FUNCTION in the Repository Layer

#

# update_pet

# → FUNCTION in the Repository Layer

from app.repositories.pet_repository import (

    get_all_pets,

    get_pet_by_id,

    add_pet,

    update_pet,

)


# --------------------------------------------------

# 2. Get all pets through the Service Layer

# --------------------------------------------------


# FUNCTION DEFINITION:

# list_pets() is a Service Layer function.

def list_pets():


    # FUNCTION CALL:

    # Call get_all_pets() in the Repository Layer.

    #

    # pets

    # → VARIABLE

    # → stores all pet rows returned from MariaDB

    pets = get_all_pets()


    # RETURN STATEMENT:

    # Return all pets to the caller.

    return pets


# --------------------------------------------------

# 3. Get one pet through the Service Layer

# --------------------------------------------------


# FUNCTION DEFINITION:

# get_pet() is a Service Layer function.

#

# pet_id

# → PARAMETER

# → identifies which pet we want

def get_pet(pet_id):


    # FUNCTION CALL:

    # Call get_pet_by_id() in the Repository Layer.

    #

    # pet_id

    # → ARGUMENT

    #

    # pet

    # → VARIABLE

    # → stores one pet row returned from MariaDB

    pet = get_pet_by_id(pet_id)


    # RETURN STATEMENT:

    # Return the pet to the caller.

    return pet


# --------------------------------------------------

# 4. Add a pet through the Service Layer

# --------------------------------------------------


# FUNCTION DEFINITION:

# create_pet() is a Service Layer function.

#

# name, pet_type, breed, age, owner_name

# → PARAMETERS

def create_pet(

    name,

    pet_type,

    breed,

    age,

    owner_name,

):


    # FUNCTION CALL:

    # Call add_pet() in the Repository Layer.

    #

    # new_pet_id

    # → VARIABLE

    # → stores the ID of the newly created pet

    new_pet_id = add_pet(

        name,

        pet_type,

        breed,

        age,

        owner_name,

    )


    # RETURN STATEMENT:

    # Return the new pet ID.

    return new_pet_id


# --------------------------------------------------

# 5. Update a pet through the Service Layer

# --------------------------------------------------



# FUNCTION DEFINITION:

# update_pet_service() is a Service Layer function.

#

# pet_id, name, pet_type, breed, age, owner_name

# → PARAMETERS

def update_pet_service(

    pet_id,

    name,

    pet_type,

    breed,

    age,

    owner_name,

):


    # FUNCTION CALL:

    # Call update_pet() in the Repository Layer.

    #

    # rows_updated

    # → VARIABLE

    # → stores how many rows were updated

    rows_updated = update_pet(

        pet_id,

        name,

        pet_type,

        breed,

        age,

        owner_name,

    )


    # RETURN STATEMENT:

    # Return the number of rows updated.

    return rows_updated



main.py 

# main.py


# --------------------------------------------------

# 1. Import Service Layer function

# --------------------------------------------------


# IMPORT STATEMENT:

# Import update_pet_service() from pet_service.py.

from app.services.pet_service import update_pet_service


# --------------------------------------------------

# 2. Main function

# --------------------------------------------------


# FUNCTION DEFINITION:

def main():


    print("🐾 Happy Paws Pet Hotel")

    print("------------------------")


    # FUNCTION CALL:

    # Ask the Service Layer to update pet ID 1.

    #

    # rows_updated

    # → VARIABLE

    # → stores the value returned by the Service Layer

    rows_updated = update_pet_service(

        1,

        "maew",

        "Cat",

        "Thai",

        400,

        "Dang",

    )


    # FUNCTION CALL:

    # Display how many rows were updated.

    print(f"Rows updated: {rows_updated}")


# --------------------------------------------------

# 3. Run the program

# --------------------------------------------------


if __name__ == "__main__":

    main()



MariaDB [happy_paws]> select * from pets;

+----+-------+------+--------+------+------------+

| id | name  | type | breed  | age  | owner_name |

+----+-------+------+--------+------+------------+

|  1 | maew  | Cat  | Thai   |  400 | Dang       |

|  2 | Buddy | Dog  | Beagle |    2 | Anan       |




Lesson 4 — Service Layer

Step 6 of 8 — Delete a Pet Through the Service


| Lesson 1 — Architecture & Project Setup <br> Lesson 2 — MariaDB + Docker <br> Lesson 3 — Python + MariaDB <br> Lesson 4 — Service Layer <br> Lesson 5 — FastAPI <br> Lesson 6 — NiceGUI <br> Lesson 7 — Our FastMCP <br> Lesson 8 — MariaDB MCP Server <br> Lesson 9 — Our FastMCP vs MariaDB MCP <br> Lesson 10 — Connect the AI Assistant <br> Lesson 11 — Docker Compose Integration <br> Lesson 12 — Security & Safe AI Access <br> Lesson 13 — Final Integrated Mini Project |
| --- |


| Step 1 of 8  Create the Pet Service                  ✅ <br> Step 2 of 8  Get All Pets Through the Service        ✅ <br> Step 3 of 8  Get One Pet Through the Service         ✅ <br> Step 4 of 8  Add a Pet Through the Service           ✅ <br> Step 5 of 8  Update a Pet Through the Service        ✅ <br> Step 6 of 8  Delete a Pet Through the Service        ◄── YOU ARE HERE <br> Step 7 of 8  Add Business Rules <br> Step 8 of 8  Review the Service Layer |
| --- |


| main.py <br> │ <br> ▼ <br> Service Layer <br> delete_pet_service() <br> │ <br> ▼ <br> Repository Layer <br> delete_pet() <br> │ <br> ▼ <br> MariaDB |
| --- |


# app/services/pet_service.py


# --------------------------------------------------

# 1. Import Repository Layer functions

# --------------------------------------------------


# IMPORT STATEMENT:

# Import functions from pet_repository.py.

#

# get_all_pets

# → FUNCTION in the Repository Layer

#

# get_pet_by_id

# → FUNCTION in the Repository Layer

#

# add_pet

# → FUNCTION in the Repository Layer

#

# update_pet

# → FUNCTION in the Repository Layer

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


# FUNCTION DEFINITION:

# list_pets() is a Service Layer function.

def list_pets():


    # FUNCTION CALL:

    # Call get_all_pets() in the Repository Layer.

    #

    # pets

    # → VARIABLE

    # → stores all pet rows returned from MariaDB

    pets = get_all_pets()


    # RETURN STATEMENT:

    # Return all pets to the caller.

    return pets


# --------------------------------------------------

# 3. Get one pet through the Service Layer

# --------------------------------------------------


# FUNCTION DEFINITION:

# get_pet() is a Service Layer function.

#

# pet_id

# → PARAMETER

# → identifies which pet we want

def get_pet(pet_id):


    # FUNCTION CALL:

    # Call get_pet_by_id() in the Repository Layer.

    #

    # pet_id

    # → ARGUMENT

    #

    # pet

    # → VARIABLE

    # → stores one pet row returned from MariaDB

    pet = get_pet_by_id(pet_id)


    # RETURN STATEMENT:

    # Return the pet to the caller.

    return pet


# --------------------------------------------------

# 4. Add a pet through the Service Layer

# --------------------------------------------------


# FUNCTION DEFINITION:

# create_pet() is a Service Layer function.

#

# name, pet_type, breed, age, owner_name

# → PARAMETERS

def create_pet(

    name,

    pet_type,

    breed,

    age,

    owner_name,

):


    # FUNCTION CALL:

    # Call add_pet() in the Repository Layer.

    #

    # new_pet_id

    # → VARIABLE

    # → stores the ID of the newly created pet

    new_pet_id = add_pet(

        name,

        pet_type,

        breed,

        age,

        owner_name,

    )


    # RETURN STATEMENT:

    # Return the new pet ID.

    return new_pet_id


# --------------------------------------------------

# 5. Update a pet through the Service Layer

# --------------------------------------------------


# FUNCTION DEFINITION:

# update_pet_service() is a Service Layer function.

#

# pet_id, name, pet_type, breed, age, owner_name

# → PARAMETERS

def update_pet_service(

    pet_id,

    name,

    pet_type,

    breed,

    age,

    owner_name,

):


    # FUNCTION CALL:

    # Call update_pet() in the Repository Layer.

    #

    # rows_updated

    # → VARIABLE

    # → stores how many rows were updated

    rows_updated = update_pet(

        pet_id,

        name,

        pet_type,

        breed,

        age,

        owner_name,

    )


    # RETURN STATEMENT:

    # Return the number of rows updated.

    return rows_updated


# --------------------------------------------------

# 6. Delete a pet through the Service Layer

# --------------------------------------------------


# FUNCTION DEFINITION:

# delete_pet_service() is a Service Layer function.

#

# pet_id

# → PARAMETER

# → identifies which pet we want to delete

def delete_pet_service(pet_id):


    # FUNCTION CALL:

    # Call delete_pet() in the Repository Layer.

    #

    # pet_id

    # → ARGUMENT

    #

    # rows_deleted

    # → VARIABLE

    # → stores how many database rows were deleted

    rows_deleted = delete_pet(pet_id)


    # RETURN STATEMENT:

    # Return the number of deleted rows to the caller.

    return rows_deleted


