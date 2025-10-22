# 🎲 Monopoly-Style Board Game (2 Players)

A console-based Monopoly-style game for two players, built in **C**.  
Created by **Rares Făgădeanu (@raresstefan14)**.

---

## 🧠 Project Overview

This project is a simplified version of the classic Monopoly game, designed to run in the terminal.  
It allows **two players** to move around a virtual board, buy properties, pay rent, and compete until one goes bankrupt.

The game logic is based on **Markov Chains**, meaning that the next state (position on the board) depends only on the current state and the dice roll — a probabilistic approach used to simulate real movement dynamics across the board.

---

## 🧩 Key Features
- 🎯 Two-player gameplay  
- 🎲 Random dice rolling (probabilistic movement via Markov Chains)  
- 🏠 Property purchase, rent, and ownership tracking  
- 💰 Bankrupt detection and game-over logic  
- 🖥️ Console-based interface with clear text prompts  
- 🗂️ Modular code structure with separate `.c` and `.h` files  

---

## ⚙️ How to Compile & Run

1. **Clone the repository:**
   ```bash
   git clone https://github.com/raresstefan14/Monopoly-Style-Board-Game-2-Players.git
   cd Monopoly-Style-Board-Game-2-Players
   ```

2. **Compile the project (using GCC):**
   ```bash
   gcc main.c board.c game.c player.c -o monopoly
   ```
   *(or use the Makefile if included:)*  
   ```bash
   make
   ```

3. **Run the game:**
   ```bash
   ./monopoly
   ```

4. **Follow the on-screen instructions** to play.

---

## 🕹️ Simplified Game Rules
- Each player starts with a fixed balance.  
- Players take turns rolling the dice.  
- Landing on an unowned property allows the player to buy it.  
- Landing on an owned property requires rent payment.  
- If a player runs out of money, the other player wins.  

The **Markov Chain** model ensures that the movement across the board evolves probabilistically based on the dice outcomes, simulating realistic board traversal.

---

## 📁 Project Structure
```
/src
  ├── main.c        # Main entry point and game loop
  ├── game.c/.h     # Core gameplay logic and turns
  ├── board.c/.h    # Board setup and properties
  ├── player.c/.h   # Player structure, money, and ownership
/Makefile           # Build automation (optional)
/README.md          # This file
```

---

## 🧮 Technologies & Concepts Used
- **C Programming Language**
- **Structs** and **modular design**
- **Dynamic memory** and **file handling**
- **Markov Chains** for probabilistic movement
- **Game logic** and control flow

---

## 💡 Why This Project Matters
This project demonstrates:
- The ability to design a complete, interactive system in **C**
- Understanding of probability and **Markov Chain modeling**
- Strong fundamentals in control flow, data structures, and modular code  
- Creativity in translating a board game into executable logic  

It’s a great beginner-to-intermediate project that shows both **technical skill** and **algorithmic thinking** — perfect for a portfolio or GitHub showcase.

---

## 👨‍💻 Author
**Rares Făgădeanu**  
GitHub: [@raresstefan14](https://github.com/raresstefan14)

> Learning C programming, algorithms, and systems through hands-on projects that combine logic and creativity.

---

## 🚀 Future Improvements
- Add more players (3–4) or AI opponents  
- Implement property trading and card events  
- Save / load game states using files  
- Add visual enhancements (colors or basic GUI)  
- Analyze movement probabilities using **Markov transition matrices**

---

⭐ *If you enjoyed this project, give it a star on GitHub — it helps a lot!* ⭐
