import random

# function for repeating experiment 10k times
def repeat_experiment():
    successes = 0 # success counter - will increase if any given experiment contains a streak of 6 consecutive flips

    # run experiment 100k times, if flip coins returns true, add 1 to success counter
    for n in range(100000):
        if flip_coins():
            successes += 1
    
    # print final calculation on what percentage of experiments contained a streak of 6
    print(f"A streak of 6 or more appeared in {successes/100000*100:.2f}% of 100,000 experiments")

# function for doing the experiment itself
def flip_coins():
    coin_flips = []
    
    # flip 100 random coins(generate random int between 0, 1), and add them to a list
    for n in range(100):
        coin_flips.append(random.randint(0, 1))
    
    # runs streak checker function, and returns true or false to repeat_experiment, depending on result of streak checker
    return streak_checker(coin_flips)

# checks for a streak of 6 in the list of 100 flips, and returns True if it finds one.
def streak_checker(coin_flips):
    # initialize streak at 1 - since if you flip a coin, no matter the result, you have a streak of 1.
    streak = 1

    # stop iteration on index 98 of list to avoid error of overstepping list bounds
    for flip in range(len(coin_flips) - 2):

        # compare current flip with next flip, if they are the same, increase streak counter by 1
        if coin_flips[flip] == coin_flips[flip + 1]:
            streak += 1

        # if not the same, reset streak counter back to 1
        else:
            streak = 1
        
        # if streak reaches 6, return True back to flip coins function, which then passes up to repeat_experiment
        if streak == 6:
            return True
    
    # if all flips are checked and no streak of 6 has been reached, return false
    return False

# python main guard, just learned about this recently and the use case for it. as far as i understand it is encouraged to use 
# this, so please let me know if this looks implimented correctly to you!
if __name__ == '__main__':
    repeat_experiment()

