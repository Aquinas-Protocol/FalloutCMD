import os
import sys
import random

"""
Autor: *redacted for Aquinas-Protocol*
Text Based Fallout Inspired Game
Written for Intro to Scripting Class
Requires: 
    - Intact 'art' and 'text' directories in same directory as script for proper function.
    - Windows, Mac OS, or Linx
    - Python 3
"""

# -------------------------------------------------Classes----------------------------------------------------------


class TextColor:
    """
    A class used to format strings with different color codes.

    Attributes
    ----------
    GREEN = Color code for green
    YELLOW = Color code for yellow
    RED = Color code for red
    current = Current text color

    Methods
    ----------
    format_str(in_str)
        Returns string formatted as current color.
    """
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'

    def __init__(self, color=GREEN):
        """
        Constructs necessary 'current' color for TextColor object.
        Can pass optional color code, default color is green.
        :param color: Optional color code to be applied.
        :type color: str
        """
        self.current = color  # set current color to passed color code

    def format_str(self, in_str):
        """
        Formats and returns a string with current color code.
        :param in_str: String to be formatted
        :type in_str: str
        :return: Passed 'in_str' formatted with current color
        """
        return self.current.join(in_str)  # return color code concatenated with 'in_str'


class File:
    """
    Class handles all file operations as a File object.

    Attributes
    ----------
    path = Path to create file object.

    Methods
    ----------
    print_utf8(color_code)
        Prints entire file with UTF-8 encoding.
    to_str()
        Returns file as a string.
    to_list()
        Returns list of file lines.
    """
    def __init__(self, path):
        """
        Validates and constructs necessary 'path' for File object
        :param path: Path to file
        :type path: str
        """
        if os.path.isfile(path) and os.access(path, os.R_OK):  # file and path exists and is readable
            self.path = path  # give object its path
        else:  # the file or path could not be found
            clear_display()  # clear the display
            err_str = "The dependency \'" + path + "\' could not be found.\n"  # build error message string
            err_str += "Please ensure that this script is in the proper \'FalloutCMD\' directory.\n"
            err_str += "For proper operation unpack \'FalloutCMD.zip\' and run script from its root directory."
            display_box(err_str, TextColor.RED)  # display error message and instructions
            input("Press Enter to continue...")  # wait for player to press 'enter'
            sys.exit(0)  # exit the script

    def print_utf8(self, color_code):
        """
        Prints a file line by line using the 'color_code' passed.
        File is read with UTF-8 encoding to read and print the special characters,
        such as in a line art file, properly.
        :param color_code: Color for printed file to be displayed
        :type color_code: str
        """
        color = TextColor(color_code)

        with open(self.path, 'r', encoding='UTF-8') as file:  # with the file open as 'read' with UTF-8 encoding
            while line := file.readline():  # while the file line is being read, store in 'line'
                if color_code != "":  # if color code is not blank
                    print(color.format_str(line.rstrip()))  # print the current line as passed color
                else:  # no valid color code
                    print(line.rstrip())  # print line without formatting

    def to_str(self):
        """
        Reads a file with UTF-8 encoding and returns it contents as a string.
        :return: File contents as string
        """

        with open(self.path, 'r', encoding='UTF-8') as file:  # with loop to open file as 'r'/ read with UTF-8 encoding
            file_contents = file.read()  # store file contents into variable 'file_contents'
        return file_contents  # return 'file_contents' string

    def to_list(self):
        """
        Reads the lines of a file into a list using UTF-8 encoding.
        :return: List of file lines
        """

        line_list = []  # declare a list to hold lines of a file 'line_list'
        with open(self.path, 'r', encoding='UTF-8') as file:  # with loop to open file as 'r' / read with UTF-8 encoding
            while line := file.readline():  # while file line is being read into 'line'
                # append file line string to 'line_list' (each line = element of list)
                # uses '.rstrip()' to strip trailing blank space from line string
                line_list.append(line.rstrip())
        return line_list  # return the list of file lines


