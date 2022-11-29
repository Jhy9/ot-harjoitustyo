```mermaid
classDiagram

game "1...*"--"1" board
board "1"--"*" tile
game .. save_manager

```
