# <center>===(Fallout CMD)===</center>

## INTRO:

Fallout CMD is a text-based Fallout adventure! 
You are 'The Courier', a lone wanderer in the Mojave wasteland and a bounty hunter. 

You’ve tracked down your biggest bounty, the infamous raider Cook-Cook hiding out in vault 3. 
When you enter the vault, you’ll need a full functioning set of Power Armor (A Helmet in the dining hall, Power Armor in the maintenance bay, and a Fusion Core powering the reactor chamber) to protect yourself from his attacks. 
You need to get a Stimpak from the medical bay, to heal from damage. 
And the firepower to take down Cook-Cook (Combat Shotgun from the armory, Ammo in the holding cell, and the Perk: Gunslinger to level up your skills that you can find in the classroom). 
You also end up locked in the vault so you will need to find the Vault Key in the living quarters to escape with your bounty.

-------------------------------------------------------
## DEPENDENCIES:

This is a dependency based game that requires its adjacent files and directories to run properly.

The file ```FalloutCMD.zip``` is a pre-packaged directory structure to allow for easy playability.

Path validation is done with every instance of file usage.

```FalloutCMD``` Is the root directory where Python script is located. 

```FalloutCMD/art``` For text art files.

```FalloutCMD/text``` For text description files.

### INCLUDED:

Additional files:

```Fallout CMD Launcher.bat``` Game launcher of Python script for Windows.

```FalloutCMD.exe``` Compiled application of the game for Windows.

-------------------------------------------------------------------------------------------------------------
## REQURIEMENTS:		

* Python 3 based		
* Windows, macOS, and Linux compatible

-------------------------------------------------------------------------------------------------------------
## FUNCTIONALITY:

* All basic gameplay requirements. (Commands, input validation, conditional loops, etc..)
* Dynamic art and room descriptions.
* Fully functional Pip-Boy. (Shows player items, dynamically updating objectives, and random quote banner.)
* Help Menu with all commands and detailed instructions for Main Game and Pip-Boy.
* Command to return to Main Menu.
* Dynamic loss description. (The description when the player loses changes based on the players items.)

#### CONSIDERED BUT <u>NOT</u> IMPLAMENTED FUNCTIONALITY:

* Dynamic Pip-Boy player map. (Excluded for complexity and partially defeated the purpose of a text based game.)
* CLI command cache. (Excluded for complexity and macOS issues, keyboard monitoring requires additional downloaded python package and elevated permissions for script and IDE to 'mimic' windows command prompt up arrow command recall. Possible to enable by changing terminal settings.)
* More dynamic 'combat' based on weapons, armor, and supplies. (Excluded due to over complexity, bulk, and outside of project scope.)     

-------------------------------------------------------------------------------------------------------------

## CONTROLS:

All commands can be entered in any case: 
    ```move north```, ```Move North```, ```MOVE NORTH```, etc..

#### <center>===(Main Game)===</center>

#### Return to Main Menu:       
Return to main menu by typing the ```main menu``` or ```mm``` command.

Example:  
```
:>main menu  {ENTER KEY}
:>mm  {ENTER KEY} 
```

#### Quit the Game: 		
Quit the game by typing the ```quit``` or ```q``` command.
Example:  
```
:>quit  {ENTER KEY}
:>q  {ENTER KEY}
```

#### Movement:  		
Moving room to room is done using the `move` command.

Example:
``` 
:>move north  {ENTER KEY}
:>move south  {ENTER KEY}
:>move east  {ENTER KEY}
:>move west  {ENTER KEY}
```

#### Picking up items: 		
To pick up an item found in a room use the `get` command.

Example: 
```
:>get stimpak  {ENTER KEY}
:>get power armor helmet  {ENTER KEY}
:>get combat shotgun  {ENTER KEY}
:>get fusion core  {ENTER KEY}
```

#### Opening the Pip-Boy:
Open your Pip-Boy by typing the `pip` or `p` command.

Example:
```
:>pip  {ENTER KEY}
:>p  {ENTER KEY}
```
-------------------------------------------------------------------------------------------------------------
