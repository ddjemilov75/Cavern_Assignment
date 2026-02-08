# Cavern Master

## How to Run the Game

1. Open a terminal and navigate to the cavern-master folder.
2. Make sure the following Python packages are installed:
   - pygame
   - pgzero
   - pgzrun (if used)
3. Run the game with the command:

pgzrun cavern.py

4. Enjoy playing.

## How to Run Tests

There are no tests.
This may be my fault, but I'm not clear on how we are supposed to implement testing.
Also no mention in assignment instructions, or during class, that testing was required.

## Project Structure

- Top-level:
  - cavern.py — the main entry point for the game.

- Inside src/:

-src/
   -app.py
   -constants.py
   -game.py
   -init.py
   -input.py
   -sound.py
   -states.py
   -utils.py
   -music (folder for music files)
   -sounds (folder for sound effect files)
   -images (folder for image files)
   -screens/
      -init.py
      -game_over.py
      -menu.py
      -play.py
   -entities/
      -base.py
      -bolt.py
      -effects.py
      -fruit.py
      -init.py
      -orb.py
      -player.py
      -robot.py

- Modularization:
  - Split the game into smaller modules: entities for game objects, screens for UI/gameflow.
  - Each Entity (Player, Robot, Orb, Fruit, Bolt) has its own file.
  - Screens separated into menu.py, game_over.py, and play.py.

- Refactoring:
  - Reduced circular imports by passing references explicitly.
  - Added utility modules: constants.py, utils.py, input.py, sound.py.
  - Top-level cavern.py remains the entry point.

- Gameplay Preservation:
  - All original mechanics, physics, and controls are preserved.
  - Player, Robot, Orbs, and other entities interact as before.
  - Sounds and images should be placed in the correct assets folder for pgzrun.
