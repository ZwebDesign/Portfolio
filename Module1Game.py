import time
import random
player_inventory = {"coins": 15, "armour": 0, "health": 20, "weapon": 1}
player_points = [0, 0]
diff_count = [0, 0, 0]


def print_inventory():
    """Does what it says. Prints inventory"""
    print("\n-------------------------------------------------------\n", player_inventory,
          "\n-------------------------------------------------------\n")


def roller_testing():
    """Asks for roll number, and makes sure it's a number that can be used"""
    correct_value = False
    while not correct_value:
        try:
            asknum = input("Pick a number between 1 and 6.")
            return dice(int(asknum))
        except ValueError:
            print("please choose an integer \n------------------------")


def dice(inputnum):
    """Compares the user guess to a random roll"""
    print("rolling...")
    time.sleep(random.randint(2, 3))
    dienum = random.randint(1, 6)
    """Outputs a usable number to wherever the code is being used"""
    if inputnum == dienum:
        print("correct")
        player_points[0] = player_points[0]+2
        return 2
    elif inputnum == dienum-1 or inputnum == dienum+1:
        print("Close. The correct answer was", str(dienum))
        player_points[0] = player_points[0] + 1
        return 1
    else:
        print("incorrect. The correct answer was", str(dienum))
        return 0


def combat(e_health, e_accuracy, e_strength, e_name, armr_brk):
    """general combat layout for all enemies. Your enemy's strength and accuracy are decided behind the scenes, all
    damage done and taken is random; however, it is vastly affected by various stats """
    print("You have entered combat.")
    alive = True
    while alive:
        if e_health <= 0:
            return 1
        elif player_inventory["health"] <= 0:
            return 0
        else:
            stun = 0
            time.sleep(1)
            """player attack sequence"""
            print("Your enemy has", e_health, "health")
            time.sleep(1)
            print_inventory()
            time.sleep(1)
            print("Roll for your damage.")
            out = roller_testing()
            if out == 2:
                dmg = random.randint(3, 5)
                stun = random.randint(1, 5)
                e_health = int(e_health) - (dmg * player_inventory["weapon"])
                time.sleep(2)
                player_points[0] = player_points[0] + dmg
                print("you do", dmg * player_inventory["weapon"], "damage")
                """Possibility to stun the enemy for a round and prevent them from taking a turn"""
                if stun == 2:
                    player_points[0] = player_points[0] + 2
                    print("You stunned the enemy this round.")
            elif out == 1:
                dmg = random.randint(2, 4)
                e_health = int(e_health) - (dmg * player_inventory["weapon"])
                time.sleep(2)
                player_points[0] = player_points[0] + dmg
                print("you do", dmg * player_inventory["weapon"], "damage")
            elif out == 0:
                dmg = random.randint(0, 2)
                miss = random.randint(1, 3)
                dmg_tkn = int(random.randint(1, 3)*(player_inventory["weapon"]/2))
                e_health = int(e_health) - (dmg * player_inventory["weapon"])
                time.sleep(2)
                player_points[0] = player_points[0] + dmg
                print("you do", dmg * player_inventory["weapon"], "damage")
                """1 in 3 chance of missing your target and hitting yourself too. This scales with the power of your 
                weapon divided by 2"""
                if miss == 3:
                    time.sleep(1)
                    player_points[0] = player_points[0] - dmg_tkn
                    player_inventory["health"] = player_inventory["health"] - dmg_tkn
                    print("You missed and hit yourself too.")
                    time.sleep(1)
                    print("-", dmg_tkn, "health")
            if e_health <= 0:
                return 1
            elif player_inventory["health"] <= 0:
                return 0
            time.sleep(2)
            """enemy attack sequence"""
            e_dmg = random.randint(1*e_accuracy, 5)
            if stun == 2:
                print("The", e_name, "is stunned this round...")
                time.sleep(2)
            else:
                time.sleep(1)
                print("The", e_name, "attacks")
                time.sleep(1)
                """Looks to see if you have armour, and takes a certain amount away based on the enemy"""
                if player_inventory["armour"] >= 1:
                    player_inventory["armour"] = player_inventory["armour"] - armr_brk
                    player_points[0] = player_points[0] + 2
                    print("Your armour absorbed this hit")
                    time.sleep(1)
                    print("-", armr_brk, "armour")
                    time.sleep(1)
                    if player_inventory["armour"] < 0:
                        time.sleep(1)
                        print("You didn't have enough armour to fully absorb it.")
                        time.sleep(1)
                        player_inventory["health"] = player_inventory["health"] - (player_inventory["armour"]*(-5))
                        print("-", player_inventory["armour"]*(-5), "health")
                        player_inventory["armour"] = 0
                else:
                    dmg = (e_strength*e_dmg)
                    player_inventory["health"] = player_inventory["health"] - dmg
                    time.sleep(1)
                    print("The", e_name, "does", dmg, "Damage")
                    time.sleep(1)
                    print("-", dmg, "health")


