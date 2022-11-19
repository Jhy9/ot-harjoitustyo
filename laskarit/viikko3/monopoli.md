T.1

```mermaid
classDiagram
  Peli-->"2-8"Pelaaja
  Pelilauta"1"<-- Peli
  Ruutu"40"<--Pelilauta 
  Pelinappula"1"<--Pelaaja
  Ruutu"1"-->Ruutu
  Pelinappula ..>  "1"Ruutu
  
  ```
  
  
  T.2
  
  ```mermaid
classDiagram
  Peli-->"2-8"Pelaaja
  Pelilauta"1"<-- Peli
  Ruutu"40"<--Pelilauta 
  Pelinappula"1"<--Pelaaja
  Ruutu"1"-->Ruutu
  Pelinappula ..>  "1"Ruutu
  Vankila --|> Ruutu
  Peli -->"1" Vankila
  Lähtöruutu --|> Ruutu
  Peli -->"1" Lähtöruutu
  SattumaYhteismaa  --|> Ruutu
  AsemaLaitos --|> Ruutu
  Katu --|> Ruutu
  class Ruutu{
    +toiminto()
  }
  class Pelaaja{
    rahat
  }
  class Katu{
    Pelaaja omistaja
    Rakennus
  }
  class SattumaYhteismaa{
    Kortti
  }
  ```
