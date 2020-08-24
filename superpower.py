import sys

def switch(num):
    """ Switch The Power (multiplying by -1) """
    return num*(-1)


def findConsecutives(len_pair, lis):
    """  Find all possible Consective , Find their Sum"""
    consecutive_sum = []
    for i in range(len(lis) - len_pair + 1):

        pair = ["", ""]
        pair[0] = sum(lis[i: i+len_pair])  # The consecutive --
        pair[1] = sum(lis) - pair[0]
        consecutive_sum.append(pair)

    return consecutive_sum


def approach1(left_switches, heros):
    """  maximum overall power that can be achieved by switching the
     power of nb_of_swiches many heroes, a given hero seeing its power
     being switched an arbitrary number of times"""
    heros = sorted(heros)

    for index, hero in enumerate(heros):
        if(left_switches):

            if(hero < 0):
                # Apply Switches to Negative Values First

                heros[index] = switch(hero)
                left_switches = left_switches-1
            elif (hero > 0):
                # Apply Switches to Positive Value

                if(left_switches % 2 != 0):
                    heros[index] = switch(hero)
                    break
        else:
            break
    return sum(heros)


def approach2(left_switches, heros):
    """ maximum overall power that can be achieved by switching
    the power of nb_of_swiches many heroes, a given hero seeing
    its power being switched an arbitrary number of times"""
    heros = sorted(heros)

    for index, hero in enumerate(heros):
        if(left_switches):

            if(hero < 0):
                # Apply Switches to Negative Values First

                heros[index] = switch(hero)
                left_switches = left_switches-1
            elif (hero > 0):
                # Apply Switches to Positive Value
                heros[index] = switch(hero)
                left_switches = left_switches-1

        else:
            break
    return sum(heros)


def approach3(availble_switches, heros):
    """ determines the maximum overall power that can be
    achieved by switching the power of nb_of_swiches many
    consecutive heroes"""

    pairs = findConsecutives(availble_switches, heros)
    smallest = pairs[0]

    for pair in pairs:
        if(pair[0] < smallest[0]):
            smallest = pair

    return switch(smallest[0]) + smallest[1]


def approach4(nb_of_switches, heros):
    """ program determines the maximum overall power that 
    can be achieved by switching the power of arbitrarily 
    many consecutive heroes"""

    # Applying approch possible times and find the maximum overall power

    appr_4 = []
    for i in range(len(heros)):
        appr_4.append(approach3(i, heros))
    return max(appr_4)


def main():
    try:
        heros = input("Please input the heroes' powers: ")

        heros = list(map(int, heros.split()))
    except:
        print("Sorry, these are not valid power values.",)
        exit()
    nb_of_switches = int(input("Please input the number of power flips: "))

    if(nb_of_switches < 0 or nb_of_switches > len(heros)):
        print("Sorry, this is not a valid number of power flips.")
        exit()
    print("Possibly flipping the power of the same hero many times, the greatest achievable power is ", approach1(
        nb_of_switches, heros), ".", sep="")
    print("Flipping the power of the same hero at most once, the greatest achievable power is ", approach2(
        nb_of_switches, heros), ".", sep="")
    print("Flipping the power of nb_of_flips many consecutive heroes, the greatest achievable power is ", approach3(
        nb_of_switches, heros), ".", sep="")
    print("Flipping the power of arbitrarily many consecutive heroes, the greatest achievable power is ", approach4(
        nb_of_switches, heros), ".", sep="")



main()
