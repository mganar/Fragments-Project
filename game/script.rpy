# script.rpy

# This is your main entry point when the player clicks "New Game"
label start:
    
    # Optional: mark that the player has begun the game (persistent flag)
    $ persistent.first_run = True

    # Jump into the current test file (chapter zero or sandbox)
    call script_0_start

    call check_ending
    return