class PipBoy:
    """
    A class for Pip-Boy object. Contains all methods and attributes required to display and control the users Pip-Boy.

    Attributes
    ----------
    inventory = Players passed inventory of items
    objectives = Player list of objectives to complete.

    Methods
    ----------
    _fill_whitespace(str_len)
        Returns a string of blank spaces for given length.
    _pip_boy_screen(list_to_display, screen_header)
        Returns a formatted list of display lines.
    _build_display(left_list, right_list, text_list)
        Builds and returns Pip-Boy center display as string.
    show()
        Displays and enters Pip-Boy full menu.
    """
    def __init__(self, inventory, objectives):
        self.inventory = inventory
        self.objectives = objectives

    # vvv  Negates 'Method may be static' warning **Method is internal, static is not needed**
    # noinspection PyMethodMayBeStatic
    def _fill_whitespace(self, str_len):
        """
        Generates a string of blank spaces for given length.
        :param str_len: Length of string to be built
        :type str_len: int
        :return: String of blank spaces for given length
        """

        line_str = ""  # initialize blank string to hold blank spaces, 'line_str'
        for i in range(0, str_len):  # loop for the arg range of 'str_len' starting with an index of 0
            line_str += " "  # append a blank space to 'line_str' for each iteration
        return line_str  # return the blank space string

    # vvv  Negates 'Method may be static' warning **Method is internal, static is not needed**
    # noinspection PyMethodMayBeStatic
    def _pip_boy_screen(self, list_to_display, screen_header):
        """
        Creates a formatted template for the pip-boy screen as list,
        ensures list has enough elements to display properly.
        :param list_to_display:Content to be displayed, line by line
        :type list_to_display: list
        :param screen_header: Header/title of screen
        :type screen_header: str
        :return: Formatted display lines, as list
        """

        # the list 'display_screen' starts with the header portion
        display_screen = [" ",  # pad top with blank line
                          "                   ==( " + screen_header + " )==",  # append header string to header line
                          " "]  # pad bottom with blank line
        # create a list with 15 blank string elements to pad the bottom of the pip-boy screen
        # provides enough padding to display properly no matter the size of 'list_to_display'
        filler = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
        display_screen.extend(list_to_display)  # adds list_to_display onto display_screen with extend
        display_screen.extend(filler)  # adds the padding filler onto the bottom display_screen with extend

        return display_screen  # return formatted display_screen list

    def _build_display(self, left_list, right_list, text_list):
        """
        Builds the center of pip-boy display, formats with correct margins to center given text_list within display.
        :param left_list: Left side of pip-boy art display lines
        :type  left_list: list
        :param right_list: Right side of pip-boy art display lines
        :type  right_list: list
        :param text_list: Text to by displayed line by line
        :type  text_list: list
        :return: Formatted center 'block' of pip-boy display as single string
        """

        display_str = ""  # initialize blank string to hold the center display, 'display_str'

        # set display height and width to fit pip-boy art
        display_h = 16
        display_w = 67

        # set the adjustment point (the point of off-set positioning for the text in relation to the display width)
        adjustment = 60

        # set the insert point (point in line text is to be inserted. here it's 7 characters into display width)
        insert_point = display_w - adjustment

        # loop for range of the display height, starting at 0, using i as the index to sync all lists together
        for i in range(0, display_h):
            txt_length = len(text_list[i])  # store the length of current line of text to be used as an int 'txt_length'

            # this statement does the heavy lifting of building the displayable pip-boy "center block" line by line,
            # appending 'display_str' with each iteration.
            # 1st: by appending the left most element of pip-boy art for that line 'left_list[i]'.
            # 2nd: it appends blank spaces up to the insert_point with fill_whitespace().
            # 3rd: 'text_list[i]' (current line of text to be displayed) is appended at its insert point.
            # 4th: the remainder of blank space is calculated subtracting the 'txt_length' from the adjustment value
            #      and that value is passed to the 'fill_whitespace()' function to be appended to display_str.
            # 5th: the right most element of pip-boy art for that line 'right_list[i]' is appended to 'display_str'
            # 6th: a newline char '\n' is appended as a string to complete this line of display_str.
            display_str += (left_list[i] + self._fill_whitespace(insert_point) + text_list[i] +
                            self._fill_whitespace(adjustment - txt_length) + right_list[i] + "\n")

        # once all lines of the pip-boy display are appended on top of each other the final display "block" is returned
        return display_str

    def show(self):
        """
        Enters the pip-boy menu, displays current inventory and objectives, uses separate commands from main game.
        """

        # create paths to pip-boy art files
        pip_boy_top_file = os.path.join("art", "pip_boy_top.txt")
        pip_boy_bottom_file = os.path.join("art", "pip_boy_bottom.txt")
        pip_boy_left_file = os.path.join("art", "pip_boy_left.txt")
        pip_boy_right_file = os.path.join("art", "pip_boy_right.txt")

        # store pip-boy top and bottom art to variables
        # raw pip-boy top file needs newline char appended for proper display
        pb_top = File(pip_boy_top_file).to_str() + "\n"
        pb_bottom = File(pip_boy_bottom_file).to_str()

        # create lists for left and right side pip-boy art lines (used to build the display)
        pb_left_lines = File(pip_boy_left_file).to_list()
        pb_right_lines = File(pip_boy_right_file).to_list()

        # set the pip-boy screen to 'objectives' / 'quest' screen
        display_text = self._pip_boy_screen(self.objectives, "Quest")

        # build the center display with the pip-boy screen as 'display_text' and store in 'pb_display' string
        pb_display = self._build_display(pb_left_lines, pb_right_lines, display_text)

        clear_display()  # clear the display
        display_box('\n' + random_quote() + '\n', TextColor.GREEN)  # display random quote above pip-boy
        print(pb_top + pb_display + pb_bottom)  # print the pip-boy as appending top, center, and bottom string

        while True:  # loop constantly until broken
            # receives player input, converts input string to lowercase(for easier processing),
            # and stores in 'cmd' variable
            cmd = input("\n---------------------------------------:>").lower()

            if cmd == "c":  # player closes the pip-boy
                clear_display()  # clear the display
                break  # break the loop
            elif cmd == "q":  # player selected the 'quest' screen
                # set the pip-boy screen to 'objectives' / 'quest' screen
                display_text = self._pip_boy_screen(self.objectives, "Quest")
                # build the center display
                pb_display = self._build_display(pb_left_lines, pb_right_lines, display_text)
                clear_display()  # clear the display
                display_box('\n' + random_quote() + '\n', TextColor.GREEN)  # display random quote above pip-boy
                print(pb_top + pb_display + pb_bottom)  # print the pip-boy as appending top, center, and bottom string
            elif cmd == "i":  # player selected the 'item' screen
                # set the pip-boy screen to 'item' screen
                display_text = self._pip_boy_screen(self.inventory, "Items")
                # build the center display
                pb_display = self._build_display(pb_left_lines, pb_right_lines, display_text)
                clear_display()  # clear the display
                display_box('\n' + random_quote() + '\n', TextColor.GREEN)  # display random quote above pip-boy
                print(pb_top + pb_display + pb_bottom)  # print the pip-boy as appending top, center, and bottom string
            else:
                print("Pip-Boy Command \'" + cmd +
                      "\' was not recognized.\nUse \'i\' for Items, \'q\' for Quest, or \'c\' to Close Pip-Boy.")
                input("Press Enter to continue...")  # wait for player to press 'enter'
                clear_display()  # clear the display
                display_box('\n' + random_quote() + '\n', TextColor.GREEN)  # display random quote above pip-boy
                print(pb_top + pb_display + pb_bottom)  # print the pip-boy as appending top, center, and bottom string


