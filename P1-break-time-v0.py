# file time: to use functions related to the time (lol). In this program, we use to calculate the time that the program should sleep before show the alert
import time
# file webbrower to use functions related to the browser ot internet. In this program, we used to open de browser when the user is at the computer for 25 minutes
import webbrowser
# file ctypes. In this program, we use to show some alert before open the browser.
import ctypes  


# how many times I want this program show the alert? 
# 31-03: try (after) to open a textbox to the user, so he can choose how many times
total_breaks = 3
# starts always in one
break_count = 1
# how many minutes I want to work before stop?
total_minutes_to_stop = 5 # the programa will wait for 20 minutes to show the alert, and after 5 minutes after show the alert, will show the video
# how many minutes after start to work did I want to show the alert?
total_minutes_firt_alert = 20
# how many minutes to you want to stop before return to work?
total_minutes_stopped = 5

print("Questo programma ha cominciato alle "+time.ctime())
while break_count <= total_breaks : 
    time.sleep(60 * 20)
    ctypes.windll.user32.MessageBoxW(0, "Ciao! Dopo più 5 minute, bisogni da fare una pausa di 5 minute, va bene?", "Mancano 5 minute!", 1)
    time.sleep(60 * 5)
    webbrowser.open("https://www.youtube.com/watch?v=zpXJRL0glbI")
    time.sleep(60 * 5)
    if break_count < total_breaks :
        ctypes.windll.user32.MessageBoxW(0, "Brava! Ora, torniamo a lavorare!", "É finita la pausa!", 1)
    else :
        ctypes.windll.user32.MessageBoxW(0, "Brava! Per ora, basta!", "É finito il lavoro :)", 1)
    break_count = break_count + 1
