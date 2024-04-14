import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(600, 600)
screen.tracer(0)
player = Player()

screen.listen()
screen.onkeypress(key="Up", fun=player.go_up)
car_manager = CarManager()
scoreboard = Scoreboard()

is_game_on = True
while is_game_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()

    # Detect collision with the car(measures the distance from the center of the car to the center of the player(turtle)
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            scoreboard.game_over()
            is_game_on = False

    # Detect successful crossing
    if player.is_successful_crossing():
        player.go_to_start_position()
        car_manager.speed_up()
        scoreboard.increase_level()

screen.exitonclick()
