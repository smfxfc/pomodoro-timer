#! python3
import os
import time

from tkinter import Button
from popup_box import pomodoro_popup

cycle_minutes = int(input("How many minutes for each Pomodoro round? "))
break_minutes = int(input("How many minutes for each break between rounds? "))
#cycle_seconds = cycle_minutes * 60
break_seconds = break_minutes * 60
cycle_counter = cycle_minutes*60

def beepbeep():
	print('\007') # linux beep
	time.sleep(1)
	print('\007')


def start_cycle():
	pomodoro_cycle = 1
	pomodoro_round = 1
	while pomodoro_cycle <= 3: # change this value according to total number of pomodoro cycles user wants
		while pomodoro_round <= 4: # 4 rounds = 1 cycle
			print(f"Starting Pomodoro cycle #{pomodoro_cycle} round #{pomodoro_round}. Begin {cycle_minutes} minute countdown.")
			cycle_counter = cycle_minutes *60
			while cycle_counter > 0:
				cycle_counter -= 1 # set to higher value when testing
				#hours, seconds = divmod(cycle_counter, 3600)
				minutes, seconds = divmod(cycle_counter, 60)
				print(f"{minutes} minutes and {seconds} seconds remaining.")
				time.sleep(1)
			beepbeep()
			
			if pomodoro_round != 4: 
				break_counter = break_minutes *60
				pomodoro_popup(message=f"Pomodoro round #{pomodoro_round} complete. Take a {break_minutes} minute break.")
				while break_counter > 0:
					break_counter -= 1 # set to higher value when testing
					minutes, seconds = divmod(break_counter, 60)
					print(f"{minutes} minutes and {seconds} seconds remaining between rounds.")
					time.sleep(1)
			# create extra long break at the end of each full pomodoro cycle
			else:
				break_counter = break_minutes * 5 * 60
				pomodoro_popup(message=f"Pomodoro round #{pomodoro_round} complete. Take a {break_minutes*5} minute break.")
				while break_counter > 0:
					break_counter -= 1 # set to higher value when testing
					minutes, seconds = divmod(break_counter, 60)
					print(f"{minutes} minutes and {seconds} seconds remaining between rounds.")
					time.sleep(1)
			beepbeep()
			pomodoro_popup(message=f"Break #{pomodoro_round} complete.")
			pomodoro_round += 1
			#break_round += 1
		pomodoro_round = 1
		pomodoro_cycle += 1
		# TODO to fix this popup to not display if user completed final cycle 
		pomodoro_popup(message=f"Full pomodoro cycle #{pomodoro_cycle-1} complete. Press enter to begin pomodoro cycle #{pomodoro_cycle}.")


start_cycle()

pomodoro_popup(message="You have completed the last scheduled pomodoro cycle. Great job!")