#healthy programmer
from pygame import mixer
from datetime import datetime
from time import time
def musiconloop(file,stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        a=input()
        if a == stopper:
            mixer.music.stop()
            break
def log_now(msg):
    with open("mylogs.txt","a")as f:
        f.write(f"{msg}  {datetime.now()} \n")
if __name__ == '__main__':
    # musiconloop("python.mp3","stop")
    init_water=time()
    init_eye = time()
    init_exercise=time()
    watersecs=5
    eyesecs=10
    exercisesecs=20
    while True:
        if time()-init_water > watersecs:
            print("Water drinking time. Enter 'drank' to stop alarm")
            musiconloop("water.mp3","drank")
            init_water=time()
            log_now("water drinking time is : ")
        if time()-init_eye > eyesecs:
            print("Eye exercise time. Enter 'eyedone' to stop alarm")
            musiconloop("eyes.mp3","eyedone")
            init_eye=time()
            log_now("eye exercise time is : ")
        if time()-init_exercise > exercisesecs:
            print("Exercise time. Enter 'done' to stop alarm")
            musiconloop("exercise.mp3","done")
            init_exercise=time()
            log_now("exercise time is : ")


