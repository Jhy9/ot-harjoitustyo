# Arkkitehtuuri
## Luokat

Luokkakaavio:
```mermaid
classDiagram

GameView -->"1" Game
Game -->"1" Board
Board -->"81" Tile
Game -->"1" SaveManager
SaveManager ..> Board

```
Luokka GameView vastaa visuaalisesta käyttöliittymästä.

Pelin keskeinen luokka on Game, jonka olio pitää itsellään peliä varten luokkien Board ja SaveManager olioita. Tämän lisäksi Game tarjoaa toiminnallisuuden tarkistaa lauta virheiden varalta metodilla check_game() ja raportoida niistä GameView:lle.

Luokan Board olio pitää itsessään pelilautaa, joka koostuu luokan Tile olioista. Board tarjoaa metodin muuttaa jonkin ruudukon sijainnin arvoa. Tämän lisäksi se voi metodeillaan palauttaa oman datansa eri muodoissa luokkien SaveManager, Game ja GameView käyttöön. 

Luokan Tile olio kuvaa pelinlaudan yhden ruudun sisältöä. Tile tarjoaa metodin muuttaa ruudun sisältöä Board oliolle.

Luokka SaveManager pitää vastuullaan tiedostojen käsittelyn. Se tarjoaa metodeillaan luokille Game ja GameView pelien lataus- ja tallennusmahdollisuudet.


## Toiminnallisuudet

### Numeron lisääminen
Numeron voi lisätä peliin valitsemalla laudalta ruudun ja painamalla lisättävää numeroa näppäimistöltä.
Lisätään ensimmäiseen ruutuun arvo 1, joka aiheuttaa virheen ensimmäiselle riville:
```mermaid
sequenceDiagram

GameView ->> Board: change_value(0, 1)
Board ->> Tile: change_value(1)
GameView ->> Game: check_board()
Game ->> Board: give_array_form()
Board -->> Game:board_array
Game -->> GameView: [0 1 2 3 4 5 6 7 8]
```
### Uuden pelin aloittaminen
Uusi peli alkaa, kun sovellus avataan tai valikon Uusi peli - komennolla.
```mermaid
sequenceDiagram

GameView ->> Game: Game()
Game ->> SaveManager: new_game()
SaveManager ->> Board: Board(boardstr)
SaveManager -->> Game: board
GameView ->> Board: give_array_form()
Board -->> GameView: board_array
```
### Pelin tallennus
Pelin voi tallentaa valikon komennolla Tallenna. Tämä avaa kansionäkymän, jossa käyttäjä voi tallentaa pelin.
Tallennus tiedostoon nimeltä test:
```mermaid
sequenceDiagram

GameView ->> SaveManager: save_game("test", board)
SaveManager ->> Board: give_save_form()
Board -->> SaveManager: board_data
```
### Pelin lataus
Pelin lataus tapahtuu komennolla Lataa, joka avaa kansionäkymän, josta käyttäjä voi valita ladattavan tiedoston.
Pelin lataus edellä tallennetusta tiedostosta:
```mermaid
sequenceDiagram

GameView ->> Game: load("src/Savegame/test")
Game ->> SaveManager: load_game("src/Savegame/test")
SaveManager ->> Board : Board(values,locks)
SaveManager -->> Game: board
GameView ->> Board: give_array_form()
Board -->> GameView: board_array

```
### Pelin luominen
Pelin luomisen voi aloittaa Pelin luonti- valikon näppäimellä Tyhjennä. Tämä luo tyhjän ruudukon seuraavasti.

```mermaid
sequenceDiagram

GameView ->> Game: Game("new")
Game ->> Board: Board([0]*81)
GameView ->> Board: give_array_form()
Board -->> GameView: board_array

```
Tämän jälkeen käyttäjä voi lisätä ruudukkoon numeroita normaalisti. Kun peli on halutunlainen, sen voi lisätä uusien pelien joukkoon Pelin luonti- valikon toiminnolla Tallenna uudeksi.
```mermaid
sequenceDiagram

GameView ->> SaveManager: add_new(board)

```
## Käyttöliittymä
Ohjelman käyttöliittymässä on yksi näkymä GameView, joka vastaa pelin visuaalisesta ulkonäöstä sekä ottaa vastaan käyttäjän syötteet. GameView ei itse toteuta näkymään liittymätöntä sovelluslogiikkaa vaan se kutsuu muiden luokkien metodeja luokan Game olion kautta. 
Lataus- ja tallennus tapahtuvat tiedostonäkymän sisältävien pop-up ikkunoiden kautta.

## Tiedon tallennus
Tiedon pysyväistalletus tapahtuu .txt muotoisiin tiedostoihin. 

Pelin aloitusruudukot sijaitsevat tiedostossa [src/sudoku/games.txt](../src/sudoku/games.txt), jossa jokainen rivi kuvaa yhtä aloitusruudukkoa. Tähän tiedostoon käyttäjä voi lisätä ruudukkoja pelin luomistoiminnon kautta.

Keskeneräisten pelien tallennus tapahtuu kansioon [src/Savegame](../src/Savegame), jonne jokainen peli tallennetaan omaan tekstitiedostoon muodossa ruudut+","+lukot.
