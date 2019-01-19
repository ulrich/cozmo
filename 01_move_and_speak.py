#!/usr/bin/env python3

import cozmo

from cozmo.util import degrees, distance_mm, speed_mmps

def cozmo_program(robot_a_nico: cozmo.robot.Robot):
    # avance de 20 cm
    robot_a_nico.drive_straight(distance_mm(200), speed_mmps(50)).wait_for_completed()

    # on le fait tourner en rond
    robot_a_nico.turn_in_place(degrees(360)).wait_for_completed()

    # remet la tete normalement
    robot_a_nico.set_head_angle(degrees(0)).wait_for_completed()

    # leve la tete
    robot_a_nico.move_head(1)

    # fait parler cozmo
    robot_a_nico.say_text("Salut les amis comment allez-vous ? Mois je vais bien.").wait_for_completed()
    robot_a_nico.say_text("Je vais dessiner un carré pour vous en Python").wait_for_completed()

    for _ in range(4):
        robot_a_nico.drive_straight(distance_mm(150), speed_mmps(150)).wait_for_completed()
        robot_a_nico.turn_in_place(degrees(90)).wait_for_completed()

    robot_a_nico.say_text("Maintenant vous devez deviner ma figure !").wait_for_completed()

    for _ in range(3):
        robot_a_nico.drive_straight(distance_mm(200), speed_mmps(150)).wait_for_completed()
        robot_a_nico.turn_in_place(degrees(120)).wait_for_completed()

    robot_a_nico.say_text("Merci !!!").wait_for_completed()

    chosen_triggers = [trigger for trigger in robot_a_nico.anim_triggers if 'WinGame' in trigger.name]
    
    for trigger in chosen_triggers:
        robot_a_nico.play_anim_trigger(trigger).wait_for_completed()

cozmo.run_program(cozmo_program)