def wares_test(ware_value):
    """processes transactions, first seeing if you have enough money and then changing your stats"""
    if player_inventory.get("coins") >= ware_value[1]:
        """Takes away the money based on whatever the list item is priced at"""
        player_inventory["coins"] = player_inventory["coins"] - ware_value[1]
        if ware_value[0] == "empty":
            print("searching...")
            time.sleep(2)
            player_points[0] = player_points[0] + 3
            print("*nothing here*")
        elif ware_value[0] == "bought":
            print("searching...")
            time.sleep(2)
            print("Item already purchased")
        else:
            """Changes stats based on the item you bought"""
            time.sleep(1)
            print("item purchased, you have", player_inventory.get("coins"), "coins left")
            if ware_value[0] == "armour":
                player_inventory["armour"] = player_inventory["armour"] + 1
                player_points[0] = player_points[0] + 3
            elif ware_value[0] == "2hp":
                player_inventory["health"] = player_inventory["health"] + 2
                player_points[0] = player_points[0] + 2
            elif ware_value[0] == "wuI":
                player_inventory["weapon"] = player_inventory["weapon"] + 1
                player_points[0] = player_points[0] + 1
            elif ware_value[0] == "wuII":
                player_inventory["weapon"] = player_inventory["weapon"] + 2
                player_points[0] = player_points[0] + 2
            elif ware_value[0] == "wuIII":
                player_inventory["weapon"] = player_inventory["weapon"] + 3
                player_points[0] = player_points[0] + 3
    else:
        print("Sorry, you can't afford this.")


def merchant():
    """Randomly generates amount and type of items for the player to purchase"""
    print("\n*you approach a merchant's table*")
    """Increases the price by 2 or 3 every iteration"""
    cost_add = diff_count[0]*random.randint(2, 3)
    items = random.randint(1, 6)
    finish = False
    """Creates and then empties wares list"""
    wares = [0]
    wares *= 0
    time.sleep(1)
    print("Merchant: Hello my friend, are you interested in any wares?")
    time.sleep(2)
    print_inventory()
    time.sleep(2)
    print("Merchant: Here are my wares\n")
    """Randomly sets up the list of available products and creates invisible list of items and associated costs for the
     "wares_test" function to access."""
    for index in range(items):
        product = random.randint(1, 4)
        if product == 1:
            print("Armour -", 10 + cost_add, "coins")
            wares.append(["armour", 10 + cost_add])
        elif product == 2:
            print("2 Health points -", 5+cost_add, "coins")
            wares.append(["2hp", 5 + cost_add])
        elif product == 3:
            upgrade_lvl = random.randint(1, 3)
            if upgrade_lvl == 1:
                print("Weapon Upgrade I -", 10 + cost_add, "coins")
                wares.append(["wuI", 10 + cost_add])
            elif upgrade_lvl == 2:
                print("Weapon Upgrade II -", 15 + cost_add, "coins")
                wares.append(["wuII", 15 + cost_add])
            elif upgrade_lvl == 3:
                print("Weapon Upgrade III -", 20 + cost_add, "coins")
                wares.append(["wuIII", 20 + cost_add])
        else:
            print("*dusty cobwebs*")
            wares.append(["empty", 0])
    print("")
    time.sleep(2)
    while not finish:
        correct_value = False
        while not correct_value:
            try:
                """processes item selection and allows the user to exit. Makes sure that values entered are correct"""
                purchase = int(input("Type( 0 to leave / 1 for the first item / 2 for the second item, etc.)"))
                if purchase >= 1:
                    wares_test(wares[purchase-1])
                    """Replaces purchased items with a blank list item called "bought" """
                    wares[purchase-1] = ["bought", 0]
                    player_points[0] = player_points[0] + 1
                elif purchase == 0:
                    correct_value = True
                    finish = True
                break
            except ValueError:
                print("please enter a valid value")
            except IndexError:
                print("please enter a valid value")
    print("Merchant: Goodbye Stranger")
    time.sleep(2)


def passage():
    """passage image"""
    print("\n|                                  |\n|                                  |\n|                           "
          "       |\n|     you've entered a passage     |\n|                                  |\n|                    "
          "              |\n|                                  |\n")
    print("roll to see what finds you in this passage")
    out = roller_testing()
    """generates outcome depending on the roll"""
    if out == 2:
        coin_num = random.randint(3, 5)
        print("You found", coin_num, "coins laying around!")
        player_inventory["coins"] = player_inventory["coins"] + coin_num
        time.sleep(1)
        player_points[0] = player_points[0] + coin_num
        print("+", coin_num, "coins")
    elif out == 1:
        print("Nothing happens...")
        time.sleep(2)
    elif out == 0:
        """Generates various levels of bad outcomes """
        bad_thing = random.randint(1, 3)
        if bad_thing == 1:
            print("You trip on a rock and hurt yourself.")
            player_inventory["health"] = player_inventory["health"] - 1
            player_points[0] = player_points[0] - 1
            time.sleep(1)
            print("Ouch, -1 health")
            time.sleep(2)
        elif bad_thing == 2:
            player_points[0] = player_points[0] - 1
            """Hidden Rat stat"""
            diff_count[2] = diff_count[2] + 1
            print("You find a dead rat. Gross, but harmless.")
            time.sleep(2)
        elif bad_thing == 3:
            coin_num = random.randint(2, 4)
            print("A pickpocket passes by.")
            time.sleep(1)
            """Tests to see if the player has coins, and then randomly selects how many coins they'll loose"""
            if player_inventory["coins"] > 0:
                print("they swipe some coins right out of your pocket.")
                player_inventory["coins"] = player_inventory["coins"] - coin_num
                time.sleep(1)
                player_points[0] = player_points[0] - coin_num
                print("-", coin_num, "coins")
                if player_inventory["coins"] <= 0:
                    player_inventory["coins"] = 0
                time.sleep(2)
            else:
                print("you had no coins to swipe.")
                player_points[0] = player_points[0] + 5
                time.sleep(1)
                print("I guess having no money pAyS oFf....")
                time.sleep(2)
                print("pretty funny, I know.")
                time.sleep(2)
    print("You keep walking.")
    time.sleep(2)
    print("---------------------------------------")