class RoomOperation:
    """
    Class handles all major room operations.

    Attributes
    ----------
    room = Room dictionary to be operated on.

    Methods
    ----------
    has_item(item)
        Check if the room has any item, or specific passed item.
    can_move(direction)
        Check if the player can move in a given direction from the room.
    print_description()
        Prints the rooms description.
    """
    def __init__(self, room):
        """
        Constructs necessary room dictionary for operations object.
        :param room: Room dictionary for operations.
        """
        self.room = room  # set this room to passed room

    def has_item(self, item=''):
        """
        Checks if the room has ANY item, optionally can check for a specific item (if item is passed).
        :param item: Optional: Item string to be found
        :return: Boolean if item was found
        """

        for key, value in self.room.items():  # loop through room items for 'key's and 'value's
            if item != '':  # if an item was passed to method
                if (key == 'Item') and (value == item):  # if 'key' 'Item' is found and its value matches passed item
                    return True  # that item was found in the room
            else:  # no item was passed to function
                if (key == 'Item') and (value != ''):  # if 'key' 'Item' is found and its value is not empty
                    return True  # an item was found in the room

        return False  # no valid item entry was found

    def can_move(self, direction):
        """
        Checks if the player can move in a specified direction in the room.
        :param direction: Cardinal direction pointer
        :type direction: str
        :return: Boolean if player can move
        """

        for key in self.room:  # loop through 'room' dictionary for it's 'key's
            if key == direction:  # if the 'key' matches passed 'direction'
                return True  # a valid direction to move was found
        return False  # no valid direction to move was found

    def print_description(self):
        """
        Prints the line art and description for the room,
        adjusts the description depending on the room state.
        """
        File(self.room['Art']).print_utf8(TextColor.YELLOW)  # display the line art for this room

        if self.has_item():  # checks if this room has an item in it
            # if the room has an item, display the whole file (includes the final item description)
            display_box(File(self.room['Description']).to_str(), TextColor.GREEN)
        else:  # else / there is no item in the room
            description_str = ''  # set a new description string variable with a blank string
            # store the lines of the description file in a list 'description_lines'
            description_lines = File(self.room['Description']).to_str().split('\n')
            description_lines.pop()  # remove the bottom three lines (item description element of file)
            description_lines.pop()  # item description element is always formatted as
            description_lines.pop()  # the last three lines of the room description file
            for i in range(
                    len(description_lines)):  # loop for remaining elements of description_lines, with 'i' as index
                description_str += description_lines[
                                       i] + '\n'  # build description string line by line, appending '\n' char

            # display the adjusted description string without the item description element
            display_box(description_str, TextColor.GREEN)


# ------------------------------------------------/END Classes----------------------------------------------------
# -------------------------------------------Variables using a Global Scope---------------------------------------
# create booleans for if the player has the helmet, armor, fusion core, shotgun, and ammo
# these 'has item' bools are initialized here for a program wide scope, then globalized in function 'objective_checker'
# for updating as objectives are processed
has_helmet = False
has_armor = False
has_fusion_core = False
has_shotgun = False
has_ammo = False
has_stimpak = False
has_vault_key = False
has_gunslinger = False
# ---------------------------------------/END Variables using a Global Scope--------------------------------------


