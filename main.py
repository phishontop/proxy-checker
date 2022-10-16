import core
import threading
import time

THREADS = 1000
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
threads = []
for proxy in proxies:
    threads.append(threading.Thread(target=checkProxy, args=(proxy,)))

for thread in threads:
    time.sleep(TIMEOUT/THREADS)
    thread.start()

for thread in threads:
    thread.join()