def trap():
    """Flips a coin and gives you one of two trap rooms."""
    room_type = random.randint(1, 2)
    print("\nYou've come across a trap room.")
    if room_type == 1:
        time.sleep(2)
        print("There are spike traps along the floor.")
        """Prints room image."""
        print(
            "\n|                                  |\n|                                  |\n|                           "
            "       |\n|                                  |\n|                                  |\n|                   "
            "               |\n|^^^^--^^^--^^^^^^^--^-^^^^^^--^^^^|\n")
        time.sleep(1)
        print_inventory()
        time.sleep(1)
        correct_value = False
        """spike trap room options and outcomes, as well as a filter for valid inputs"""
        while not correct_value:
            try:
                options = int(input("Type( 1 to run across / 2 to carefully maneuver around the spikes "
                                    "/ 3 to lose a piece of armour and get through safely)"))
                if options == 1 or options == 2 or options == 3:
                    if options == 1:
                        hurt = random.randint(1, 3)
                        """2:1 chance on whether or not you make it through when running"""
                        if hurt == 1 or hurt == 3:
                            time.sleep(1)
                            print("You made it across safely, lucky.")
                            player_points[0] = player_points[0] + 1
                            time.sleep(1)
                            break
                        elif hurt == 2:
                            time.sleep(1)
                            print("You were too slow. You lost 5 health")
                            player_inventory["health"] = player_inventory["health"] - 5
                            time.sleep(1)
                            print("-5 health")
                            time.sleep(1)
                            break
                    elif options == 2:
                        """Removes any weapon you may have, penalizing higher up players"""
                        time.sleep(1)
                        print("creeping required you to loose some weight")
                        if player_inventory["weapon"] > 1:
                            time.sleep(1)
                            print("You dropped your weapon because it was too much to carry.")
                            time.sleep(2)
                            print("-", player_inventory["weapon"] - 1, "weapon damage")
                            player_inventory["weapon"] = 1
                            time.sleep(1)
                            break
                        else:
                            time.sleep(2)
                            print("You didn't have any weapon to drop, so you were light enough.")
                            time.sleep(3)
                            break
                    elif options == 3:
                        if player_inventory["armour"] >= 1:
                            player_inventory["armour"] = player_inventory["armour"] - 1
                            time.sleep(1)
                            player_points[0] = player_points[0] + 5
                            print("You use your armour to safely get over the spikes.")
                            break
                        else:
                            player_inventory["health"] = player_inventory["health"] - 5
                            time.sleep(1)
                            print("You did not have any armour, so you loose 5 health attempting this.")
                            time.sleep(3)
                            print("-5 health")
                            break
                else:
                    print("please enter a valid value")
                if player_inventory["health"] <= 0:
                    break
            except ValueError:
                print("please enter a valid value")
    elif room_type == 2:
        time.sleep(2)
        """Prints room image."""
        print("the walls are slowly moving in, and the door behind you has locked\n|                                 "
              " |\n|                                  |\n|   ->                        <-   |\n|                       "
              "           |\n|    ->                      <-    |\n|                                  |\n|           "
              "                       |\n")
        time.sleep(1)
        print_inventory()
        time.sleep(1)
        correct_value = False
        """shrinking wall room options and outcomes, as well as a filter for valid inputs"""
        while not correct_value:
            try:
                options = int(input("Type( 1 to run across / 2 to cry for help / 3 to hold the walls apart with your "
                                    "weapon)"))
                if options == 1 or options == 2 or options == 3:
                    if options == 1:
                        hurt = random.randint(1, 3)
                        """1:2 chance on whether or not you make it through when running"""
                        if hurt > 1:
                            time.sleep(1)
                            print("You made it across safely, lucky.")
                            player_points[0] = player_points[0] + 1
                            time.sleep(2)
                            break
                        elif hurt == 1:
                            time.sleep(1)
                            print("You were too slow. You lost 5 health")
                            player_inventory["health"] = player_inventory["health"] - 5
                            time.sleep(1)
                            print("-5 health")
                            time.sleep(2)
                            break
                    elif options == 2:
                        """Penalizes those with lots of coins by taking all of them."""
                        time.sleep(1)
                        print("Somebody heard your cries.")
                        time.sleep(1)
                        print("They helped you in exchange for all your coins")
                        time.sleep(2)
                        print("-", player_inventory["coins"], "coins")
                        player_inventory["coins"] = 0
                        time.sleep(2)
                        break
                    elif options == 3:
                        if player_inventory["weapon"] >= 3:
                            time.sleep(1)
                            print("You are able to keep the walls apart and run through safely.")
                            time.sleep(2)
                            break
                        else:
                            time.sleep(1)
                            print("Your weapon was not strong enough to hold the walls")
                            time.sleep(1)
                            print("-", player_inventory["weapon"]-1, "weapon damage")
                            player_inventory["weapon"] = 1
                            player_points[0] = player_points[0] + 3
                            player_inventory["health"] = player_inventory["health"] - 5
                            print("- 5 health")
                            break
                else:
                    print("please enter a valid value")
                if player_inventory["health"] <= 0:
                    break
            except ValueError:
                print("please enter a valid value")