def display_box(txt, color_code):
    """
    Prints a display box that contains the passed string as the given passed color.
    :param txt: Text to be displayed
    :type txt: str
    :param color_code: Color of display to be applied
    :type color_code: str
    """
    color = TextColor(color_code)

    top = "------------------------------------------------------------------------------------------------\n"
    bottom = "\n------------------------------------------------------------------------------------------------"
    if color_code != "":  # if color code is not blank
        print(color.format_str(top + txt + bottom))  # prints appended "box" around 'txt' through as_color
    else:  # no valid color code
        print(top + txt + bottom)  # prints appended "box" around 'txt' string on top and bottom


def clear_display():
    """
    Clears the display depending on operating system.
    Passes 'cls' or 'clear through 'os.system' effectively speaking directly to command prompt or terminal.
    In the event no operating system can be identified, 25 blank lines are printed
    (only functions properly when ran through command prompt or terminal)
    """
    if os.name == 'nt':  # if the operating system is windows based
        os.system('cls')  # send cls to command prompt
    elif os.name == 'posix':  # if the operating system is posix based (Mac-OS, Linux, Etc..)
        os.system('clear')  # send clear to terminal
    else:   # unable to identify operating system
        for i in range(25):
            print()  # print 25 blank lines


def main_menu():
    """
    Displays the main menu roll sequence.
    """

    welcome_art = os.path.join("art", "welcome.txt")  # set path to welcome line art

    clear_display()  # clear the console

    File(welcome_art).print_utf8(TextColor.GREEN)  # display the welcome art

    display_box("Maximize console window to see the full game ^^^^^^^^^^^", TextColor.GREEN)  # display instruction box

    input("Press Enter to continue...")  # wait for player to press 'enter'

    clear_display()  # clear the console

    File(welcome_art).print_utf8(TextColor.GREEN)  # display the welcome art again

    # display main menu box
    display_box("Type \'S\' to start game or type \'Q\' to quit game or \'help\' for help / instructions.",
                TextColor.GREEN)


def play_intro():
    """
    Plays the into section, tells backstory and setup for entry into the vault.
    """

    # set paths to intro text files
    intro_txt = os.path.join("text", "intro.txt")
    intro_two_txt = os.path.join("text", "intro2.txt")
    intro_three_txt = os.path.join("text", "intro3.txt")
    intro_four_txt = os.path.join("text", "intro4.txt")

    vault_door_art = os.path.join("art", "vault_door.txt")  # set path to vault door art

    clear_display()  # clear the console
    File(intro_txt).print_utf8(TextColor.GREEN)  # display first part of intro file
    input("Press Enter to continue...")  # wait for player to press 'enter'
    clear_display()  # clear the console
    File(intro_two_txt).print_utf8(TextColor.GREEN)  # display second part of intro file
    input("Press Enter to continue...")  # wait for player to press 'enter'
    clear_display()  # clear the console
    File(intro_three_txt).print_utf8(TextColor.GREEN)  # display third part of intro file
    input("Press Enter to continue...")  # wait for player to press 'enter'
    clear_display()  # clear the console
    File(intro_four_txt).print_utf8(TextColor.GREEN)  # display fourth part of intro file
    input("Press Enter to continue...")  # wait for player to press 'enter'
    clear_display()  # clear the console
    File(vault_door_art).print_utf8(TextColor.YELLOW)  # display the vault door line art as yellow
    display_box("You see the vault through a dust cloud..\nYou approach the door.. Open it?", TextColor.YELLOW)
    input("Press Enter to Open The Door..")  # wait for player to press 'enter'


def help_screen():
    """
    Displays the Main Game help screen and Pip-Boy help screen waits for player to press enter before clearing screen.
    """

    help_main_txt = os.path.join("text", "help_main.txt")  # path to main help file
    help_pip_txt = os.path.join("text", "help_pip.txt")  # path to pip help file

    clear_display()  # clear the console
    File(help_main_txt).print_utf8(TextColor.GREEN)  # display main help file
    input("Press Enter for Pip-Boy Controls")  # wait for player to press 'enter'
    clear_display()  # clear the console
    File(help_pip_txt).print_utf8(TextColor.GREEN)  # display pip-boy help file
    input("Press Enter to continue...")  # wait for player to press 'enter'
    clear_display()  # clear the console


def random_quote():
    """
    Generates a random Fallout quote, formats for display and returns it as a string.
    :return: Random formatted fallout quote
    """

    quotes_txt = os.path.join("text", "quotes.txt")  # set path to quotes file
    all_quotes = File(quotes_txt).to_list()  # read all quotes into a list
    rand_quote_index = random.randrange(0, len(all_quotes))  # generate a random index between 0 and list length
    quote_str = all_quotes[rand_quote_index]  # store the random quote in its own string
    final_q_str = ''  # initialize a string for final formatted quote
    last_found_i = 0  # initialize an int for last found index

    # logic and looping ensures quote length fits within display properly
    if len(quote_str) > 96:  # if the quote length exceeds display
        # loop through the quote by char, checking for acceptable breakpoint for first line
        for i in range(len(quote_str)):
            # if the index is greater than 90 and current char is a blank space
            if i > 90 and quote_str[i] == ' ':  # an acceptable breakpoint was found
                final_q_str += quote_str[i] + '\n'  # append the char and newline to final string
                last_found_i = i  # set last found index as current index
                break  # break the loop, the first line is complete
            else:  # continue building line
                final_q_str += quote_str[i]  # append the current char to final string

        if last_found_i != 0:  # if the last found index is caught, confirming before slicing
            final_q_str += quote_str[last_found_i:]  # append remainder of quote using slice from found index
    else:  # quote fits within display
        final_q_str = quote_str  # set final string as quote string

    quote_and_author = final_q_str.split(' -')  # separate the quote and author using .split()

    return quote_and_author[0] + '\n    -' + quote_and_author[1]  # return the quote, a newline, then the author


