# Disclaimer
The author is not responsible for any misuse of the code. Do not use this code for any illegal activities.

**by (cyb3r00v3)**

# Metasploit Installer

This script installs the Metasploit framework on an Ubuntu system. The Metasploit framework is a powerful tool used for developing and executing exploits against a target system.

# Prerequisites

A system running Ubuntu
An Internet connection
How to use
Download or clone the script.
Make the script executable: chmod +x install_msf.py
Run the script as root: sudo ./install_msf.py

# What the script does

Installs Git, if it is not already installed.
Installs the msfdb command, if it is not already installed.
Updates the system package list.
Installs a number of dependencies needed to run the Metasploit framework.
Installs the bundler gem.
Clones the Metasploit repository from GitHub.
Changes into the metasploit-framework directory and runs bundle install to install the remaining dependencies and complete the installation of the Metasploit framework.

# Notes

The script adds the gem, bundle, and git executables to the PATH.
The msfdb command is used to initialize and manage a Metasploit database.
