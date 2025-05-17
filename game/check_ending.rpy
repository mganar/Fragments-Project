label check_ending:

    scene black
    with fade
    
    $ total_trust = sum(trust.values())
    $ total_fear = sum(fear.values())


    if total_trust >= 50 and total_fear <= 20:
        "FATE DETERMINED. BLUE ENDING"
        jump ending_one_start
    elif total_fear >= 50 and total_trust <= 20:
        "FATE DETERMINED. RED ENDING"
        jump ending_three_start
    else:
        "FATE DETERMINED. BLUE ENDING"
        jump ending_two_start

    return