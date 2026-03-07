  <img width="690" height="208" alt="image" src="https://github.com/user-attachments/assets/dabfe902-eea2-46d9-88cd-7c1d7b685890" />
                                                  
                                                       
# Hill Climbing Maze Solver
A visualization of the **Hill Climbing Search Algorithm** solving a randomly generated maze using **Python** and **Pygame**.

The agent starts from the **top-left corner** of the maze and attempts to reach the **goal at the bottom-right corner** by always moving toward the cell with the **lowest heuristic value (Manhattan distance)**.

This project demonstrates how **local search algorithms** work and also highlights one of their key limitations — **getting stuck at local maxima**.

---

## Features

* Random maze generation
* Visualization using Pygame
* Hill Climbing heuristic search
* Path tracking visualization
* Detection of local maxima (stuck state)
* Reset maze functionality

---

## Algorithm Used

### Hill Climbing

Hill Climbing is a **greedy local search algorithm** used in Artificial Intelligence.

The algorithm works as follows:

1. Start from an initial position.
2. Look at neighboring cells.
3. Calculate the heuristic value for each neighbor.
4. Move to the neighbor with the lowest heuristic value.
5. Repeat until:

   * The goal is reached
   * No better neighbor exists (**local maximum**)

---

## Heuristic Function

The algorithm uses **Manhattan Distance** as the heuristic.

h(n) = |x₁ − x₂| + |y₁ − y₂|

Where:

* **(x₁, y₁)** → Current position
* **(x₂, y₂)** → Goal position

---

## Technologies Used

* Python
* Pygame
* Artificial Intelligence (Search Algorithms)

---

## Requirements

* Python 3.x
* pygame==2.5.2

---

## Installation

Clone the repository:

```bash
git clone https://github.com/aafeefarahman/Hill-Climbing-Maze-Solver.git
```

Navigate to the project folder:

```bash
cd Hill-Climbing-Maze-Solver
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Running the Project

Run the following command:

```bash
python main.py
```

The maze visualization window will open and the agent will start solving the maze automatically.

---

## Output Visualization
<img width="448" height="471" alt="image" src="https://github.com/user-attachments/assets/12902f4a-68f5-46aa-bbac-9d2142600e67" />
<img width="447" height="468" alt="image" src="https://github.com/user-attachments/assets/537f3eb4-f502-4571-9638-2fac7b501c31" />

---

## Controls

| Key | Action         |
| --- | -------------- |
| R   | Reset the maze |

---

## Limitation

Hill Climbing can get stuck in a **local maximum**, meaning the algorithm may stop before reaching the goal if no neighboring cell has a better heuristic value.

This behavior demonstrates an important drawback of **greedy search algorithms**.

---

## Learning Outcomes

This project demonstrates:

* Local Search Algorithms
* Heuristic Functions
* AI Pathfinding
* Visualization using Python and Pygame

---
