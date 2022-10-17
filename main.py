import threading
import time
import core
import os
import requests
from multiprocessing import Pool, current_process

THREADS = 50
TIMEOUT = 5
PROXIES_FILE = "proxies.txt"
VALID_FILE = "multiprocessing_valid.txt"
VALID_PROXIES = []

def loadProxies():
    lines = []
    with open(PROXIES_FILE) as file:
        lines = file.readlines()
    return [line.rstrip() for line in lines]

def checkProxy(proxy):
    try:
        checker = core.Checker(proxy, timeout=TIMEOUT)
        valid = checker.check()
        if valid:
            print(f"[VALID] {proxy}")
            VALID_PROXIES.append(proxy)
        
    except:
        print(f"[ERROR] {proxy}")

def writeValid():
    if len(VALID_PROXIES) > 0:
        with open(VALID_FILE, "a") as file:
            for validProxy in VALID_PROXIES:
                file.write(f'{validProxy}\n')
            print('[+] Saved valid proxies...')
        print(f'[+] Done!')
    else:
        print('[!] No valid proxies...')

if __name__ == "__main__":    
    with Pool(THREADS) as pool:
        arguments = (proxy for proxy in loadProxies())
        pool.map(checkProxy, arguments)
    
    writeValid()
