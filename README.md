# Elementary Cellular Automaton Simulator

Welcome to the Elementary Cellular Automaton Simulator! This console application simulates the evolution of elementary cellular automata.

## Features

- **Interactive User Input**: The application guides you through providing necessary inputs.
- **Input Validation**: Ensures that user inputs are valid.
- **Configurable Settings**: Specify the size of the automaton, rule number, boundary conditions, and number of generations.
- **Visual Representation**: Displays the evolution of the automaton generation by generation.

## Getting Started

### Prerequisites

- Python 3.9 installed on your system

### Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/batoomer/elementary-automata.git
    cd elementary-cellular-automaton
    ```

### Running the Application

1. Navigate to the project directory:
    ```bash
    cd elementary-automata
    ```

2. Run the application:
    ```bash
    python3 main.py
    ```

3. Follow the on-screen prompts to provide the required inputs:
    - **Size**: Enter the number of cells in the automaton (must be a positive integer).
    - **Rule**: Enter the rule number (must be between 0 and 255).
    - **Boundary Condition**: Choose from 'fixed_dead', 'fixed_alive', 'periodic', 'adiabatic', 'reflexive'.
    - **Generations**: Enter the number of generations to simulate (must be a positive integer).

4. Watch the automaton evolve.

### Boundary Conditions

- **fixed_dead**: The boundaries are always dead (0).
- **fixed_alive**: The boundaries are always alive (1).
- **periodic**: The boundaries wrap around, connecting the first and last cells.
- **adiabatic**: The boundaries take the state of the first and last cells respectively.
- **reflexive**: The boundaries take the state of the second and second-to-last cells respectively.


