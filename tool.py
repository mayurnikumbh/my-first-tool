#!/usr/bin/env python3

import os
import time

def banner():
    os.system("clear")
    print("\033[1;32m")
    print("===================================")
    print("        KALI SETUP TOOL             ")
    print("===================================")
    print(" Author : Mayur")
    print(" Version: 1.0")
    print("===================================")
    print("\033[0m")

def check_url():
    url = input("Enter URL: ")
    fake_words = ["login", "verify", "free", "bonus", "offer"]
    print("\nChecking...\n")
    time.sleep(1)
    if any(word in url.lower() for word in fake_words):
        print("\033[1;31m[!] Suspicious / Phishing Link\033[0m")
    else:
        print("\033[1;32m[✓] Link looks SAFE\033[0m")
    input("\nPress Enter to continue...")

def help_menu():
    print("""
This tool checks URLs for suspicious keywords.
Use it for educational & awareness purposes only.
    """)
    input("Press Enter to continue...")

while True:
    banner()
    print("1) Check URL")
    print("2) Help")
    print("3) Exit")
    choice = input("\nSelect option: ")

    if choice == "1":
        check_url()
    elif choice == "2":
        help_menu()
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid option!")
        time.sleep(1)
