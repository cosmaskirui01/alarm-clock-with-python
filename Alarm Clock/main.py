import time
import datetime
import pygame


def set_alarm(alarm_time):
    print("Setting alarm to " + str(alarm_time))
    sound_file = "my_music.mp3"
    running = True

    while running:
        currentTime = datetime.datetime.now().strftime("%H:%M:%S")
        print(currentTime)

        if currentTime == alarm_time:
            print("Wake up")
            pygame.mixer.init()
            pygame.mixer.music.load(sound_file)
            pygame.mixer.music.play()

            while pygame.mixer.music.get_busy():
                time.sleep(1)


            running = False

        time.sleep(1)




if __name__ == '__main__':
    alarm_time = input("enter alarm time(HH:MM:SS): ")
    set_alarm(alarm_time)