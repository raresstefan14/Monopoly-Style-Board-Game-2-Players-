# Monopoly-Style-Board-Game-2-Players-
This is a simple Python implementation of a Monopoly-style board game for two players. The game uses tkinter for the GUI, numpy for statistical tracking, and matplotlib for visualizing move frequencies.

Features

A board of 40 positions (as in classic Monopoly).

Two players take turns rolling two dice and moving around the board.

Passing “Start” awards 200 units of currency.

Properties can be purchased when landed on and still available.

When a player lands on a property owned by the other, rent is paid.

Special squares trigger actions: e.g., “Go to Jail”, “Luxury Tax”.

Tracks how many times each board position has been visited; you can display a bar chart of visit frequencies.

Buttons for “Next Turn”, “Buy Property” and “Show Frequencies” are positioned on the right side of the board for better layout usability.

Usage

Install required packages: numpy, matplotlib.

Run python monopoly.py (or whatever you name the file).

Use the “Next Turn” button to advance the turn.

When the “Buy Property” button becomes enabled, you may purchase the property you have landed on.

At any time you can click “Show Frequencies” to view a frequency chart of landed-on positions.

Folder Structure
/monopoly-game
   README.md
   monopoly.py

Why place buttons on the right?

The typical layout places control buttons below the board, which can make the board appear squashed or crowded. By moving the controls to the right, the board remains central and clear, and controls are more accessible.

Possible Enhancements

Support for more than 2 players.

More complex property ownership/rent logic (houses/hotels).

Better UI styling, icons for properties.

Markov Chain Model
The game’s board is modelled as a discrete‐time Markov chain with 40 states (one per board square).
A transition-matrix P is computed whereeach entry 
𝑃
𝑖
𝑗
P
ij
	​

 represents the probability of moving from square i to square j in one turn (via dice roll).
Because the next state depends only on the current state and not on the full move history, the chain satisfies the “memoryless” (Markov) property.
Tracking the number of landings per square (via vizite_casete) provides an empirical estimate of the long-run state-visit probabilities, giving insights into which squares are most frequently occupied and thus potentially highest strategic value.

Save/load game state.

Network multiplayer support.