def pop_and_replace_objective(objective_list, index, rep_str):
    """
    Removes and replaces an element of given list.
    :param objective_list: Objectives to be altered
    :type objective_list: list
    :param index: Index for position in list
    :type index: int
    :param rep_str: Objective line to replace previous line
    :type rep_str: str
    """

    objective_list.pop(index)  # remove current list entry at current iteration point using '.pop(index)'
    objective_list.insert(index, rep_str)  # replace said element by inserting 'rep_str' at current index


def update_objective_line(obj_str, objective_list, index):
    """
    Marks a players objective line as complete.
    :param obj_str: Objective line entry to be marked complete
    :type obj_str: str
    :param objective_list: Player's objectives
    :type objective_list: list
    :param index: Index for position in list
    :type index: int
    """

    if obj_str in objective_list[index]:  # confirm that objective line entry matches 'objective_list' at index
        checked_obj = obj_str.replace('()', '(*)')  # replace unchecked box with checked box
        pop_and_replace_objective(objective_list, index, checked_obj)  # replace objective line with checked line


def objective_checker(player_items, objective_list):
    """
    Checks and updates the players objectives / quest. Iterates through all items and objectives,
    marks and updates all objective lines.
    :param player_items: Player's item inventory
    :type player_items: list
    :param objective_list: Player's original objectives
    :type objective_list: list
    :return: Updated objectives list
    """

    # globalize scope of 'has item' bools, to make external values changeable within this function
    global has_helmet
    global has_armor
    global has_fusion_core
    global has_shotgun
    global has_ammo
    global has_stimpak
    global has_vault_key
    global has_gunslinger

    # these nested loops check every player item against every objective and adjusts the list as needed
    for item in player_items:  # loop through the player items for each item
        for i in range(len(objective_list)):  # loop through all objectives, using 'i' as an index
            # this first set of branching statements checks for items needed for "singular objectives"
            # ( only one item is needed to "check off objective" e.g. -Find a Stimpak () = -Find a Stimpak (*) )
            if item == 'Stimpak':  # if the item 'Stimpak' is found
                # check if 'Stimpak' is in objective line for current objective_list iteration
                update_objective_line('-Find a Stimpak ()', objective_list, i)
                has_stimpak = True  # set the bool, showing that the player has the item 'Stimpak'
            elif item == 'Gunslinger':  # else if the item 'Perk: Gunslinger' is found
                # check if 'Perk: Gunslinger' is in objective line for current objective_list iteration
                update_objective_line('-Level Up and Find Gunslinger Perk ()', objective_list, i)
                has_gunslinger = True  # set the bool, showing that the player has the item 'Perk: Gunslinger'
            elif item == 'Vault Key':  # else if the item 'Vault Key' is found
                # check if 'Vault Key' is in objective line for current objective_list iteration
                update_objective_line('-Find the Vault Key to Escape ()', objective_list, i)
                has_vault_key = True  # set the bool, showing that the player has the item 'Vault Key'
            # the following statements check for items that are one of "multiple objectives" (needs multiple items)
            # these objectives are made blank when item is found as opposed to "updating" the line by "checking off"
            elif item == "Helmet":  # else if the item 'Helmet' is found
                # check if 'Helmet' is in objective line for current objective_list iteration
                if "> Helmet" in objective_list[i]:
                    has_helmet = True  # set the bool, showing that the player has the item 'Helmet'
                    pop_and_replace_objective(objective_list, i, '')  # replace with a blank string
            elif item == 'Power Armor':  # else if the item 'Power Armor' is found
                # check if 'Power Armor' is in objective line for current objective_list iteration
                if '> Power Armor' in objective_list[i]:
                    has_armor = True  # set the bool, showing that the player has the item 'Power Armor'
                    pop_and_replace_objective(objective_list, i, '')  # replace with a blank string
            elif item == 'Fusion Core':  # else if the item 'Fusion Core' is found
                # check if 'Fusion Core' is in objective line for current objective_list iteration
                if '> Fusion Core' in objective_list[i]:
                    has_fusion_core = True  # set the bool, showing that the player has the item 'Fusion Core'
                    pop_and_replace_objective(objective_list, i, '')  # replace with a blank string
            elif item == 'Combat Shotgun':  # else if the item 'Combat Shotgun' is found
                # check if 'Combat Shotgun' is in objective line for current objective_list iteration
                if '> Find Combat Shotgun' in objective_list[i]:
                    has_shotgun = True  # set the bool, showing that the player has the item 'Combat Shotgun'
                    pop_and_replace_objective(objective_list, i, '')  # replace with a blank string
            elif item == 'Ammo':  # else if the item 'Ammo' is found
                # check if 'Find Ammo' is in objective line for current objective_list iteration
                if '> Find Ammo' in objective_list[i]:
                    has_ammo = True  # set the bool, showing that the player has the item 'Ammo'
                    pop_and_replace_objective(objective_list, i, '')  # replace with a blank string

    # after iterating through all items and objectives, check if player has all items needed for "multiple objectives"
    # the "multiple objectives" parent tree (main objective line with check box (*)) is indexed at its fixed position
    # index 'objective_list[0]' = -Find Working Set of Power Armor,
    # objective_list[5] = -Find Weapon to Deal with Cook-Cook
    if has_helmet and has_armor and has_fusion_core:  # if the user has all items for complete power armor set
        if '*' not in objective_list[0]:  # if this objective is not already "checked off"
            pop_and_replace_objective(objective_list, 0, '-Find Working Set of Power Armor (*)')

    if has_ammo and has_shotgun:  # if the user has ammo and shotgun (functioning weapon set)
        if '*' not in objective_list[5]:  # if this objective is not already "checked off"
            pop_and_replace_objective(objective_list, 5, '-Find Weapon to Deal with Cook Cook (*)')

    return objective_list  # return the updated list of objective


