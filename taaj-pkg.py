import argparse
import os
from rich.progress import track


# Terminal colors

reset_color = "\033[0m"
green = "\033[32m"
red = "\033[31m"
yellow = "\033[93m"
cyan = "\033[36m"

# Python packages only for linux

python = [
    "django", "kivy", "flask",
    "pillow", "flask", "ipython",
    "selenium", "scapy", "whois",
    "pandas", "pytelegrambotapi",
    "telebot", "python-dotenv", "autopep8",
    "secure-smtplib", "pyperclip3", "random2",
    "paramiko", "opencv-python", "scipy",
    "bs4", "datetime", "pygame",
    "python-dev-tools", "cython"
]

arch_pkgs = [
    "neofetch", "bpytop", "htop",
    "tor", "tmux", "virtualbox",
    "preload", "libreoffice-fresh", "nmap",
    "discord", "discover", "gcc",
    "android-tools", "whois", "kvantum-qt5",
    "etcher", "cython", "mysql"
]

# Termux section
termux_start = [
    "pkg update -y", "pkg upgrade -y", "termux-setup-storage"
]

termux_install = [
    "coreutils", "openssh", "git",
    "tor", "neofetch", "unstable-repo",
    "x11-repo", "python-pip", "zsh"
]

termux_py = [
    "ipython", "scapy", "whois",
    "pytelegrambotapi", "telebot", "python-dotenv",
    "secure-smtplib", "pyperclip3", "random2",
    "datetime", "bs4", "paramiko",
    "requests", "cython","python-dev-tools",
]

# Script Flags

parser = argparse.ArgumentParser()

parser.add_argument("-l", "--linux",
                    help="Same Python modules for all distros")

parser.add_argument("-a", "--arch",
                    help="Options of Arch Linux")

parser.add_argument("-t", "--termux",
                    help="Options of Termux")

args = parser.parse_args()


# List all tasks for a given flag

def listing(tasks):
    for task in tasks:
        print(cyan, task, reset_color)
    print("\nTasks:", len(tasks))
# Linux Python pkg installation


def python_pkgs(key):
    starting = input("[?] Start instalation? [Y/n] ") or "Y"

    if starting == "y" or starting == "Y":
        print(f"{green}[+] started{reset_color}\n")
        for pkg in track(key, description="Installing..."):
            print(f"{yellow}[*]{pkg}:{reset_color}")
            os.system(f"pip install {pkg}")
            print(f"{green}[+] Task Done!{reset_color}\n")

    elif starting == "n" or starting == "N":
        print(f"{red}[X] Canceled!{reset_color}")
    else:
        print(f"{red}[X] Not Defined!")
        exit

# Package installation for arch linux


def linux_setup(key1, key2):
    starting = input("[?] Start instalation? [Y/n] ") or "Y"

    if starting == "y" or starting == "Y":
        print(f"{green}[+] started{reset_color}\n")
        for pkg in track(key2, description="Installing..."):
            print(f"{yellow}[*]{pkg}:{reset_color}")
            os.system(key1 + pkg)
            print(f"{green}[+] Task Done!{reset_color}\n")

    elif starting == "n" or starting == "N":
        print(f"{red}[X] Canceled!{reset_color}")
    else:
        print(f"{red}[X] Not Defined!")
        exit

    os.system("exit")

# Termux Settings Setup


def termux_setup():

    starting = input("[?] Start Setup? [Y/n] ") or "Y"
    if starting == "y" or starting == "Y":
        print(f"{green}[+] started{reset_color}\n")
        for command in termux_start:
            print(f"{yellow}[*]{command}:{reset_color}")
            os.system(command)
            print(f"{green}[+] Task Done!{reset_color}\n")

    elif starting == "n" or starting == "N":
        print(f"{red}[X] Canceled!{reset_color}")
    else:
        pass

# Termux requirements installation


def main():
    # Linux

    if args.linux == "py":
        try:
            listing(python)
            print("\n")
            python_pkgs(python)
        except KeyboardInterrupt:
            print(f"\n{red}[X] Canceled!{reset_color}")

    # Arch Linux

    if args.arch == "pkgs":
        try:
            if os.geteuid() == 0:
                listing(arch_pkgs)
                print("\n")
                arch_standard = "pacman -Syu "
                linux_setup(arch_standard, arch_pkgs)
            else:
                print(
                    f"{yellow}[!] Run as root in order to work currectly!{reset_color}\n")
        except KeyboardInterrupt:
            print(f"\n{red}[X] Canceled!{reset_color}")
    # Termux

    if args.termux == "setup":
        try:
            listing(termux_start)
            print("\n")
            termux_setup()
        except KeyboardInterrupt:
            print(f"\n{red}[X] Canceled!{reset_color}")

    elif args.termux == "pkgs":
        try:
            listing(termux_install)
            print("\n")
            termux_standard = "pkg install "
            linux_setup(termux_standard, termux_install)
        except KeyboardInterrupt:
            print(f"\n{red}[X] Canceled!{reset_color}")

    elif args.termux == "py":
        try:
            listing(termux_py)
            print("\n")
            python_pkgs(termux_py)
        except KeyboardInterrupt:
            print(f"\n{red}[X] Canceled!{reset_color}")
    else:
        print(f"{red}[X] Nothing to do!{reset_color}")


if __name__ == "__main__":
    main()
