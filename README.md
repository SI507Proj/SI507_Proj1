

## About the Project
* This project about the simulation of the Card Game of War and its unittest.
* The detailed explanation about the game can be found in [this link](http://www.bicyclecards.com/how-to-play/war/)
* Unittest parts check the expected behaviors of the game.
* Please check the code description file in the repository

## Installation
* Setup and Download
	1. Install and init Git
	2. Setup SSH key in your env and github
	3. Git clone with SSH git@github.com:sehwchoi/SI507_Proj1.git
	4. Or you can download the source files from [this link](https://github.com/sehwchoi/SI507_Proj1)

* Python version
This program requires Python Ver.3 to be installed

* Virtual env
Recommend to use VirtualEnv
> virtualenv --python=python3 venv_test
> source venv_test/bin/activate

* External library requirements
Please check requirements.txt in the source file.
You can install requirements using pip3 as below.
> pip3 install -r requirements.txt 

## How to Run Game
SI507F17_project1_cards.py simulates The card game of war.
If there are fails or errors after run, there is a bug in the game.
> python3 SI507F17_project1_cards.py

## How to Test Game
SI507F17_project1_test.py unit tests the card game.
>python3 I507F17_project1_test.py