def boss():
    """Setting up the boss within the game,"The mole King" """
    b_health = random.randint(50, 100)
    b_accuracy = random.randint(2, 5)
    b_damage = random.randint(3, 5)
    a_brk = random.randint(2, 3)
    print("While wondering through the dungeon you walk into the realm of the Mole King...")
    correct_value = False
    """Makes sure the values entered are usable."""
    while not correct_value:
        try:
            response = int(input("Type( 1 to try and run / 2 to attack the Mole King / 3 to grovel before the "
                                 "Mole King and beg for forgiveness)"))
            if response == 1:
                print("No one can escape the Mole King...")
                time.sleep(1)
                print("Your attempt to run was futile...")
                time.sleep(1)
                print("-", player_inventory["armour"], "armour\n-", player_inventory["health"], "health")
                time.sleep(1)
                break
            elif response == 2:
                out = combat(b_health, b_accuracy, b_damage, "Mole King", a_brk)
                if out == 1:
                    print("You have defeated the Mole King...")
                    player_points[0] = player_points[0]+50
                    time.sleep(1)
                    print("In a wave of grief his mole minions dig a massive hole through to the surface.")
                    time.sleep(3)
                    print("They drag the Mole King up, and you never see any of them again...")
                    break
                elif out == 0:
                    time.sleep(1)
                    print("You were so close to escaping...")
                    break
            elif response == 3:
                player_points[0] = player_points[0] + 10
                print("roll to see if he will spare you.")
                time.sleep(1)
                out = roller_testing()
                time.sleep(1)
                if out == 2:
                    print("Your groveling was effective, so the Mole king grants you a proper weapon with which to "
                          "fight")
                    player_inventory["weapon"] = player_inventory["weapon"] + 2
                    time.sleep(3)
                    print("+ 2 weapon damage")
                    out = combat(b_health, b_accuracy, b_damage, "Mole King", a_brk)
                    if out == 1:
                        print("You have defeated the Mole King...")
                        player_points[0] = player_points[0] + 50
                        time.sleep(1)
                        print("In a wave of grief his mole minions dig a massive hole through to the surface.")
                        time.sleep(3)
                        print("They drag the Mole King up, and you never see any of them again...")
                        break
                    elif out == 0:
                        time.sleep(1)
                        print("You were so close to escaping...")
                        break
                elif out == 1:
                    print("You accomplished nothing. The Mole king still wishes to fight")
                    out = combat(b_health, b_accuracy, b_damage, "Mole King", a_brk)
                    if out == 1:
                        print("You have defeated the Mole King...")
                        player_points[0] = player_points[0] + 50
                        time.sleep(1)
                        print("In a wave of grief his mole minions dig a massive hole through to the surface.")
                        time.sleep(3)
                        print("They drag the Mole King up, and you never see any of them again...")
                        return 1
                    elif out == 0:
                        time.sleep(1)
                        print("You were so close to escaping...")
                        break
                elif out == 0:
                    print("The Mole king scoffs at your prostration.")
                    time.sleep(1)
                    print("You are nothing, and must be destroyed")
                    time.sleep(1)
                    print("He takes the first hit")
                    player_inventory["health"] = player_inventory["health"] - 5
                    time.sleep(1)
                    print("-5 health")
                    out = combat(b_health, b_accuracy, b_damage, "Mole King", a_brk)
                    if out == 1:
                        print("You have defeated the Mole King...")
                        player_points[0] = player_points[0] + 50
                        time.sleep(1)
                        print("In a wave of grief his mole minions dig a massive hole through to the surface.")
                        time.sleep(3)
                        print("They drag the Mole King up, and you never see any of them again...")
                        return 1
                    elif out == 0:
                        time.sleep(1)
                        print("You were so close to escaping...")
                        break
            else:
                print("please enter a valid value")
            if player_inventory["health"] <= 0:
                break
        except ValueError:
            print("please enter a valid value")


def chest():
    print("You found a chest!")
    time.sleep(1)
    open_it = input("hit enter to open").lower()
    if open_it == "no":
        player_inventory["health"] = 0
    else:
        loot = random.randint(1, 2)
        coin_num = random.randint(5, 10)
        health_num = random.randint(4, 7)
        time.sleep(1.5)
        print("opening...")
        time.sleep(2)
        if loot == 2:
            player_inventory["coins"] = player_inventory["coins"] + coin_num
            time.sleep(1)
            player_points[0] = player_points[0] + coin_num
            print("There were", coin_num, "coins")
            time.sleep(1)
            print("+", coin_num, "coins")
        elif loot == 1:
            player_inventory["health"] = player_inventory["health"] + health_num
            time.sleep(1)
            player_points[0] = player_points[0] + health_num
            print("There were", health_num, "health points")
            time.sleep(1)
            print("+", health_num, "health")


