# pip install --upgrade pip setuptools wheel
# if not install try above command

from playsound import playsound
import time

# for terminal clear and return the latest value on single line

CLEAR = "\033[2J"
CLEAR_AND_RETURN = "\033[H"


def alaram(seconds):
    time_elapsed = 0
    print(CLEAR)
    while time_elapsed < seconds:
        time.sleep(1)
        time_elapsed += 1
        
        time_left = seconds - time_elapsed
        minutes_left = time_left // 60
        seconds_left = time_left % 60
        
        print(f"{CLEAR_AND_RETURN} Alaram Sounds in: {minutes_left:02d}:{seconds_left:02d}")
    playsound("core-project\OOPS\Alaram.mp3")


minutes = int(input("How many minutes to wait: "))
seconds = int(input("How many seconds to wait: "))
time_in_seconds = minutes * 60 + seconds
alaram(time_in_seconds)
# playsound("C:\PythonProjects\core-project\OOPS\Alaram.mp3")
