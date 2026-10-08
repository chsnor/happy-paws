Claude Code + MariaDB MCP Server — Mini Tutorial


Install Claude Code

In powershell

PS C:\Users\Pacifica> irm https://claude.ai/install.ps1 | iex


PS C:\Users\Pacifica> claude --version

2.1.289 (Claude Code)


PS C:\Users\Pacifica> cd C:\alongkot_299\happy-paws2


PS C:\alongkot_299\happy-paws2> claude


| Claude Code <br> │ <br> │ MCP <br> ▼ <br> MariaDB MCP Server <br> │ <br> │ SQL <br> ▼ <br> MariaDB <br> │ <br> ▼ <br> happy_paws |
| --- |







Step 2 of 2 — Understand MCP Client and Server


| Setup     Install Claude Code <br> Lesson 1  Understand the Architecture <br> Step 1  Understand the Connection <br> Step 2  Understand MCP Client and Server <br> Lesson 2  Store MariaDB Credentials in Windows <br> Lesson 3  Install MariaDB MCP Server <br> Lesson 4  Connect Claude Code to MariaDB MCP <br> Lesson 5  Query the Happy Paws Database |
| --- |



| Claude Code                         MariaDB MCP Server <br> │                                      │ <br> │          MCP request                 │ <br> ├─────────────────────────────────────►│ <br> │                                      │ <br> │                                Execute SQL <br> │                                      │ <br> │                                   MariaDB <br> │                                      │ <br> │          MCP result                  │ <br> ◄─────────────────────────────────────┤ |
| --- |

Lesson 2 — Store MariaDB Credentials in Windows

Step 1 of 2 — Create Windows User Environment Variables


| Setup     Install Claude Code                         ✅ <br> Lesson 1  Understand the Architecture                 ✅ <br> Step 1  Understand the Connection           ✅ <br> Step 2  Understand MCP Client and Server    ✅ <br> Lesson 2  Store MariaDB Credentials in Windows <br> Step 1  Create User Environment Variables   ◄── YOU ARE HERE <br> Step 2  Verify Environment Variables <br> Lesson 3  Install MariaDB MCP Server <br> Lesson 4  Connect Claude Code to MariaDB MCP <br> Lesson 5  Query the Happy Paws Database |
| --- |


We will store MariaDB Credentials as Windows User Environment Variables.


Windows User Environment Variables

│

├── DB_HOST       = localhost

├── DB_PORT       = 3333 / 3306

├── DB_USER       = root

├── DB_PASSWORD   = ********

└── DB_NAME       = happy_paws


PS C:\alongkot_299\happy-paws2> [Environment]::SetEnvironmentVariable("DB_HOST", "localhost", "User")

PS C:\alongkot_299\happy-paws2> [Environment]::SetEnvironmentVariable("DB_USER", "happyuser", "User")

PS C:\alongkot_299\happy-paws2> [Environment]::SetEnvironmentVariable("DB_PASSWORD", "happypassword", "User")


PS C:\alongkot_299\happy-paws2> [Environment]::SetEnvironmentVariable("DB_NAME", "happy_paws", "User")


| Windows User Environment Variables <br> │ <br> ├── DB_USER <br> └── DB_PASSWORD <br> │ <br> ▼ <br> MariaDB MCP Server |
| --- |




Lesson 2 — Store MariaDB Credentials in Windows

Step 2 of 2 — Verify Environment Variables

| Setup     Install Claude Code                         ✅ <br> Lesson 1  Understand the Architecture                 ✅ <br> Step 1  Understand the Connection           ✅ <br> Step 2  Understand MCP Client and Server    ✅ <br> Lesson 2  Store MariaDB Credentials in Windows <br> Step 1  Create User Environment Variables   ✅ <br> Step 2  Verify Environment Variables        ◄── YOU ARE HERE <br> Lesson 3  Install MariaDB MCP Server <br> Lesson 4  Connect Claude Code to MariaDB MCP <br> Lesson 5  Query the Happy Paws Database |
| --- |


PS C:\Users\Pacifica> echo $env:DB_USER

happyuser

PS C:\Users\Pacifica> echo $env:DB_NAME

happy_paws

PS C:\Users\Pacifica> echo $env:DB_HOST

localhost

PS C:\Users\Pacifica> if ($env:DB_PASSWORD) { "DB_PASSWORD is set" } else { "DB_PASSWORD is NOT set" }

DB_PASSWORD is set



Lesson 4 — Install and Connect MariaDB MCP Server

Step 1 of 3 — Download the Official MariaDB MCP Server


| Setup     Install Claude Code                         ✅ <br> Lesson 1  Understand the Architecture                 ✅ <br> Step 1  Understand the Connection           ✅ <br> Step 2  Understand MCP Client and Server    ✅ <br> Lesson 2  Store MariaDB Credentials in Windows        ✅ <br> Step 1  Create User Environment Variables   ✅ <br> Step 2  Verify Environment Variables        ✅ <br> Lesson 3  Connect MCP to Our Docker MariaDB            ✅ <br> Step 1  Verify MariaDB Docker Container      ✅ <br> Step 2  Verify happy_paws Database           ✅ <br> Lesson 4  Install and Connect MariaDB MCP Server <br> Step 1  Download MariaDB MCP Server          ◄── YOU ARE HERE <br> Step 2  Install MCP Server Dependencies <br> Step 3  Add MariaDB MCP to Claude Code <br> Lesson 5  Query Happy Paws with Claude Code |
| --- |



| C:\alongkot_299 <br> │ <br> ├── happy-paws <br> │     └── Our application <br> │ <br> └── mariadb-mcp <br> └── MCP server for Claude |
| --- |


PS C:\alongkot_299> git clone https://github.com/MariaDB/mcp.git mariadb-mcp


PS C:\alongkot_299> cd mariadb-mcp


Lesson 4 — Install and Connect MariaDB MCP Server

Step 2 of 3 — Install MCP Server Dependencies


| Setup     Install Claude Code                         ✅ <br> Lesson 1  Understand the Architecture                 ✅ <br> Lesson 2  Store MariaDB Credentials in Windows        ✅ <br> Lesson 3  Connect MCP to Our Docker MariaDB           ✅ <br> Lesson 4  Install and Connect MariaDB MCP Server <br> Step 1  Download MariaDB MCP Server         ✅ <br> Step 2  Install MCP Server Dependencies     ◄── YOU ARE HERE <br> Step 3  Add MariaDB MCP to Claude Code <br> Lesson 5  Query Happy Paws with Claude Code |
| --- |


PS C:\alongkot_299\mariadb-mcp> uv sync



Lesson 4 — Install and Connect MariaDB MCP Server

Step 3 of 3 — Add MariaDB MCP to Claude Code


| Setup     Install Claude Code                         ✅ <br> Lesson 1  Understand the Architecture                 ✅ <br> Lesson 2  Store MariaDB Credentials in Windows        ✅ <br> Lesson 3  Connect MCP to Our Docker MariaDB           ✅ <br> Lesson 4  Install and Connect MariaDB MCP Server <br> Step 1  Download MariaDB MCP Server         ✅ <br> Step 2  Install MCP Server Dependencies     ✅ <br> Step 3  Add MariaDB MCP to Claude Code      ◄── YOU ARE HERE <br> Lesson 5  Query Happy Paws with Claude Code |
| --- |


PS C:\alongkot_299\mariadb-mcp> claude mcp add mariadb --scope user --transport stdio uv -- --directory C:\alongkot_299\mariadb-mcp run server.py


PS C:\alongkot_299\mariadb-mcp> claude mcp list



