import time

def stamp():
    now = time.localtime(time.time())
    fmtnow = time.strftime('%Y-%m-%d %H:%M:%S %a',now)
    return fmtnow

if __name__=='__main__':
    print(stamp())

