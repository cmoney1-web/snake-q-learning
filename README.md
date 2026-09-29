# Snake AI - Q-Learning

A Python Snake game featuring an AI agent trained using **Q-learning and reinforcement learning**. The agent learns through repeated gameplay to find food, avoid collisions, and improve its decisions over time.

## How It Works

The AI uses a Q-table to learn which actions are best in different situations. It can:

- Move straight
- Turn left
- Turn right

The agent receives rewards for eating food and moving towards it, while receiving penalties for collisions and poor movements.

An **epsilon greedy strategy** is used during training so the agent can balance exploring new actions with using what it has already learned.

## Features

- Q-learning reinforcement learning agent
- Reward and penalty system
- Epsilon-greedy exploration
- Collision detection
- Automatic AI training
- Persistent Q-table storage
- Python Turtle graphical interface

## Technologies

- Python
- Turtle
- Q-Learning
- Reinforcement Learning
- Git & GitHub

## Running the Project

Run the game with:

```bash
python main.py
```

To train the AI:

```python
TRAINING = True
```

To watch the trained AI:

```python
TRAINING = False
```

The project currently trains the agent over **5,000 games** and saves its learned Q-values locally.

## What I Learned

This project gave me practical experience implementing reinforcement learning, designing reward systems, balancing exploration and exploitation, and integrating an AI agent into an existing Python game.