def next_fight_step(txt, art, art_color):
    """
    Performs a given step for the final fight sequence. Displays art, a message, and prompts player to continue.
    :param txt: Text to be displayed
    :type txt: str
    :param art: Path of art to be displayed
    :type art: str
    :param art_color: Color of art to be displayed
    :type art_color: str
    """
    clear_display()  # clear the console
    File(art).print_utf8(art_color)  # display line art
    display_box(txt, TextColor.GREEN)  # display text in display box
    input("Press Enter to continue...")  # wait for player to press 'enter'


def boss_fight_sequence(items):
    """
    Plays 'boss fight' sequence, including all logic for if the player wins or loses.
    Displays 'fight' progressively, depending on the players items.
    :param items: Inventory of player's items.
    :type items: list
    :return: If the player has won or lost
    """
    # set paths to line art files
    success_art = os.path.join("art", "vault_boy_thumb.txt")
    success_txt = os.path.join("text", "success.txt")
    cook_cook = os.path.join("art", "cook-cook.txt")

    input("Press Enter to Turn and Face Cook-Cook...")  # wait for player to press 'enter'

    clear_display()  # clear the console

    File(cook_cook).print_utf8(TextColor.YELLOW)  # display Cook-Cook Art

    if len(items) == 8:  # if the player has all the items (inventory is correct length)
        display_box("Cook-Cook: \"Ooooo look who came prepared! Too bad its not gunna help you!\"", TextColor.GREEN)
        input("Press Enter to shoot!")  # wait for player to press 'enter' to 'kill' cook-cook
        File(success_txt).print_utf8(TextColor.GREEN)  # display success message
        input("Press Enter to continue...")  # wait for player to press 'enter'
        clear_display()  # clear the console
        File(success_art).print_utf8(TextColor.GREEN)  # display success art
        display_box("Congratulations! You beat FalloutCMD!\nI hope you enjoyed it as much as I enjoyed making it!",
                    TextColor.GREEN)
        input("Press Enter to continue...")  # wait for player to press 'enter'
        return True
    else:  # else player does not have all items needed to win ('fight' will display depending on players items)
        display_box("Cook-Cook: \"Fresh Meat! I'm eating good tonight!\"", TextColor.GREEN)
        input("Press Enter to Fight!")  # wait for player to press 'enter' to 'fight' cook-cook

        # condense logic for if the player has complete sets of armor and weapons
        has_full_power_armor = has_armor and has_fusion_core and has_helmet  # player has full set of armor
        has_firepower = has_shotgun and has_ammo and has_gunslinger  # player has full weapon 'set'

        fight_log = ""  # create blank string to hold text of the 'fight'
        game_over = os.path.join('art', 'game_over.txt')  # set the path to game over line art

        if has_full_power_armor:  # if the user has a full set of power armor
            fight_log += "Cook-Cook fires his flame thrower, but you can take the damage for now...\n"
        else:  # player has not found a full set
            fight_log += "Cook-Cook fires his flame thrower, you're getting burned up quick!\n"

        next_fight_step(fight_log, cook_cook, TextColor.YELLOW)  # run next fight step

        if has_stimpak:  # if the player has a stimpak
            fight_log += "You took some damage but the Stimpak fixes you right up!\n"
        else:  # the player does not have a stimpak
            fight_log += "You take some damage but you have nothing to heal you. You don't have long...\n"

        next_fight_step(fight_log, cook_cook, TextColor.YELLOW)  # run next fight step

        if has_firepower:  # if the player has a full weapon set
            fight_log += "You got Cook-Cook in your sights, you land your shots but he keeps fighting...\n"
        else:  # player does not a have a full weapon set
            fight_log += "Cook-Cook: \"What's the matter kid? You got no firepower?\"\n"
            fight_log += "You can't cause enough damage, its not looking good...\n"

        next_fight_step(fight_log, cook_cook, TextColor.YELLOW)  # run next fight step

        fight_log += "You tried but you didn't have enough to make is out in one piece..\n"
        fight_log += "Cook-Cook: \"Another chump from the wastes, never stood a chance!\"\n"

        if has_vault_key:  # if the player has the vault key
            fight_log += "You had the Vault Key. You could have escaped.. Too bad you didn't make it.\n"
        else:  # the player does not have the key
            fight_log += "You never found the Vault Key. Even if you survived, you would have never made it out..\n"

        next_fight_step(fight_log, game_over, TextColor.GREEN)  # run final fight step

        return False


