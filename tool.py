#!/usr/bin/env python3

# =======================
# IMPORTS
# =======================
import re
import socket
import time
import sys

# =======================
# VERSION
# =======================
VERSION = "1.0"

# =======================
# FUNCTIONS
# =======================

def is_valid_url(url):
    pattern = re.compile(
        r'^(https?:\/\/)?'
        r'([a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}'
        r'(\/.*)?$'
    )
    return re.match(pattern, url)


def internet_available():
    try:
        socket.create_connection(("8.8.8.8", 53), timeout=3)
        return True
    except:
        return False


def risk_check(url):
    score = 0
    risky_words = ["login", "verify", "secure", "account", "free", "bonus"]

    for word in risky_words:
        if word in url.lower():
            score += 1

    if url.count("-") >= 3:
        score += 1

    if url.startswith("http://"):
        score += 1

    return score


def banner():
    print("\033[1;36m")
    print("===================================")
    print("   KALI SETUP - URL CHECKER")
    print(f"           Version v{VERSION}")
    print("===================================")
    print("\033[0m")


def main():

    # -------- VERSION ARGUMENT --------
    if len(sys.argv) > 1:
        if sys.argv[1] in ["-v", "--version"]:
            print(f"Kali Setup Version v{VERSION}")
            return

    banner()

    if not internet_available():
        print("\033[1;31m[!] No internet connection\033[0m")
        return

    url = input("Enter URL to check: ").strip()

    if not is_valid_url(url):
        print("\033[1;31m[!] Invalid URL format\033[0m")
        return

    print("\nScanning URL...")
    time.sleep(1)

    score = risk_check(url)

    if score >= 3:
        print("\033[1;31m[!] High Risk URL (Suspicious)\033[0m")
    elif score == 2:
        print("\033[1;33m[!] Medium Risk URL\033[0m")
    else:
        print("\033[1;32m[✓] Low Risk URL\033[0m")

    print("\n[INFO] This tool is for learning & awareness only.")


# =======================
# ENTRY POINT
# =======================
if __name__ == "__main__":
    main()
