# 🎲 Monopoly-Style Board Game (2 Players)

A console-based Monopoly-inspired board game for **two players**, built in **Python**.  
Created by **Rares Făgădeanu (@raresstefan14)**.

---

## 🧠 Project Overview

This project simulates a simplified Monopoly-style board game running in the terminal.  
Two players take turns rolling dice, moving around the board, buying properties, and paying rent — until one goes bankrupt.  

The player movement and decision system are modeled using **Markov Chains**, meaning that each game state (player position, balance, and ownership) depends only on the current state, providing a probabilistic and realistic simulation of board dynamics.

---

## 🧩 Key Features
- 🎲 Turn-based gameplay for two players  
- 💰 Property buying, ownership tracking, and rent collection  
- 🏦 Bank balance updates and bankruptcy detection  
- 🔁 Movement modeled using **Markov Chains** (state-based transitions)  
- 🖥️ Console-based interface with clear prompts and text output  
- 📊 Structured, modular Python code for easy understanding  

---

## ⚙️ How to Run

1. **Clone the repository:**
   ```bash
   git clone https://github.com/raresstefan14/Monopoly-Style-Board-Game-2-Players.git
   cd Monopoly-Style-Board-Game-2-Players
   ```

2. **Make sure you have Python 3 installed**, then run:
   ```bash
   python main.py
   ```

3. **Follow the on-screen instructions** to play.  

---

## 🕹️ Simplified Rules
- Each player starts with a set amount of money.  
- Players take turns rolling dice (probabilistic via Markov Chains).  
- If you land on an unowned property, you can buy it.  
- If you land on a property owned by your opponent, you pay rent.  
- The first player to go bankrupt loses.  

---

## 🧮 Technologies & Concepts Used
- **Python 3**
- **Markov Chains** for probabilistic state transitions  
- **OOP (Object-Oriented Programming)** for game logic  
- **Random module** for dice rolls  
- **Console input/output** for interaction  

---

## 📁 Project Structure
```
/Monopoly-Style-Board-Game-2-Players
  ├── main.py           # Entry point for the game
  ├── board.py          # Board setup and properties
  ├── player.py         # Player logic and balance tracking
  ├── game.py           # Turn handling and win conditions
  ├── utils.py          # Helper functions (Markov transitions, dice rolls)
  ├── README.md         # This file
```

---

## 💡 Why This Project Matters
This project demonstrates your ability to:
- Build a **complete game system** in Python  
- Apply **probabilistic modeling (Markov Chains)** in a fun context  
- Use **object-oriented design** and modular code  
- Combine **math, logic, and gameplay** into one coherent project  

It’s an excellent addition to your portfolio to show both technical and creative skills.

---

## 👨‍💻 Author
**Rares Făgădeanu**  
GitHub: [@raresstefan14](https://github.com/raresstefan14)

> Exploring Python, machine learning, and game design through hands-on projects that mix math and creativity.

---

## 🚀 Future Improvements
- Add AI or computer opponents  
- Add a save/load feature for ongoing games  
- Expand to more players (3–4)  
- Visualize Markov transitions or probabilities  
- Add a simple GUI using `tkinter` or `pygame`

---

⭐ *If you enjoyed this project, give it a star on GitHub — it helps a lot!* ⭐
