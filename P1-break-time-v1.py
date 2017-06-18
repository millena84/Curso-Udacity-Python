#####################################################################
#																	#
#	Exercise for the Udacity course "Programming Foundations with 	#
#	Python"															#
#   Lesson 2: Use functions - P1: Take a break project				#
#	--------------------------------------------------				#
#																	#
#	This exercise is an evolution of udacity exercise. In this 		#
#	program we will: 												#
#	will:															#
#	1)	Receive how many times the user wants to take a break;		#
#	2)	Receive how many minutes the user wants to stay in the 		#
#		computer (and then, take a break);							#
#	x)	Push the button to start the program;						#
#	3) 	The program will show a message, with the time of the 		#
#		beginning;													#
#	4)	5 minutes before the time that the user choose to take a 	#
#		break 														#
#	5)	When the break time comes, the program will open a browser 	#
#		with a video (that can be choosen by the user but not now)	#
#	6)	The break takes 5 minutes. Then will appear a message to go #
#		back to	work												#
#	7)	This loop will execute how many times the user put in the 	#
#		beginning													#
#																	#
#===================================================================#
#																	#
#	Modules that we use in this program:							#
#	- webbrowser													#
#	- times		 													#
#	- ctypes														# 
#																	#
#	Functions used in this program:									#
#	- webbrowser.open = open the browser with a URL that ask for. 	#
#	  sintax: webbrowser.open("URL")								#
#	- time.sleep = makes the program sleep for a number off seconds	#
#	  sintax: time.sleep(seconds)									#
#	- ctypes.windll.user32.MessageBox = 
#	  sintax: 
#	- 
#																	#
#####################################################################

import	time
import	webbrowser
import	ctypes

