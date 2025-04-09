# Add FastAPI Web Service Integration for Blakserv

## What
- Created FastAPI routes for server management in `api.py`
- Configured FastAPI server to connect to the BlakSton server maintenance port
- Implemented initial API endpoints:
  - GET /api/v1/admin/who
  - GET /api/v1/admin/status
  - GET /api/v1/admin/memory
  - POST /api/v1/admin/send-users

## Why
- Enable modern web-based management interface for blakserv
- Provide secure, RESTful API access to server functions
- Allow external tools/services to interact with the server

## Technical Flow
```ascii
FastAPI Client -> FastAPI Routes -> Maintenance Port -> Blakserv
   (HTTP)          (api.py)       (TCP Socket)         (C Core)

[Web Client] --HTTP--> [FastAPI Router] 
                          |
                          v
                    [Maintenance Port] 
                          |
                          v
                        Blakserv
```

## Implementation Details
### FastAPI Router (`api.py`):

- REST endpoint definitions
- JSON response formatting
- Maintenance port command handling

### Maintenance Client (`maintenance.py`):

- TCP socket connection to BlakSton server maintenance port
- Command sending and response handling

## Configuration
Add the following to the `blakserv.cfg` in the server running directory:
```
[Socket]             
MaintenancePort      9998
MaintenanceMask      0.0.0.0
```

