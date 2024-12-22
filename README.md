# LastMove-Game
Stone Game

This project is a two-player console-based game that involves strategy and careful planning. Players take turns moving their big stones and placing small stones on the game board. The objective is to block your opponent's movements and claim victory.

## Features

Dynamic Board Size: Players can select a board size of 3x3, 5x5, or 7x7.
Player Symbols: Each player selects a unique symbol to represent their big stone.
Turn-Based Gameplay: Players alternate turns moving their big stones and placing small stones.
Custom Movement Directions: Stones can move in cardinal (N, S, E, W) and diagonal (NE, NW, SE, SW) directions.
Win Condition: The winner is the player who successfully blocks their opponent from moving their big stone.

## How to Play
Each player selects a unique capital letter to represent their big stone (excluding "O").
Choose the size of the board (3, 5, or 7).
The game begins with Player 1's big stone at the bottom center and Player 2's big stone at the top center of the board.
During each turn:
Move your big stone in any valid direction.
Place a small stone ("O") on the board to block your opponent.
The game ends when a player successfully blocks their opponent's big stone from moving.

Follow the on-screen instructions to play the game.

## Project Structure

stone_game.py: Contains the main game logic and functions.

## Key Functions

is_place_taken(table_list, row, col): Checks if a position on the board is already occupied.

draw_table(size, table_list, letters): Renders the game board in the console.

put_small_stone(table_list, player_symbol, positions): Allows a player to place a small stone on the board.

move_big_stone(size, table_list, player_symbol, pos_player, directions): Handles the movement of a player's big stone.

find_winner(table_list, directions, pos_opponent, size, player_symbol): Determines if a player has won by blocking their opponent.

play(p1_symbol, p2_symbol, size, table_list, letters, directions): Manages the main gameplay loop.

main(): Entry point for the program, initializing game settings and starting the game loop.

## Example Gameplay

Initialization:
Player 1 selects A, Player 2 selects B.
Board size: 5x5.

Game Board:

    A   B   C   D   E
  ---------------------
1 |   |   |  |   |   | 1
  ---------------------
2 |   |   |   |   |   | 2
  ---------------------
3 |   |   |   |   |   | 3
  ---------------------
4 |   |   |   |   |   | 4
  ---------------------
5 |   |   | A |   |   | 5
    A   B   C   D   E

Player Turns:

Player 1 moves their big stone and places a small stone.

Player 2 does the same.

Winning:

The game ends when one player cannot move their big stone.