def main():
    """
    Main program function.
    Contains main menu loop and gameplay loop in sequence.
    Assigns all rooms, inventory, objectives for current gameplay iteration.
    Can call self on 'main menu' command to restart sequence.
    """

    main_menu()  # display main menu

    # ----------------------------------------------MAIN MENU LOOP------------------------------------------------------
    while True:  # runs a continuous menu loop
        # receives player input, converts input string to lowercase(for easier processing), and stores in 'cmd' variable
        cmd = input(":>").lower()

        if cmd == "s":  # if the player entered the start command
            clear_display()  # clear the console
            # display opening quote
            display_box("\n                                  War. War Never Changes...\n", TextColor.GREEN)
            input("Press Enter to continue...")  # wait for player to press 'enter'
            break  # break menu loop
        elif ("quit" in cmd) or cmd == "q":  # else if the player entered the quit command
            sys.exit(0)  # close the game
        elif cmd == "help" or cmd == "h":  # else if the player entered the help command
            help_screen()  # display help screen
            main_menu()  # display main menu again
        else:  # else the command is not recognized
            display_box("Command not recognized.\nType \'S\' to Start Game or type \'Q\' to Quit Game.",
                        TextColor.GREEN)
            input("Press Enter to continue...")  # wait for player to press 'enter'
    # -----------------------------------------/END MAIN MENU LOOP------------------------------------------------------

    play_intro()  # play the intro sequence

    # -------------------------------------------Setup Operations-------------------------------------------------------
    # create nested dictionaries for all rooms
    # they will all have a 'Name', a cardinal direction pointer e.g. North='Recreation Area', 'Art' path to line art,
    # and a 'Description' path to text description file. some will have Items.
    rooms = {
        'Vault Entrance': dict(Name='Vault Entrance', North='Recreation Area',
                               Art=os.path.join('art', 'vault_entrance.txt'),
                               Description=os.path.join('text', 'vault_entrance_desc.txt')),
        'Recreation Area': dict(Name='Recreation Area', North='Armory', East='Maintenance Bay', West='Living Quarters',
                                South='Vault Entrance', Art=os.path.join('art', 'rec_area.txt'),
                                Description=os.path.join('text', 'recreation_area_desc.txt')),

        'Living Quarters': dict(Name='Living Quarters', North='Dining Hall', East='Recreation Area', Item='Vault Key',
                                Art=os.path.join('art', 'living_quarters.txt'),
                                Description=os.path.join('text', 'living_quarters_desc.txt')),
        'Dining Hall': dict(Name='Dining Hall', West='Medical Bay', East='Class Room', South='Living Quarters',
                            Item='Helmet', Art=os.path.join('art', 'dining_hall.txt'),
                            Description=os.path.join('text', 'dining_hall_desc.txt')),
        'Medical Bay': dict(Name='Medical Bay', East='Dining Hall', Item='Stimpak',
                            Art=os.path.join('art', 'mr_handy.txt'),
                            Description=os.path.join('text', 'medical_bay_desc.txt')),
        'Class Room': dict(Name='Class Room', West='Dining Hall', Item='Gunslinger',
                           Art=os.path.join('art', 'class_room.txt'),
                           Description=os.path.join('text', 'class_room_desc.txt')),

        'Maintenance Bay': dict(Name='Maintenance Bay', West='Recreation Area', South='Reactor Chamber',
                                East='Holding Cell', Item='Power Armor',
                                Art=os.path.join('art', 'maintenance _bay.txt'),
                                Description=os.path.join('text', 'maintenance _bay_desc.txt')),
        'Reactor Chamber': dict(Name='Reactor Chamber', North='Maintenance Bay', Item='Fusion Core',
                                Art=os.path.join('art', 'reactor_chamber.txt'),
                                Description=os.path.join('text', 'reactor_chamber_desc.txt')),
        'Holding Cell': dict(Name='Holding Cell', West='Maintenance Bay', Item='Ammo',
                             Art=os.path.join('art', 'holding_cell.txt'),
                             Description=os.path.join('text', 'holding_cell_desc.txt')),

        'Armory': dict(Name='Armory', North='Overseer\'s Office', South='Recreation Area', Item='Combat Shotgun',
                       Art=os.path.join('art', 'armory.txt'), Description=os.path.join('text', 'armory_desc.txt')),
        'Overseer\'s Office': dict(Name='Overseer\'s Office', South='Armory',
                                   Art=os.path.join('art', 'overseer_office.txt'),
                                   Description=os.path.join('text', 'overseer_office_desc.txt'))
    }

    inventory = []  # set player inventory as empty
    objectives = ['-Find Working Set of Power Armor ()',
                  '   > Helmet',
                  '   > Power Armor',
                  '   > Fusion Core',
                  '',
                  '-Find Weapon to Deal with Cook Cook ()',
                  '   > Find Combat Shotgun',
                  '   > Find Ammo',
                  '',
                  '-Find a Stimpak ()',
                  '-Level Up and Find Gunslinger Perk ()',
                  '-Find the Vault Key to Escape ()',
                  '-Kill Cook Cook ()']  # setup player's objectives list in proper format

    current_room = rooms['Vault Entrance']  # set current room to starting room: Vault Entrance
    current_room_op = RoomOperation(current_room)  # set current room operations to current room
    hud_box_art = os.path.join("art", "hud_box.txt")  # set path to hud line art
    # --------------------------------------/END Setup Operations-------------------------------------------------------

    # ------------------------------------------------GAMEPLAY LOOP-----------------------------------------------------
    while True:  # runs a continuous gameplay loop
        clear_display()  # clear the console

        # display the description and art in its current status using current room operation
        current_room_op.print_description()

        if current_room['Name'] == 'Overseer\'s Office':  # if the player is in the 'Boss Fight' room
            objective_checker(inventory, objectives)  # update objectives list
            if boss_fight_sequence(inventory):  # if the player has won
                sys.exit(0)  # close the program
            else:  # else the player has lost
                main()  # call self, main function, restarting game sequence from the beginning

        File(hud_box_art).print_utf8(TextColor.GREEN)  # display hud box

        # receives player input, converts input string to lowercase(for easier processing), and stores in 'cmd' variable
        cmd = input(":>").lower()

        if cmd == "help" or cmd == "h":  # if the player enters the 'help' command
            help_screen()  # display help screen
        elif "move" in cmd:  # else if the player enters the 'move' command
            # parses out the direction from move command by replacing 'move ' with a blank space
            # use .title() to capitalize first letter of 'sub_cmd' and match expected direction formatting
            sub_cmd = cmd.replace("move ", "").title()
            if current_room_op.can_move(sub_cmd):  # if the player can move in the direction entered
                # set the current room to the room of the direction entered
                # index the 'rooms' nested dictionaries using the 'current_room's cardinal direction pointer
                # for the given direction in 'sub_cmd'
                current_room = rooms[current_room[sub_cmd]]
                current_room_op = RoomOperation(current_room)  # set current room operation to new current room
            else:  # the player can't move in that direction
                print('You can\'t move that way!')
                input("Press Enter to continue...")  # wait for player to press 'enter'
        elif "get" in cmd:  # else if the player enters the 'get' command
            # parse out the item from get command by replacing 'get ' with a blank space, stores in 'sub_cmd'
            # format the sub command with title() to match item entries (fusion core = Fusion Core)
            sub_cmd = cmd.replace("get ", "").title()
            if current_room_op.has_item(sub_cmd):  # if the 'current_room has' the item parsed from 'sub_cmd'
                inventory.append(current_room['Item'])  # append the player inventory with the item in current_room
                # remove the item from parent dictionary 'rooms' indexing using current_room and removing its item
                rooms[current_room['Name']].pop('Item')
                print('You Picked Up ' + sub_cmd + '!')  # show the player what they picked up
                input("Press Enter to continue...")  # wait for player to press 'enter'
            else:  # this room has no item
                print('There\'s no ' + sub_cmd + ' to get here!')  # display that the item entered isn't there
                input("Press Enter to continue...")  # wait for player to press 'enter'
        elif cmd == "main menu" or cmd == "mm":  # else if the player enters the 'main menu' command
            main()  # call self, main function, restarting game sequence from the beginning
        elif cmd == "pip" or cmd == "p":  # else if the player enters the pip-boy command
            objectives = objective_checker(inventory, objectives)  # update objectives list
            pip = PipBoy(inventory, objectives)  # set and update Pip-Boy object
            pip.show()  # open the Pip-Boy
        elif cmd == "quit" or cmd == "q":  # else if the player enters the 'quit' command
            sys.exit(0)  # close the program
        else:  # command was not found
            print("The command \'" + cmd + "\' is not recognized")  # print that command entered is not recognized
            input("Press Enter to continue...")  # wait for player to press 'enter'
    # --------------------------------------------/END GAMEPLAY LOOP----------------------------------------------------


# check if special variable '__name__' is '__main__' (if this script executed itself and not imported)
if __name__ == "__main__":
    main()  # run main game function
