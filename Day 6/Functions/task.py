def get_user_name():
    print("Hello")
    name = input("What is your name?\n")
    print("Hello")
    print(name+"!")


get_user_name()

# Hurdle 4
# think(100)
#
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
#
# def jump():
#     turn_right()
#     move()
#     turn_right()
#     move()
#
# while not at_goal():
#     if right_is_clear():
#         jump()
#     elif front_is_clear():
#         move()
#     elif not front_is_clear() and not right_is_clear():
#         turn_left()


# Maze solution 1
#
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
# while not at_goal():
#     turn_right()
#         if wall_in_front():
#             turn_left()
#             if wall_in_front():
#                 turn_left()
#             else:
#                 move()
#         else:
#             move()

# Maze solution 2
#
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
#
#
# while not at_goal():
#     if right_is_clear():
#         turn_right()
#         move()
#     elif front_is_clear():
#         move()
#     else:
#         turn_left()

# Infinite Loop Solution (all three problems)
#
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
# infinite_loop_blocker = 0
# while not at_goal():
#     if infinite_loop_blocker > 23:
#         infinite_loop_blocker -= 1
#         if front_is_clear():
#             move()
#         else:
#             turn_right()
#             if front_is_clear():
#                 move()
#             else:
#                 turn_right()
#                 turn_right()
#     elif right_is_clear():
#         turn_right()
#         move()
#         infinite_loop_blocker += 1
#     elif front_is_clear():
#         move()
#     else:
#         turn_left()