def low_enemy():
    enemy_health = random.randint(5, 15)
    enemy_accuracy = random.randint(1, 3)
    strength = random.randint(1, 2)
    print("A Mole grunt finds you wandering...")
    time.sleep(2)
    print_inventory()
    time.sleep(1)
    correct_value = False
    while not correct_value:
        try:
            response = int(input("Type( 1 to attempt to leave / 2 to attack "
                                 "/ 3 to try and bargain with the grunt)"))
            if response == 1 or response == 2 or response == 3:
                if response == 1:
                    time.sleep(1)
                    run_suc = random.randint(1, 3)
                    if run_suc == 1:
                        print("You try and run, but the grunt gets you while your back is turned")
                        time.sleep(2)
                        if player_inventory["armour"] >= 1:
                            player_inventory["armour"] = player_inventory["armour"] - 1
                            print("fortunately, your armour is all that gets damaged.")
                            time.sleep(1)
                            print("-1 armour")
                            time.sleep(1)
                            break
                        else:
                            print("You didn't have any armour to protect you...")
                            time.sleep(2)
                            print("-", player_inventory["health"], "health")
                            player_inventory["health"] = 0
                            break
                    else:
                        player_inventory["health"] = player_inventory["health"] - 2
                        print("You barely escape, but not without getting scratched up on the way out.")
                        time.sleep(2)
                        print("-2 health")
                        time.sleep(1)
                        break
                elif response == 2:
                    time.sleep(1)
                    c_out = combat(enemy_health, enemy_accuracy, strength, "Grunt", 1)
                    if c_out == 1:
                        time.sleep(1)
                        print("Grunt defeated!")
                        time.sleep(2)
                        item_upgrade = random.randint(1, 2)
                        payout = random.randint(5, 20)
                        if item_upgrade == 1:
                            print("It dropped 2 armour")
                            player_inventory["armour"] = player_inventory["armour"] + 2
                            time.sleep(1)
                            print("+2 armour")
                            player_points[0] = player_points[0] + 10
                        elif item_upgrade == 2:
                            print("It dropped a weapon upgrade")
                            player_inventory["weapon"] = player_inventory["weapon"] + 1
                            time.sleep(1)
                            player_points[0] = player_points[0] + 5
                            print("+1 weapon")
                        time.sleep(3)
                        player_inventory["coins"] = player_inventory["coins"] + payout
                        print("It also dropped", payout, "coins")
                        time.sleep(1)
                        print("+", payout, "coins")
                        time.sleep(2)
                        break
                    else:
                        break
                elif response == 3:
                    time.sleep(1)
                    print("you must roll to see how effective your bargaining skills are.")
                    out = roller_testing()
                    time.sleep(2)
                    if out == 2:
                        coin_num = random.randint(2, 4)
                        print("Your bargaining skills are second to none. You manage to convince the grunt that you are"
                              " not an enemy, and you manage to grab a few coins in the process.")
                        time.sleep(5)
                        player_inventory["coins"] = player_inventory["coins"] + coin_num
                        time.sleep(1)
                        print("+", coin_num, "coins")
                        time.sleep(2)
                        break
                    if out == 1:
                        print("You are just barely persuasive enough to escape, but it'll cost you 10 coins")
                        time.sleep(2)
                        if player_inventory["coins"] >= 10:
                            player_inventory["coins"] = player_inventory["coins"] - 10
                            print("-10 coins")
                            time.sleep(1)
                            break
                        else:
                            print("Unfortunately you couldn't pay up...")
                            time.sleep(1)
                            c_out = combat(enemy_health, enemy_accuracy, strength, "Grunt", 1)
                            if c_out == 1:
                                time.sleep(1)
                                print("Grunt defeated!")
                                time.sleep(2)
                                item_upgrade = random.randint(1, 2)
                                payout = random.randint(5, 20)
                                if item_upgrade == 1:
                                    print("It dropped 2 armour")
                                    player_inventory["armour"] = player_inventory["armour"] + 2
                                    time.sleep(1)
                                    print("+2 armour")
                                    player_points[0] = player_points[0] + 10
                                elif item_upgrade == 2:
                                    print("It dropped a weapon upgrade")
                                    player_inventory["weapon"] = player_inventory["weapon"] + 1
                                    time.sleep(1)
                                    print("+1 weapon")
                                    player_points[0] = player_points[0] + 5
                                time.sleep(3)
                                player_inventory["coins"] = player_inventory["coins"] + payout
                                print("It also dropped", payout, "coins")
                                time.sleep(1)
                                player_points[0] = player_points[0] + payout
                                print("+", payout, "coins")
                                time.sleep(2)
                                break
                            else:
                                break
                    if out == 0:
                        print("Somehow you made it worse for yourself...")
                        player_inventory["health"] = player_inventory["health"] - 2
                        time.sleep(2)
                        player_points[0] = player_points[0] - 5
                        print("-2 health")
                        if player_inventory["health"] <= 0:
                            break
                        time.sleep(1)
                        c_out = combat(enemy_health, enemy_accuracy, strength, "Grunt", 1)
                        if c_out == 1:
                            time.sleep(1)
                            print("Grunt defeated!")
                            time.sleep(2)
                            item_upgrade = random.randint(1, 2)
                            payout = random.randint(5, 20)
                            if item_upgrade == 1:
                                print("It dropped 2 armour")
                                player_inventory["armour"] = player_inventory["armour"] + 2
                                time.sleep(1)
                                print("+2 armour")
                                player_points[0] = player_points[0] + 10
                            elif item_upgrade == 2:
                                print("It dropped a weapon upgrade")
                                player_inventory["weapon"] = player_inventory["weapon"] + 1
                                time.sleep(1)
                                print("+1 weapon")
                                player_points[0] = player_points[0] + 5
                            time.sleep(3)
                            player_inventory["coins"] = player_inventory["coins"] + payout
                            print("It also dropped", payout, "coins")
                            time.sleep(1)
                            print("+", payout, "coins")
                            time.sleep(2)
                            break
                        else:
                            break
            else:
                print("please enter a valid value")
        except ValueError:
            print("please enter a valid value")


