import threading
def draw_board(spot):
    board = (f"|{spot[1]} | {spot[2]} | {spot[3]}|\n"
           f"|{spot[4]} | {spot[5]} | {spot[6]}|\n"
           f"|{spot[7]} | {spot[8]} | {spot[9]}|")
    print(board)

def check_turn(turn):
    if turn % 2 == 0:
        return 'O'
    else:
        return 'X'
def check_for_win(spots):
    #Handle Horizontal cases
    if (spots[1]==spots[2]==spots[3]\
        or spots[4]==spots[5]==spots[6]\
        or spots[7]==spots[8]==spots[9]):
        return True
    #Handle Vertical cases      
    elif (spots[1]==spots[4]==spots[7]\
        or spots[2]==spots[5]==spots[8]\
        or spots[3]==spots[6]==spots[9]):
        return True
    #Handle Diagonal cases      
    elif (spots[1]==spots[5]==spots[9]\
        or spots[3]==spots[5]==spots[7]):
        return True
    else:
        return False

def get_input_with_timeout(timeout):
    """Function to get input within a time limit"""
    input_value = None

    def input_thread():
        nonlocal input_value
        input_value = input()  # Get user input

    thread = threading.Thread(target=input_thread)
    thread.start()
    thread.join(timeout)  # Wait for timeout seconds

    if thread.is_alive():
        return None  # Return None if time expired
    return input_value  # Return actual input if provided