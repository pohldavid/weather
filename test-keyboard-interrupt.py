import sys
from time import sleep


try:
    while True:
        print('trying')
        sleep(1)
except KeyboardInterrupt:
    print('keyboard interrupt')
    sys.exit()
