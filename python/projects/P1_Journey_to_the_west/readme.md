# Journey to the West - Text Adventure Game

Xuehua Xiong 08.2026

## Overview
This is a text-based interactive game inspired by the Chinese fantacy novel "Journey to the West". In 629 AD, in real history, the monk, Master Xuanzang departed from western China, and began on a 16-year journey across Central Asia, finally reached his destination at Nalanda in India, to study sacred Buddhist texts and bring knowledge back to his people. In this game, the player takes on the role of Master.Xuanzang, walking the adventurous path by making wise choices when encountering legendary companions (Wukong, Bajay, Sandy). The decisions made throughout the journey will affect the team's trust score and determine the type of their teammate relationships.

## SDG Alignment
It meets the UN's Sustainable Development Goals by fostering SDG 4 (Quality Education) through the cultural preservation and storytelling of classic mythological novel, and SDG 17 (Partnerships for the Goals) by emphasizing equal partnership, emotional support, and inclusive collaboration among teammates rather than hierarchical control 

## Project Structure
- `main.py`: Navigation of the entry of application, the main menu, user registration, and age verification.
- `game_logic.py`: Manages the core storyline chapters, player interactions, trust score calculation, and final ending evaluations.

## Features
- **User Input**: Asks for the player's name and age using `input()`.
- **Age Check**: Uses `if` statements to check if the player is at least 12 years old.
- **Choices**: Uses `if-elif-else` statements so players can choose different options to shape the story.
- **Score and Lists**: Uses basic variables to track trust scores and a list (`team`) to collect companions.

## How to Run
1. Put `main.py` and `game_logic.py` in the same folder.
2. Open your terminal in that folder.