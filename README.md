# Don't let them perish

Simple API using GraphQL and postgreSQL to manage plants in each related room.

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

## GraphQL query examples

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
