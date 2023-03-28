# Don't let them perish

Simple REST and GraphQL API using postgreSQL to manage plants in each related room.

[GraphQL queries](#graphql)  
[REST endpoints](#rest)  
[Setup](#setip)

**Room**
Room name
Plant count (updated upon change)

**Plant**
Plant name
Date last watered
Associated room

## Technologies

- Python
- Flask
- GraphQL
- SQLAlchemy
- PostgreSQL

## <a name="graphql">GraphQL query examples</a>

### Add a Room:

```
mutation {
  addRoom(
    roomName:"Kitchen"
  )
    {
    room{
      id
      roomName
      plantCount
    }
  }
  }

```

### Add a Plant:

```
mutation {
  addPlant(
    roomName:"Kitchen",
    plantName:"Spider",
    dateWatered:"26/03/2023")
  {
    plant{
      id
      plantName
      dateWatered
      location{
        roomName
      }
    }
  }
}

```

### View all Rooms:

```
{
  allRooms{
    edges{
      node{
        roomName
        plantCount
      }
    }
  }
}
```

### View all Plants:

```
{
  allPlants{
    edges{
      node{
        plantName
        location {
          id
        }
        dateWatered
      }
    }

  }
}
```

### View Room by name:

```
query {
  roomByName(roomName: "Kitchen") {
    id
    roomName
    plantCount
  }
}
```

### View Plant by name:

```
query {
  plantByName(plantName: "Spider") {
    id
    plantName
    dateWatered
    location {
      roomName
    }
  }
}
```

### Delete Room by name:

```
mutation {
  deleteRoomByName(roomName: "Kitchen") {
    success
  }
}
```

### Update Room:

```
mutation {
  updateRoom(
    roomData: {
      id: "Um9vbVR5cGU6NA=="
      roomName: "Bathroom"
    }
  ) {
    success
  }
}
```

### Update Plant:

```
mutation {
  updatePlant(
    plantData: {
      id: "UGxhbnRUeXBlOjg="
      plantName: "Spider"
      dateWatered: "27/03/2023"
    }
  ) {
    success
  }
}
```

## <a name="rest">REST endpoints</a>

### Rooms

Get all Rooms: `GET /rooms`

Get Room by ID: `GET /rooms/<id>`

Get Room by name: `GET /rooms/<room name>`

Create Room: `POST /rooms` with json:

```
{
    "room_name": "Kitchen"
}
```

Update Room: `PUT /rooms` with json:

```
{
    "room_name": "Kitchen"
}
```

Delete Room by ID: `DELETE /rooms/<id>`

### Plants

Get all Plants: `GET /plants`

Get Plant by ID: `GET /plants/<id>`

get Plant by name: `GET /plants/<plant name>`

Create Plant: `POST /plants` with json:

```
{
    "plant_name": "Fern",
    "date_watered": "27/03/2023",
    "room_name": "Kitchen"
}
```

Update Plant: `PUT /plants` with json:

```
{
    "plant_name": "Fern",
    "date_watered": "27/03/2023",
    "room_name": "Kitchen"
}
```

Delete Plant by ID: `DELETE /plants/<id>`

## <a name="setup">Setup</a>

Create PostgreSQL database: `createdb dont_let_them_perish`

Create `.env` file and add `DATABASE_URL='postgresql://user:password@localhost/dont_let_them_perish'`, replacing user, password and database name as needed.
See `.env_example` for example.

From main directory run `python -m pip install -r requirements.txt` to install required packages.

Run the app in terminal: `python app.py`
