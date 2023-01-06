import os
import subprocess
import sys

def install_git():
    # Install Git
    subprocess.run(['apt-get', 'install', '-y', 'git'])

    # Add Git to the PATH
    with open('~/.bashrc', 'a') as bashrc:
        bashrc.write('\nexport PATH=$PATH:/usr/bin/git')

def install_msfdb():
    # Check if the msfdb command is in the PATH
    result = subprocess.run(['which', 'msfdb'], stdout=subprocess.PIPE)
    if result.returncode != 0:
        # msfdb is not in the PATH, so install it
        subprocess.run(['apt-get', 'install', '-y', 'msfdb'])

# Update the system
subprocess.run(['apt-get', 'update'])

# Check if Git is installed
result = subprocess.run(['which', 'git'], stdout=subprocess.PIPE)
if result.returncode != 0:
    # Git is not installed, so install it
    install_git()

# Install the msfdb command if it is not found
install_msfdb()

# Install dependencies
dependencies = ['curl', 'build-essential', 'libreadline-dev', 'libssl-dev', 'libpq5', 'libpq-dev', 'libreadline5', 'libsqlite3-dev', 'libpcap-dev', 'openjdk-8-jre-headless', 'xtightvncviewer', 'libxml2-dev', 'libxslt1-dev', 'libyaml-dev', 'autoconf', 'zlib1g-dev', 'ruby', 'ruby-dev']

for dependency in dependencies:
    subprocess.run(['apt-get', 'install', '-y', dependency])

# Add the gem executable to the PATH
subprocess.run(['echo', 'export PATH=$PATH:/usr/local/bin', '>>', '~/.bashrc'])

# Install the bundler gem
subprocess.run(['gem', 'install', 'bundler'])

# Add the bundle executable to the PATH
subprocess.run(['echo', 'export PATH=$PATH:/usr/local/bundle/bin', '>>', '~/.bashrc'])

# Clone Metasploit from GitHub
subprocess.run(['git', 'clone', 'https://github.com/rapid7/metasploit-framework.git'])

# Install Metasploit
os.chdir('metasploit-framework')
subprocess.run(['bundle', 'install'])

print('Your Metasploit has been successfully installed! Happy Hacking Champ')