def med_enemy():
    print("You are approached by a member of the Mole Council")
    health = random.randint(20, 30)
    accuracy = random.randint(1, 3)
    dmg = random.randint(2, 4)
    a_brk = random.randint(1, 2)
    correct_value = False
    while not correct_value:
        try:
            answer = int(input("Type ( 1 to join the moles and live forever in the dungeon / 2 to attack the Mole "
                               "/ 3 to try and pickpocket the Mole)"))
            if answer == 1:
                diff_count[1] = 1
                return 1
            elif answer == 2:
                c_out = combat(health, accuracy, dmg, "Council member", a_brk)
                if c_out == 1:
                    coins = random.randint(5, 15)
                    print("You defeated them.")
                    time.sleep(1)
                    print("They had a drawing of their mole family in their pocket.")
                    time.sleep(2.5)
                    print("They had some coins and a piece of armour as well...")
                    time.sleep(1.5)
                    player_inventory["armour"] = player_inventory["armour"] + 1
                    player_inventory["coins"] = player_inventory["coins"] + coins
                    print("+", coins, "coins \n+ 1 armour")
                    break
            elif answer == 3:
                print("Roll to see how effective you are")
                out = roller_testing()
                if out == 2:
                    coins = random.randint(10, 20)
                    print("You swipe some of their coins and a strange vial.")
                    player_inventory["coins"] = player_inventory["coins"] + coins
                    time.sleep(1.5)
                    """Hidden Vial stat"""
                    player_points[1] = player_points[1] + 1
                    player_points[0] = player_points[0] + 10
                    print("+", coins, "coins\n+ 1 u̴̠̻͔͙̥̫̰̫̹̹̭̘͗̆̓͐͘̕ͅn̵̨̢̛̼͉̫͕̼͔͎͕̠̜͚̠̽̿̒̉͑̀͜͝k"
                                      "̶̨̛͈͕̞̙̼̻͖͋́͐͐̓̑͗͋̑̿̚͜͠n̷̺̼̯̔͛̈́̏͗̉̓̒͌́ǫ̶̡̛̟̞͓̮̉͋̉̿͐̋͝w̶̡̧̨̞͉̹̬͙̺̮͔̥̒̏̄̔͂̏͝ͅ")
                    time.sleep(1)
                    print("This angers the Mole...")
                    time.sleep(1)
                    c_out = combat(health, accuracy, dmg, "Council member", a_brk)
                    if c_out == 1:
                        coins = random.randint(5, 15)
                        print("You defeated them.")
                        time.sleep(1)
                        print("They had a drawing of their mole family in their pocket.")
                        time.sleep(2.5)
                        print("They had some coins and a piece of armour as well...")
                        time.sleep(1.5)
                        player_inventory["armour"] = player_inventory["armour"] + 1
                        player_inventory["coins"] = player_inventory["coins"] + coins
                        print("+", coins, "coins \n+ 1 armour")
                        break
                elif out == 1:
                    print("You swipe a strange vial")
                    """Hidden Vial stat"""
                    player_points[1] = player_points[1] + 1
                    time.sleep(1)
                    player_points[0] = player_points[0] + 10
                    print("+ 1 u̴̠̻͔͙̥̫̰̫̹̹̭̘͗̆̓͐͘̕ͅn̵̨̢̛̼͉̫͕̼͔͎͕̠̜͚̠̽̿̒̉͑̀͜͝k̶̨̛͈͕̞̙̼̻͖͋́͐͐̓̑͗͋̑̿̚͜͠n"
                          "̷̺̼̯̔͛̈́̏͗̉̓̒͌́ǫ̶̡̛̟̞͓̮̉͋̉̿͐̋͝w̶̡̧̨̞͉̹̬͙̺̮͔̥̒̏̄̔͂̏͝ͅ")
                    time.sleep(1)
                    print("This angers the Mole...")
                    c_out = combat(health, accuracy, dmg, "Council member", a_brk)
                    if c_out == 1:
                        coins = random.randint(5, 15)
                        print("You defeated them.")
                        time.sleep(1)
                        print("They had a drawing of their mole family in their pocket.")
                        time.sleep(2.5)
                        print("They had some coins and a piece of armour as well...")
                        time.sleep(1.5)
                        player_inventory["armour"] = player_inventory["armour"] + 1
                        player_inventory["coins"] = player_inventory["coins"] + coins
                        print("+", coins, "coins \n+ 1 armour")
                        break
                elif out == 0:
                    print("You are caught in the action...")
                    time.sleep(1)
                    if player_inventory["armour"] >= 1:
                        print("- 1 armour")
                        player_inventory["armour"] = player_inventory["armour"] - 1
                        print("This angers the Mole...")
                        c_out = combat(health, accuracy, dmg, "Council member", a_brk)
                        if c_out == 1:
                            coins = random.randint(5, 15)
                            print("You defeated them.")
                            time.sleep(1)
                            print("They had a drawing of their mole family in their pocket.")
                            time.sleep(2.5)
                            print("They had some coins and a piece of armour as well...")
                            time.sleep(1.5)
                            player_inventory["armour"] = player_inventory["armour"] + 1
                            player_inventory["coins"] = player_inventory["coins"] + coins
                            print("+", coins, "coins \n+ 1 armour")
                            break
                    else:
                        print("This angers the Mole...")
                        c_out = combat(health, accuracy, dmg, "Council member", a_brk)
                        if c_out == 1:
                            coins = random.randint(5, 15)
                            print("You defeated them.")
                            time.sleep(1)
                            print("They had a drawing of their mole family in their pocket.")
                            time.sleep(2.5)
                            print("They had some coins and a piece of armour as well...")
                            time.sleep(1.5)
                            player_inventory["armour"] = player_inventory["armour"] + 1
                            player_inventory["coins"] = player_inventory["coins"] + coins
                            print("+", coins, "coins \n+ 1 armour")
                            break
            else:
                print("please enter a valid value")
            if player_inventory["health"] <= 0:
                break
        except ValueError:
            print("please enter a valid value")


