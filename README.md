# Daily Reflection Tree

This repository contains the solution for the DeepThought Role Simulation Assignment.

## Project Structure

```
.
├── tree/
│   ├── reflection-tree.json       # Part A: the deterministic decision tree data
│   └── tree-diagram.md            # Part A: visual diagram using Mermaid.js
├── agent/
│   └── main.py                    # Part B: runnable Python CLI agent
├── transcripts/
│   ├── persona-1-transcript.md    # Sample run (Victim/Entitled/Self-centric)
│   └── persona-2-transcript.md    # Sample run (Victor/Contributing/Altrocentric)
├── write-up.md                    # Part A: design rationale and psychological grounding
└── README.md                      # Instructions to run the project
```

## Part A: The Tree Data
The reflection tree is defined entirely in `tree/reflection-tree.json`. It is a deterministic state machine composed of nodes. The available node types are:
- `start`, `end`: Boundary nodes for the session.
- `question`: Prompts the user with predefined choices and calculates trait signals based on their answers.
- `decision`: Evaluates accumulated state (e.g. `axis1.dominant:internal`) or previous answers to route the user down the appropriate branch.
- `reflection`: Delivers a reframing statement constructed through answer interpolation.
- `bridge`: A transitional node bridging to the next psychological axis.
- `summary`: Synthesizes the user's choices into a single wrap-up reflection at the end.

## Part B: The Agent
The `agent/main.py` script serves as the interactive runtime for the tree.

**Key constraints respected:**
- 0 LLM API calls are made during runtime.
- Traversal is entirely deterministic.
- State is accumulated by evaluating signals configured in the tree JSON.

### How to Run
Ensure you have Python 3 installed. No external dependencies are required.

```bash
cd agent
python3 main.py
```

Or you can run it from the root directory by passing the path to the JSON file:
```bash
python3 agent/main.py tree/reflection-tree.json
```

## Psychological Grounding
This tree forces participants to evaluate themselves along three interconnected axes:
1. **Locus (Victim vs Victor):** Julian Rotter's Locus of Control.
2. **Orientation (Contribution vs Entitlement):** Psychological Entitlement vs Organ's Organizational Citizenship Behavior.
3. **Radius (Self-Centrism vs Altrocentrism):** Maslow's Self-Transcendence.

For detailed insight into the design decisions made for this architecture, please read `write-up.md`.
