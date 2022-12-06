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

main ->> Board: change_value(location, value)
Board ->> Tile: change_value(value)
main ->> Game: check_board()
Game -->> main: 1
