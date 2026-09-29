from turtle import Screen
import time
from Snake import Snake, UP, DOWN, LEFT, RIGHT, MOVE_DISTANCE
from food import Food
from Score import Score
from agent import QLearningAgent

TRAINING = False
TRAINING_GAMES = 5000
SCREEN_LIMIT = 280
SAVE_EVERY = 100
WATCH_SPEED = 0.08

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("green")
screen.title("Snake AI - Q Learning")

if TRAINING:
    screen.tracer(0, 0)
else:
    screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Score()
agent = QLearningAgent()

game_number = 1
steps_without_food = 0
ai_best_score = 0


def point_is_dangerous(x, y):
    if (
        x > SCREEN_LIMIT
        or x < -SCREEN_LIMIT
        or y > SCREEN_LIMIT
        or y < -SCREEN_LIMIT
    ):
        return True

    for segment in snake.segment[1:]:
        if segment.distance(x, y) < 10:
            return True

    return False


def next_point_for_heading(heading):
    x = snake.head.xcor()
    y = snake.head.ycor()

    if heading == RIGHT:
        x += MOVE_DISTANCE
    elif heading == LEFT:
        x -= MOVE_DISTANCE
    elif heading == UP:
        y += MOVE_DISTANCE
    elif heading == DOWN:
        y -= MOVE_DISTANCE

    return x, y


def relative_headings():
    heading = int(snake.head.heading())

    right_turn = {
        RIGHT: DOWN,
        DOWN: LEFT,
        LEFT: UP,
        UP: RIGHT,
    }

    left_turn = {
        RIGHT: UP,
        UP: LEFT,
        LEFT: DOWN,
        DOWN: RIGHT,
    }

    return heading, right_turn[heading], left_turn[heading]


def get_state():
    straight, right, left = relative_headings()

    sx, sy = next_point_for_heading(straight)
    rx, ry = next_point_for_heading(right)
    lx, ly = next_point_for_heading(left)

    head_x = snake.head.xcor()
    head_y = snake.head.ycor()

    return (
        int(point_is_dangerous(sx, sy)),
        int(point_is_dangerous(rx, ry)),
        int(point_is_dangerous(lx, ly)),
        int(food.xcor() < head_x),
        int(food.xcor() > head_x),
        int(food.ycor() < head_y),
        int(food.ycor() > head_y),
    )


def perform_action(action):
    straight, right, left = relative_headings()
    new_heading = (straight, right, left)[action]
    snake.head.setheading(new_heading)


def has_died():
    if (
        snake.head.xcor() > SCREEN_LIMIT
        or snake.head.xcor() < -SCREEN_LIMIT
        or snake.head.ycor() > SCREEN_LIMIT
        or snake.head.ycor() < -SCREEN_LIMIT
    ):
        return True

    for segment in snake.segment[1:]:
        if snake.head.distance(segment) < 10:
            return True

    return False


def reset_game():
    global game_number
    global steps_without_food
    global ai_best_score

    current_score = scoreboard.score

    if current_score > ai_best_score:
        ai_best_score = current_score
        agent.save()

    scoreboard.reset()
    snake.reset()
    food.refresh()

    steps_without_food = 0

    if TRAINING:
        agent.end_game()

    game_number += 1

    if TRAINING and game_number % SAVE_EVERY == 0:
        agent.save()

    if TRAINING and game_number % 100 == 0:
        print(
            f"Game {game_number}/{TRAINING_GAMES} | "
            f"AI Best {ai_best_score} | "
            f"Epsilon {agent.epsilon:.3f} | "
            f"States {len(agent.q_table)}"
        )

    screen.title(
        f"Snake AI | Game {game_number} | AI Best {ai_best_score}"
    )


if not TRAINING:
    agent.epsilon = 0


while True:

    if TRAINING and game_number > TRAINING_GAMES:
        agent.save()

        print()
        print("Training complete")
        print(f"Games: {TRAINING_GAMES}")
        print(f"AI best score: {ai_best_score}")
        print(f"States learned: {len(agent.q_table)}")
        print()
        print("Change TRAINING = False to watch the AI.")

        break

    if not TRAINING:
        screen.update()
        time.sleep(WATCH_SPEED)

    state = get_state()

    old_distance = snake.head.distance(food)

    action = agent.choose_action(state)

    perform_action(action)

    snake.move()

    new_distance = snake.head.distance(food)

    steps_without_food += 1

    done = has_died()

    if done:
        reward = -100

    elif snake.head.distance(food) < 15:
        reward = 100

        food.refresh()
        scoreboard.increasesocre()
        snake.extend()

        steps_without_food = 0

    elif new_distance < old_distance:
        reward = 1

    else:
        reward = -1

    if steps_without_food > 250 + len(snake.segment) * 30:
        reward = -50
        done = True

    next_state = get_state()

    if TRAINING:
        agent.learn(
            state,
            action,
            reward,
            next_state,
            done,
        )

    if done:
        reset_game()


screen.update()
screen.exitonclick()