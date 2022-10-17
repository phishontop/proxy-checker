import core
import threading
import time

THREADS = 500
TIMEOUT = 5


def loadProxies():
    with open("proxies.txt") as file:
        lines = file.readlines()
        return [line.rstrip() for line in lines]

def checkProxy(proxy):
    try:
        checker = core.Checker(proxy, timeout=TIMEOUT)
        valid = checker.check()
        if valid:
            print(f"[VALID] {proxy}")
            with open("valid.txt", "a") as validFile:
                validFile.write(f"{proxy}\n")

    except:
        print(f"[ERROR] {proxy}")

proxies = loadProxies()
for proxy in proxies:
    threading.Thread(target=checkProxy, args=(proxy,)).start()
    time.sleep(TIMEOUT/THREADS)
    