def rat_enemy():
    sw_members = random.randint(20, 30)
    sw_stat = random.randint(2, 3)
    time.sleep(1)
    print("You come across a swarm of rats...")
    time.sleep(1)
    correct_value = False
    while not correct_value:
        try:
            answer = int(input("Type( 1 to run from the rats / 2 to attack the swarm / 3 to drop "
                               "u̴̠̻͔͙̥̫̰̫̹̹̭̘͗̆̓͐͘̕ͅn̵̨̢̛̼͉̫͕̼͔͎͕̠̜͚̠̽̿̒̉͑̀͜͝k̶̨̛͈͕̞̙̼̻͖͋́͐͐̓̑͗͋̑̿̚͜͠n"
                               "̷̺̼̯̔͛̈́̏͗̉̓̒͌́ǫ̶̡̛̟̞͓̮̉͋̉̿͐̋͝w̶̡̧̨̞͉̹̬͙̺̮͔̥̒̏̄̔͂̏͝ͅ )"))
            time.sleep(1)
            if answer == 1:
                chance = random.randint(1, 3)
                if chance > 1:
                    print("This was the right decision, the rats want nothing to do with you.")
                    time.sleep(1)
                    break
                else:
                    print("Running does nothing. Now they have an advantage.")
                    time.sleep(1)
                    player_inventory["health"] = player_inventory["health"] - sw_stat * 2
                    print("-", sw_stat*2, "health")
                    time.sleep(1)
                    out = combat(sw_members, sw_stat, sw_stat, "the Swarm", 1)
                    if out == 1:
                        time.sleep(1)
                        print("You defeat the Swarm")
                        time.sleep(1)
                        print("they mostly drop garbage")
                        time.sleep(1)
                        player_inventory["coins"] = player_inventory["coins"] + int(sw_stat * 2)
                        player_inventory["health"] = player_inventory["health"] + 1
                        print("+", int(sw_stat * 2), "coins")
                        print("+1 health")
                        break
                    elif out == 0:
                        time.sleep(1)
                        print("You were overrun by the swarm")
                        break
            elif answer == 2:
                print("You challenge the swarm...")
                time.sleep(1)
                out = combat(sw_members, sw_stat, sw_stat, "the Swarm", 1)
                if out == 1:
                    time.sleep(1)
                    print("You defeat the Swarm")
                    time.sleep(1)
                    print("they mostly drop garbage")
                    time.sleep(1)
                    player_inventory["coins"] = player_inventory["coins"] + int(sw_stat * 2)
                    player_inventory["health"] = player_inventory["health"] + 1
                    print("+", int(sw_stat*2), "coins")
                    print("+ 1 health")
                    break
                elif out == 0:
                    time.sleep(1)
                    print("You were overrun by the swarm...")
                    break
            elif answer == 3:
                if player_points[1] >= 1:
                    winnings_c = random.randint(15, 30)
                    winnings_h = random.randint(3, 6)
                    print("You drop a Vial")
                    time.sleep(1)
                    print("the rats come under your spell and go to collect you treasures")
                    time.sleep(1)
                    player_inventory["coins"] = player_inventory["coins"] + winnings_c
                    player_inventory["health"] = player_inventory["health"] + winnings_h
                    print("+", winnings_c, "coins")
                    print("+", winnings_h, "health")
                    time.sleep(1)
                    break
                else:
                    print("You have nothing. Now they have an advantage.")
                    time.sleep(1)
                    player_inventory["health"] = player_inventory["health"] - sw_stat * 2
                    print("-", sw_stat * 2, "health")
                    time.sleep(1)
                    out = combat(sw_members, sw_stat, sw_stat, "the Swarm", 1)
                    if out == 1:
                        time.sleep(1)
                        print("You defeat the Swarm")
                        time.sleep(1)
                        print("they mostly drop garbage")
                        time.sleep(1)
                        player_inventory["coins"] = player_inventory["coins"] + int(sw_stat * 2)
                        player_inventory["health"] = player_inventory["health"] + 1
                        print("+", int(sw_stat * 2), "coins")
                        print("+1 health")
                        break
                    elif out == 0:
                        time.sleep(1)
                        print("You were overrun by the swarm")
                        break
            else:
                print("please enter a valid value")
            if player_inventory["health"] <= 0:
                break
        except ValueError:
            print("please enter a valid value")


def introduction():
    """Sets up the user to play the game"""
    start = False
    while not start:
        beginning = input("Welcome to ""Roll"". To begin playing type begin").lower()
        if beginning == "begin":
            start = True
    """Introductory section and tutorial"""
    tutorial_go = input("would you like the tutorial (yes/no)").lower()
    if tutorial_go == "yes":
        print("To start we will learn the dice rolling mechanics. \n\nGuess the roll correctly for a reward and "
              "incorrectly to suffer.")
        out = roller_testing()
        time.sleep(2)
        """reads output from dice roll"""
        if out == 2:
            print("Guessing correctly has positive outcomes.")
        elif out == 1:
            print("Guessing close will give you a small positive or neutral outcome.")
        elif out == 0:
            print("Missing your guess wil result in a neutral or negative outcome.")
        time.sleep(3)
        print("\nRolling benefits can include coins, better hits, and easier gameplay in general.")
        time.sleep(3)
        print("your inventory looks like this\n-------------------------------------------------------\n",
              player_inventory, "\n-------------------------------------------------------")
        time.sleep(5)
        print("It contains all your important information.")
        time.sleep(3)
        print("There are a few stats in there. This includes your coins, which is the game currency.\nYou can use coins"
              " to buy armour health and weapon upgrades.\nArmour will be useful in combat, and to help you escape "
              "some traps.\nHealth is pretty self explanatory, run out and you die.\nThe weapon stat shows your"
              " damage multiplier. In essence, when fighting any damage done wil be multiplied by your weapon number."
              "\n")
        time.sleep(25)
        print("You will also collect points as you travel through the dungeon. Your points will display after you die, "
              "or exit the dungeon.")
        time.sleep(4)
        player_points[0] = player_points[0] + 10
        print("Other than that, just follow the instructions!\n")
        time.sleep(3)
        print("****** Tutorial Finished ******\n")


