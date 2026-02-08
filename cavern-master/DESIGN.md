# Cavern Master Design Overview

## Screens Architecture

The game uses a screen-based architecture to separate game states. Each screen handles its own update and draw logic.

- **MenuScreen**: Displays the title and waits for the player to start. Handles animation of the “Press Space” prompt.
- **PlayScreen**: Manages the active gameplay, calling update/draw on all entities and handling collisions.
- **GameOverScreen**: Shows the game over screen and waits for the player to restart or quit.

The `App` class acts as the central controller, holding a reference to the current screen and switching between them based on `State` enums (`MENU`, `PLAY`, `GAME_OVER`).

## Input Design

- Inputs are abstracted into an `InputState` object passed to each screen.
- Player controls (movement and actions) are mapped to keyboard keys (left, right, up, space).
- Functions or references are passed explicitly to entities that require input (e.g., Player for movement and shooting) to avoid circular imports.

This allows screens and entities to remain decoupled from Pygame’s global state while still reacting to user input.

## Pause Functionality

- Pause is handled within `PlayScreen` by tracking a `paused` flag.
- When pause is triggered (e.g., via a key press), the `update` method skips entity updates while still drawing the game state.
- Input is still monitored during pause to allow unpausing.
- This design keeps pause localized to gameplay without affecting menu or game over screens.

**Summary:** Screens isolate logic by state, input is injected explicitly, and pause is a simple flag checked during `PlayScreen.update()`. This ensures clean separation of concerns and avoids tangled dependencies.