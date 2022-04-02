### UML
```mermaid
 classDiagram
      class Game{
        +Int diceAmt
        +Tile startTile
        +Tile jailTile
        +Player[8] players
        +Die[2] dice
        +Tile[40] squares
      }
      class Board{
          +Int squares
          +String id
      }
      class Player{
          +String username
          +String id
          +Piece piece
      }
      class Piece{
        +Tile onSquare
        +move()
      }
      class Die{
          +String username
          +String id
          +throw()
      }
      class Tile{
        +Tile succSquare
        +Tile predSquare
        +Piece piece
        +Player owner
      }
      class RandomTile{
        +Card[] cards
      }
      class StartTile{
        +Card card
      }
      class StationTile{
        +String name
      }
      class JailTile{
        +Player jailedPlayer
      }
      class StreetTile{
        +String street
        +House[4] houses
        +Hotel hotel
        +hasHotel() boolean
      }

      class Building{
        
      }

      class Hotel{
        String name
        Int price
      }

      class House{
        Int price
      }

      class Card{
        +action()
      }


      Game --* Board
      Game --* Player
      Game --* Die
      Board --* Tile
      Player -- Piece
      Tile -- Piece
      Tile -- JailTile : instance
      Tile -- StartTile : instance
      Tile -- RandomTile : instance
      Tile -- StationSquare : instance
      Tile -- StreetTile
      StreetTile -- House
      StreetTile -- Hotel
      RandomTile -- Card
 ```