def room_config():
    room_num = random.randint(5, 10)
    iterations = random.randint(3, 5)
    for i in range(iterations):
        if player_inventory["health"] <= 0:
            time.sleep(2)
            break
        for k in range(room_num):
            room_typ = random.randint(1, 6)
            if player_inventory["health"] <= 0:
                time.sleep(2)
                break
            else:
                if room_typ == 1 or room_typ == 2:
                    passage()
                elif room_typ == 3 or room_typ == 4:
                    trap()
                    print("---------------------------------------")
                elif room_typ == 5:
                    merchant()
                    print("---------------------------------------")
                elif room_typ == 6:
                    rat = random.randint(1, 3+diff_count[2])
                    if rat > 3:
                        rat_enemy()
                        print("---------------------------------------")
                    else:
                        chest()
                        print("---------------------------------------")
        if player_inventory["health"] <= 0:
            break
        merchant()
        print("---------------------------------------")
        if diff_count[0] >= 2:
            med_enemy()
            diff_count[0] = diff_count[0] + 1
            if player_inventory["health"] <= 0 or diff_count[1] == 1:
                break
            print("---------------------------------------")
            time.sleep(2)
        else:
            low_enemy()
            diff_count[0] = diff_count[0] + 1
            if player_inventory["health"] <= 0:
                break
            print("---------------------------------------")
            time.sleep(2)
    if player_inventory["health"] <= 0 or diff_count[1] == 1:
        return
    boss()


def playing():
    in_play = True
    while in_play:
        diff_count[0] = 0
        diff_count[1] = 0
        diff_count[2] = 0
        print("          ┌───┐    ┌┐ ┌┐ \n          │┌─┐│    ││ ││ \n          │└─┘│┌──┐││ ││ \n          "
              "│┌┐┌┘│┌┐│││ ││ \n          │││└┐│└┘││└┐│└┐\n          └┘└─┘└──┘└─┘└─┘\n")
        player_inventory["coins"] = 15
        player_inventory["armour"] = 0
        player_inventory["health"] = 20
        player_inventory["weapon"] = 1
        player_points[0] = 0
        player_points[1] = 0
        room_config()
        if player_inventory["health"] <= 0:
            print(player_inventory["health"])
            print("Your health reached or dropped below zero.\nYou Died in the dungeon.")
            print("you had", int(player_points[0]) * 10, "points")
        elif diff_count[1] == 1:
            print("You join the moles underground, and the rest of your life is spent in servitude to the Mole King.")
            time.sleep(2)
            print("Your life is peaceful, but you will never forget blue skies and the stars at night...")
            time.sleep(2)
            print("you ended your journey with", int(player_points[0]) * 10, "points\n", player_inventory["coins"],
                  "coins\n", player_inventory["armour"], "armour\n", player_inventory["health"], "health\n",
                  player_inventory["weapon"], "weapon upgrades")
        else:
            time.sleep(2)
            print("You can finally escape the dungeon")
            time.sleep(1)
            print("The sound of wind flowing across the landscape brings a sense of calmness.")
            time.sleep(2)
            print("you escaped with", int(player_points[0]) * 10, "points\n", player_inventory["coins"], "coins\n",
                  player_inventory["armour"], "armour\n", player_inventory["health"], "health\n",
                  player_inventory["weapon"], "weapon upgrades")
            time.sleep(3)
            """All 5 special endings"""
            if player_points[1] >= 2:
                print("You remember the mystery vials still in your pocket, so you open them and a strange gas escapes."
                      )
                time.sleep(2)
                print("A cloud starts to form and the ground begins to shake.")
                time.sleep(1)
                print("Then it begins to pour rain, and you see the army of moles returning.")
                time.sleep(1.5)
                print("The cloud surrounds you and the mole people bow before you.")
                time.sleep(1.5)
                print("\nYou have become\n")
                time.sleep(2)
                print("The Mole King")
            elif player_inventory["coins"] >= 50:
                print("You escaped rich, and surely prosperity will follow you.")
            elif player_inventory["weapon"] >= 15:
                print("With your skill earned in the dungeon you've become the deadliest adventurer in the land.")
            elif player_inventory["armour"] >= 10:
                print("You've become unstoppable with layers and layers of armour protecting you. A tank of a person, "
                      "nobody is going to mess with you.")
            elif player_inventory["health"] >= 25:
                print("Your health is incredible. You will live for years and years wondering the land, "
                      "legends will be told far in the future of your never ending life")
            time.sleep(3)
        time.sleep(3)
        loop = True
        while loop:
            again = input("Would you like to play again?(yes/no)").lower()
            if again == "yes":
                break
            elif again == "no":
                in_play = False
                break
            else:
                print("Please type yes or no")


introduction()
playing()
