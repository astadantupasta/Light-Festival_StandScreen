# Light-Festival_StandScreen

This project is software for a real light installation which consists of 169 lit tiles (13x13 matrix). The code has a visual simulation (user interface) in order to simulate interaction with the light installation via computer.

In reality, a person has to step on the tile. In UI, a user has to click on the square when "stepping on" the tile, and unclick it when wants to "step off" the tile.
Numbers on the tiles: weight of a person, which is on the tile.

Code runs in cycles:
1. An animation of 1 min is shown (with music), no interaction with the installation is needed.
2. Then, for 5 min the user can interact with the installation (step on it). If no interaction happens in 20 sec., a default animation with music is displayed.
3. After 5 min, another game turns on and is shown for 5 min.
4. Cycle starts again

Running the code
------------
```sh
$ python main.py
```
