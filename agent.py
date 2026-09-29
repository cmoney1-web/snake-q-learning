import json
import os
import random

MODEL_FILE = "q_table.json"


class QLearningAgent:
    def __init__(
        self,
        learning_rate=0.2,
        discount=0.9,
        epsilon=1.0,
        epsilon_decay=0.998,
        min_epsilon=0.05,
    ):
        self.learning_rate = learning_rate
        self.discount = discount
        self.epsilon = epsilon
        self.epsilon_decay = epsilon_decay
        self.min_epsilon = min_epsilon
        self.q_table = {}
        self.load()

    def _key(self, state):
        return "".join(str(int(x)) for x in state)

    def values(self, state):
        key = self._key(state)

        if key not in self.q_table:
            self.q_table[key] = [0.0, 0.0, 0.0]

        return self.q_table[key]

    def choose_action(self, state):
        if random.random() < self.epsilon:
            return random.randrange(3)

        q_values = self.values(state)

        return q_values.index(max(q_values))

    def learn(self, state, action, reward, next_state, done):
        current = self.values(state)[action]

        if done:
            future = 0
        else:
            future = max(self.values(next_state))

        target = reward + self.discount * future

        self.values(state)[action] += self.learning_rate * (target - current)

    def end_game(self):
        self.epsilon = max(
            self.min_epsilon,
            self.epsilon * self.epsilon_decay,
        )

    def save(self):
        with open(MODEL_FILE, "w") as file:
            json.dump(
                {
                    "epsilon": self.epsilon,
                    "q_table": self.q_table,
                },
                file,
            )

    def load(self):
        if os.path.exists(MODEL_FILE):
            try:
                with open(MODEL_FILE) as file:
                    data = json.load(file)

                self.q_table = data.get("q_table", {})
                self.epsilon = data.get(
                    "epsilon",
                    self.epsilon,
                )

            except (json.JSONDecodeError, OSError):
                self.q_table = {}
