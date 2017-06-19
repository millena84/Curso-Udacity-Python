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

import	pymsgbox
import	time
import	webbrowser
import	ctypes

qtd_min_trab == pymsgbox.prompt("Digite quantos minutos durarao sua sessão de trabalho:", "Tempo de trabalho")
qtd_intervalos == pymsgbox.prompt("Digite quantos intervalos quer fazer:", "Quantidade de intervalos")
qtd_min_intervalo == pymsgbox.prompt("Digite o quantos minutos durarão seu intervalo:", "Duração do intervalo")

# MELHORIA: definir tempo mínimo de trabalho
qtd_min_pre_intervalo = int(qtd_min_trab) - 5

contador_intervalos = 1

pymsgbox.alert(text="Hora de início do programa: "+time.ctime(), title="Break time")

#	enquanto o programa ainda não atingiu a quantidade de intervalos proposta pelo usuário
while int(contador_intervalos) <= int(qtd_intervalos) :
	# coloca o programa para aguardar o tempo informado pelo usuário
	# (qtd_min_pre_intervalo * 60)
	time.sleep(5)
	pymsgbox.alert(text="Faltam 5 minutos para o seu intervalo", title="Atenção!")
	# 5 minutos antes do intervalo, avisa o usuário
	# 5 minutos (5 * 60)
	time.sleep(5)
	# Avisa que chegou a hora do intervalo
	pymsgbox.alert(text="Hora do intervalo", title="Atenção")
	# abre o video do youtube
	webbrowser.open("https://www.youtube.com/watch?v=DLHAiojuUq0")
	# coloca o programa para aguardar o tempo do intervalo
	time.sleep(int(qtd_min_intervalo))
	# se a quantidade de intervalos ainda não atingiu o total informado pelo usuário
	if int(contador_intervalos) < int(qtd_intervalos) :
		pymsgbox.alert(text="Agora voltemos ao trabalho!", title="Aviso")
	else :
		pymsgbox.alert(text="Ótimo! por hoje chega :)", title="Agora vá descansar :)")
	contador_intervalos = contador_intervalos + 1