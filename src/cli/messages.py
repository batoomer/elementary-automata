LOGO = """\033[94m
███████╗██╗     ███████╗███╗   ███╗███████╗███╗   ██╗████████╗ █████╗ ██████╗ ██╗   ██╗
██╔════╝██║     ██╔════╝████╗ ████║██╔════╝████╗  ██║╚══██╔══╝██╔══██╗██╔══██╗╚██╗ ██╔╝
█████╗  ██║     █████╗  ██╔████╔██║█████╗  ██╔██╗ ██║   ██║   ███████║██████╔╝ ╚████╔╝ 
██╔══╝  ██║     ██╔══╝  ██║╚██╔╝██║██╔══╝  ██║╚██╗██║   ██║   ██╔══██║██╔══██╗  ╚██╔╝  
███████╗███████╗███████╗██║ ╚═╝ ██║███████╗██║ ╚████║   ██║   ██║  ██║██║  ██║   ██║   
╚══════╝╚══════╝╚══════╝╚═╝     ╚═╝╚══════╝╚═╝  ╚═══╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   
                                                                                       
 █████╗ ██╗   ██╗████████╗ ██████╗ ███╗   ███╗ █████╗ ████████╗ █████╗ 
██╔══██╗██║   ██║╚══██╔══╝██╔═══██╗████╗ ████║██╔══██╗╚══██╔══╝██╔══██╗
███████║██║   ██║   ██║   ██║   ██║██╔████╔██║███████║   ██║   ███████║
██╔══██║██║   ██║   ██║   ██║   ██║██║╚██╔╝██║██╔══██║   ██║   ██╔══██║
██║  ██║╚██████╔╝   ██║   ╚██████╔╝██║ ╚═╝ ██║██║  ██║   ██║   ██║  ██║
╚═╝  ╚═╝ ╚═════╝    ╚═╝    ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝
\033[0m"""

HEADER = """
Welcome to the Elementary Automata Simulator!
---------------------------------------------

This program simulates the evolution of elementary cellular automata. It asks for the size of the automata grid, 
a rule number, and the type of boundary condition to be applied. The automata will evolve over a specified number
of generations."""

INTRO = """
Elementary Automata
-------------------

Elementary cellular automata are simple models of computation consisting of a row of cells, 
each of which can be in one of two states dead or alive (0 or 1). The state of each cell in 
the next generation depends on its current state and the state of its two immediate neighbors, 
according to a specific rule."""

RULESET_EXPLANATION = """
Rules and Rulesets
------------------

A rule in elementary cellular automata specifies the state of a cell based on the states of 
its neighbors. There are 256 possible rules, numbered from 0 to 255. Each rule can be represented 
as an 8-bit binary number, where each bit specifies the new state of a cell for a particular 
combination of neighbor states.

For example, Rule 30 can be represented as follows:


Current Pattern     New State
---------------     ---------
     ■■■                □    
     ■■□                □    
     ■□■                □    
     ■□□                ■    
     □■■                ■    
     □■□                ■    
     □□■                ■    
     □□□                □    


where, ■ represents state 1 (alive) and □ represents state 0 (dead). Thus, the corresponding binary 
representation of Rule 30 is 00011110."""


BOUNDARY_EXPLANATION = """
Boundary Conditions
-------------------

Boundary conditions define how the edges of the automaton grid behave. There are several types:
"""

FIXED_BOUNDARY_EXPLANATION = """
1. Fixed Boundary Condition

In a fixed boundary condition, the boundary values are fixed and do not change
regardless of the state of the system. The fixed values are typically 0 (dead) or 1 (alive).


Fixed state                                          Fixed State
    v                                                    v      
+-------┋+------+------+------+- ••• -+------+------+┋-------+  
|  0/1  ┋|  X1  |  X2  |  X3  |  •••  | Xn-1 |  Xn  |┋  0/1  |  
+-------┋+------+------+------+- ••• -+------+------+┋-------+
"""

REFLEXIVE_BOUNDARY_EXPLANATION = """
2. Reflexive Boundary Condition

In a reflexive boundary condition, the boundary values are a reflection of the neighboring values, 
essentially mirroring the adjacent cell value


     --- Reflexive ---                    --- Reflexive ---   
     |               |                    |               |   
     v               v                    v               v   
+-------┋+------+------+------+- ••• -+------+------+┋-------+
|  X2   ┋|  X1  |  X2  |  X3  |  •••  | Xn-1 |  Xn  |┋  Xn-1 |
+-------┋+------+------+------+- ••• -+------+------+┋-------+
"""

ADIABATIC_BOUNDARY_EXPLANATION = """
3. Adiabatic Boundary Condition

In an adiabatic boundary condition, the boundary values are set to the value of the adjacent cell itself,
representing an insulated boundary.


    Adiabatic                                    Adiabatic       
    |       |                                    |       |    
    v       v                                    v       v    
+-------┋+------+------+------+- ••• -+------+------+┋-------+
|  X1   ┋|  X1  |  X2  |  X3  |  •••  | Xn-1 |  Xn  |┋  Xn-1 |
+-------┋+------+------+------+- ••• -+------+------+┋-------+
"""

PERIODIC_BOUNDARY_EXPLANATION = """
4. Periodic Boundary Condition

In a periodic boundary condition, the boundaries are connected to form a loop. The first cell is adjacent 
to the last cell, creating a continuous, cyclic system.


    -------------------Periodic-------------------            
    |                                            |            
    v                                            v            
+-------┋+------+------+------+- ••• -+------+------+┋-------+
|  Xn   ┋|  X1  |  X2  |  X3  |  •••  | Xn-1 |  Xn  |┋   X1  |
+-------┋+------+------+------+- ••• -+------+------+┋-------+
            ^                                            ^    
            |                                            |    
            -------------------Periodic-------------------    
                                
                                
For more information refer to: \033[96mhttps://mathworld.wolfram.com/ElementaryCellularAutomaton.html\033[0m
"""

SECTIONS = [
    f"{LOGO}\n\n{HEADER}",
    INTRO,
    RULESET_EXPLANATION,
    BOUNDARY_EXPLANATION,
    FIXED_BOUNDARY_EXPLANATION,
    REFLEXIVE_BOUNDARY_EXPLANATION,
    ADIABATIC_BOUNDARY_EXPLANATION,
    PERIODIC_BOUNDARY_EXPLANATION
]








