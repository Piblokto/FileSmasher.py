# FileSmasher.py
FileSmasher is basic script written in Python designed to use as much bandwidth as physically possible.

The idea stems from my original [MirrorSmasher Shell Script](https://github.com/Piblokto/MirrorSmasher) which I created when I first got gigabit internet. With a line speed of ~950mbps, I managed to use >20TB of data and bandwidth every day.


## What does it do?
FileSmasher utilises the wget python package to download large amounts of information, and simultaneously delete it. 

The intended use of this program is to test stability and performance of an internet connection over a sustained period of time.

FileSmasher is designed to be as minimal, yet as customisable as possible. Simply make a list of any files hosted on a web/file server (or use the default list in this respository), edit the config.ini file to fit your desired presets; speed cap, amount of times looped, ect... , then watch as your network usage spikes.


### Disclaimer
This could very well breach your ISP's fair use policy, I take no responsibility if your internet services get limited or cancelled from use of this script. This is simply a tool that I made for fun.

You should also be warned that the file servers may see your IP address downloading the same file multiple times and decide to block your IP from their services. This is why it's recommended to have a variety of files in your links.txt. 

**You have been warned**



#
## Setup
The setup process for FileSmasher is very simple. Just simply clone the repository, install any dependencies (see requirements), make any desired changes to the config file, and then run main.py.

For more information please see the wiki.

### Requirements
- [Python 3.9](https://www.python.org/downloads/)
- [Python wget](https://pypi.org/project/wget/)

For easy install of python dependencies, please see requirements.txt, this is updated the most, and automates the process, simply just type ```pip install -r requirements.txt```
