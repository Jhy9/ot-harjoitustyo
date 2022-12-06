Luokkakaavio:
```mermaid
classDiagram

game "1...*"--"1" board
board "1"--"*" tile
game .. save_manager

```
Sekvenssikaavio:
Ruudun arvon muutos, joka ei aiheuta virhettä pelin kannalta:

```mermaid
sequenceDiagram

main ->> Board: changeValue(location, value)
Board ->> Tile: changeValue(value)
main ->> Game: check_Board()
Game -->> main: 1
