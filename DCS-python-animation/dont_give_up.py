import sys, time

message = " Don't give up!\n Think hard! \nOr have a guess if you're unsure~"

def typewriter(message):
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()
        
        if char !="\n":
            time.sleep(0.1)
        else:
            time.sleep(1)

typewriter(message)