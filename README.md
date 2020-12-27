# Online Chess Pygame

This is a chess game written in [Python](https://www.python.org "Python homepage") 3.6.9, using the pygame, sockets and threading libraries. The engine supports 2 players playing at a time, on different machines and networks. Basic client server system is made based on [TechwithTim's tutorial](https://www.youtube.com/watch?v=_fx7FQ3SP0U "Online server tutorial"), while rest of the code handle UI and actual gameplay. 

## To Run the Code

First, you have to clone/download this repository to get access to both modes of the game

#### Offline Mode

You can simply run the Chess.py code and play it with someone else on the same machine.

#### Online Mode

You will need to change the server IP address to the one that is hosting the game in these 2 files:

* server.py
* network.py

Then, you can run the server.py on one machine, then start one instance of client.py on each machine to play online chess

## Gameplay Samples

![](https://github.com/Anthon1e/Online-Chess-Pygame/blob/main/Sample1.gif)

![](https://github.com/Anthon1e/Online-Chess-Pygame/blob/main/Sample1.gif)

## Known Bugs

* Checkmate does not work

## Special Thanks to

* TechwithTim's Tutorials on [Pygame](https://www.youtube.com/watch?v=i6xMBig-pP4&list=PLzMcBGfZo4-lp3jAExUCewBfMx3UZFkh5 "Pygame Tutorial") and [Online Server](https://www.youtube.com/watch?v=_fx7FQ3SP0U "Online server tutorial")
* [Mason Wong](https://github.com/masonw19 "MW github") - We started this project together but did them differently