## Setting Up the Environment
1. **Install Poetry**:
   Follow the instructions on the [Poetry installation page](https://python-poetry.org/docs/#installation) to install Poetry.

2. **Initialize and Install Dependencies**:
   Navigate to the project directory and install dependencies:
   ```bash
   cd c:\Meridian59\blakserv\fastapi
   poetry install
   ```

3. **Activate the Virtual Environment**:
   ```bash
   poetry shell
   ```

## Starting the FastAPI Server
1. Start the FastAPI server using uvicorn:
   ```bash
   uvicorn main:app --host 127.0.0.1 --port 8000 --reload
   ```

## Testing
- Access the API documentation at `http://127.0.0.1:8000/docs`
- Test the endpoints using curl or a web browser:
   ```bash
   curl -X GET "http://127.0.0.1:8000/api/v1/admin/who"
   curl -X GET "http://127.0.0.1:8000/api/v1/admin/status"
   curl -X GET "http://127.0.0.1:8000/api/v1/admin/memory"
   curl -X POST "http://127.0.0.1:8000/api/v1/admin/send-users?message=Hello"
   ```

``` mermaid
graph TD
    subgraph Users
        P[Players] --> W[Web Interface]
        A[Admins] --> W
        I[IoT/Automations] --> API[FastAPI Endpoints]
    end
    
    subgraph Server Integration
        W --> API
        API --> M[Maintenance Port]
        M --> B[Blakserv]
        B --> G[Game World]
    end
```


## Available commands
The following list shows the admin commands that are to be implemented via FastAPI using the maintenance port.

6 complete

### Show Commands
- show account (AdminShowAccount) :white_check_mark:
- show belong (AdminShowObjects) :white_check_mark:
- show class (AdminShowClass) :white_check_mark:
- show clock (AdminShowTime) :white_check_mark:
- show configuration (AdminShowConfiguration)
- show constant (AdminShowConstant)
- show list (AdminShowList)
- show listnode (AdminShowListNode)
- show memory (AdminShowMemory) :white_check_mark:
- show message (AdminShowMessage)
- show name (AdminShowName)
- show object (AdminShowObject)
- show protocol (AdminShowProtocol)
- show resource (AdminShowResource)
- show status (AdminShowStatus) :white_check_mark:
- show string (AdminShowString)
- show table (AdminShowTable)
- show timer (AdminShowTimer)
- show usage (AdminShowUsage)
- show user (AdminShowUser)

### Set Commands
- set account name (AdminSetAccountName)
- set account object (AdminSetAccountObject)
- set account password (AdminSetAccountPassword)
- set class (AdminSetClass)
- set config boolean (AdminSetConfigBool)
- set config integer (AdminSetConfigInt)
- set config string (AdminSetConfigStr)
- set object (AdminSetObject)

### Suspend Commands
- suspend account (AdminSuspendAccount)
- suspend user (AdminSuspendUser)

### Unsuspend Commands
- unsuspend account (AdminUnsuspendAccount)
- unsuspend user (AdminUnsuspendUser)

### Send Commands
- send object (AdminSendObject)
- send users (AdminSendUsers) :white_check_mark:
- send class (AdminSendClass)

### Terminate Commands
- terminate nosave (AdminTerminateNoSave)
- terminate save (AdminTerminateSave)

### Miscellaneous Commands
- garbage (AdminGarbage)
- lock (AdminLock)
- mark (AdminMark)
- read (AdminRead)
- reload game (AdminReloadGame)
- reload motd (AdminReloadMotd)
- reload packages (AdminReloadPackages)
- reload system (AdminReloadSystem)
- save configuration (AdminSaveConfiguration)
- save game (AdminSaveGame)
- say (AdminSay)
- unlock (AdminUnlock)
- who (AdminWho)  :white_check_mark: Done












### Show Commands
- show account (AdminShowAccount) :white_check_mark: Done
show belong (AdminShowObjects)
show class (AdminShowClass)
- show clock (AdminShowTime) :white_check_mark: Done
show configuration (AdminShowConfiguration)
show constant (AdminShowConstant)
show list (AdminShowList)
show listnode (AdminShowListNode)
- show memory (AdminShowMemory) :white_check_mark: Done
show message (AdminShowMessage)
show name (AdminShowName)
show object (AdminShowObject)
show protocol (AdminShowProtocol)
show resource (AdminShowResource)
- show status (AdminShowStatus) :white_check_mark: Done
show string (AdminShowString)
show table (AdminShowTable)
show timer (AdminShowTimer)
show usage (AdminShowUsage)
show user (AdminShowUser)

### Set Commands
set account name (AdminSetAccountName)
set account object (AdminSetAccountObject)
set account password (AdminSetAccountPassword)
set class (AdminSetClass)
set config boolean (AdminSetConfigBool)
set config integer (AdminSetConfigInt)
set config string (AdminSetConfigStr)
set object (AdminSetObject)

### Suspend Commands
suspend account (AdminSuspendAccount)
suspend user (AdminSuspendUser)
Unsuspend Commands
unsuspend account (AdminUnsuspendAccount)
unsuspend user (AdminUnsuspendUser)

### Send Commands
send object (AdminSendObject)
send users (AdminSendUsers) :white_check_mark: Done
send class (AdminSendClass)

### Terminate Commands
terminate nosave (AdminTerminateNoSave)
terminate save (AdminTerminateSave)

### Miscellaneous Commands
garbage (AdminGarbage)
lock (AdminLock)
mark (AdminMark)
read (AdminRead)
reload game (AdminReloadGame)
reload motd (AdminReloadMotd)
reload packages (AdminReloadPackages)
reload system (AdminReloadSystem)
save configuration (AdminSaveConfiguration)
save game (AdminSaveGame)
say (AdminSay)
unlock (AdminUnlock)
who (AdminWho) 
### Show Commands
- show account (AdminShowAccount) :white_check_mark: Done
show belong (AdminShowObjects)
show class (AdminShowClass)
- show clock (AdminShowTime) :white_check_mark: Done
show configuration (AdminShowConfiguration)
show constant (AdminShowConstant)
show list (AdminShowList)
show listnode (AdminShowListNode)
- show memory (AdminShowMemory) :white_check_mark: Done
show message (AdminShowMessage)
show name (AdminShowName)
show object (AdminShowObject)
show protocol (AdminShowProtocol)
show resource (AdminShowResource)
- show status (AdminShowStatus) :white_check_mark: Done
show string (AdminShowString)
show table (AdminShowTable)
show timer (AdminShowTimer)
show usage (AdminShowUsage)
show user (AdminShowUser)

### Set Commands
set account name (AdminSetAccountName)
set account object (AdminSetAccountObject)
set account password (AdminSetAccountPassword)
set class (AdminSetClass)
set config boolean (AdminSetConfigBool)
set config integer (AdminSetConfigInt)
set config string (AdminSetConfigStr)
set object (AdminSetObject)

### Suspend Commands
- suspend account (AdminSuspendAccount)
- suspend user (AdminSuspendUser)
- Unsuspend Commands
- unsuspend account (AdminUnsuspendAccount)
- unsuspend user (AdminUnsuspendUser)

### Send Commands
- send object (AdminSendObject)
- send users (AdminSendUsers) :white_check_mark: Done
- send class (AdminSendClass)

### Terminate Commands
- terminate nosave (AdminTerminateNoSave)
- terminate save (AdminTerminateSave)

### Miscellaneous Commands
garbage (AdminGarbage)
lock (AdminLock)
mark (AdminMark)
read (AdminRead)
reload game (AdminReloadGame)
reload motd (AdminReloadMotd)
reload packages (AdminReloadPackages)
reload system (AdminReloadSystem)
save configuration (AdminSaveConfiguration)
save game (AdminSaveGame)
say (AdminSay)
unlock (AdminUnlock)
who (AdminWho)






























































all commands
### Show Commands

show account (AdminShowAccount)
- show accounts (AdminShowAccounts)
show belong (AdminShowObjects)
show class (AdminShowClass)
- show clock (AdminShowTime)
show configuration (AdminShowConfiguration)
show constant (AdminShowConstant)
show list (AdminShowList)
show listnode (AdminShowListNode)
- show memory (AdminShowMemory)
show message (AdminShowMessage)
show name (AdminShowName)
show object (AdminShowObject)
show protocol (AdminShowProtocol)
show resource (AdminShowResource)
- show status (AdminShowStatus)
show string (AdminShowString)
show table (AdminShowTable)
show timer (AdminShowTimer)
show usage (AdminShowUsage)
show user (AdminShowUser)
show users (AdminShowUsers)

### Set Commands

set account name (AdminSetAccountName)
set account object (AdminSetAccountObject)
set account password (AdminSetAccountPassword)
set class (AdminSetClass)
set config boolean (AdminSetConfigBool)
set config integer (AdminSetConfigInt)
set config string (AdminSetConfigStr)
set object (AdminSetObject)

### Suspend Commands

suspend account (AdminSuspendAccount)
suspend user (AdminSuspendUser)
Unsuspend Commands

unsuspend account (AdminUnsuspendAccount)
unsuspend user (AdminUnsuspendUser)

### Send Commands

send object (AdminSendObject)
send users (AdminSendUsers)
send class (AdminSendClass)
Terminate Commands

terminate nosave (AdminTerminateNoSave)
terminate save (AdminTerminateSave)

### Miscellaneous Commands

garbage (AdminGarbage)
lock (AdminLock)
mark (AdminMark)
read (AdminRead)
reload game (AdminReloadGame)
reload motd (AdminReloadMotd)
reload packages (AdminReloadPackages)
reload system (AdminReloadSystem)
save configuration (AdminSaveConfiguration)
save game (AdminSaveGame)
say (AdminSay)
unlock (AdminUnlock)
- who (AdminWho)