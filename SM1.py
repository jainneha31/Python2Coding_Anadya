def even_odd_swap(x):
    if len(x) % 2 != 0:
        x = x + " "

    even_letters = x[0::2]
    odd_letters = x[1::2]
    s = ""

    for i in range(len(even_letters)):
        s = s + odd_letters[i]
        s = s + even_letters[i]

    return s


def swap_middle(x):
    if len(x) % 2 != 0:
        x = x + " "

    first_half = x[0 : int(len(x) / 2) : 1]
    second_half = x[int(len(x) / 2) :: 1]

    s = ""
    s = s + second_half
    s = s + first_half
    return s


def reverse(x):
    s = x[::-1]
    return s


def swap_mid_rev(x):
    s_swap = swap_middle(x)
    s = reverse(s_swap)
    return s


def swap_mid_rev_decode(x):
    s_rev = reverse(x)
    s = swap_middle(s_rev)
    return s


def reverse_word(x):
    words = x.split(" ")
    s = ""
    for kk in range(len(words)):
        s = s + reverse(words[kk]) + " "
    return s


import random

codenames = [
    "Red Falcon",
    "Ghost Raven",
    "Dark Cobra",
    "Iron Shadow",
    "Silent Fox",
    "Neon Viper",
    "Silver Wolf",
    "Midnight Owl",
    "Steel Hawk",
    "Blue Cheetah",
    "Cold Panther",
    "Rogue Eagle",
    "Golden Tiger",
    "Velvet Spider",
    "Arctic Lynx",
]


actions = [
    "transmits",
    "intercepts",
    "shadows",
    "bypasses",
    "observes",
    "secures",
    "breaches",
    "clones",
    "monitors",
    "uploads",
    "follows",
    "infiltrates",
    "disables",
    "extracts",
    "scouts",
]


descriptors = [
    "encoded",
    "encrypted",
    "classified",
    "hidden",
    "secure",
    "digital",
    "locked",
    "private",
    "suspicious",
    "corrupted",
    "priority",
    "remote",
    "laser",
    "sensitive",
    "forbidden",
]


targets = [
    "files",
    "signal",
    "laptop",
    "bunker",
    "briefcase",
    "assets",
    "gateway",
    "server",
    "package",
    "database",
    "suspect",
    "station",
    "circuit",
    "intel",
    "sector",
]


def generate_secret_phrase():
    phrase_parts = [
        random.choice(codenames),
        random.choice(actions),
        random.choice(descriptors),
        random.choice(targets),
    ]
    return " ".join(phrase_parts).upper()


x = generate_secret_phrase()


x_even_odd = even_odd_swap(x)

x_rev = reverse(x)

x_rev_word = reverse_word(x)

x_swap_mid = swap_middle(x)

x_swap_mid_rev = swap_mid_rev(x)

print("Today, you are being tested if you would make a good spy.\n")
print("You will be given a secret phrase and you will have to decode it.\n")
print("You have 5 chances. Go DECODE!\n")


print("Secret phrase:", x_even_odd)
guess = input("Enter your guess: ").upper()
if guess == x:
    print("Congratulations! You have decoded the secret phrase.")
    print("You are a GOOD spy!")
else:
    print("Secret phrase:", x_rev)
    guess2 = input("Enter your 2nd guess:  ").upper()
    if guess2 == x:
        print("Congratulations! You have decoded the secret phrase.")
        print("You are a GOOD spy!")
    else:
        print("Secret phrase:", x_rev_word)
        guess3 = input("Enter your 3rd guess:  ").upper()
        if guess3 == x:
            print("Congratulations! You have decoded the secret phrase.")
            print("You are a GOOD spy!")
        else:
            print("Secret phrase:", x_swap_mid)
            guess4 = input("Enter your 4th guess:  ").upper()
            if guess4 == x:
                print("Congratulations! You have decoded the secret phrase.")
                print("You are a GOOD spy!")
            else:
                print("Secret phrase:", x_swap_mid_rev)
                guess5 = input("Enter your 5th guess:  ").upper()
                if guess5 == x:
                    print("Congratulations! You have decoded the secret phrase.")
                    print("You are a GOOD spy!")
                else:
                    print("Sorry, you have failed to decode the secret phrase.")
                    print("You make a BAD spy!")
                    print(f"The secret phrase was: {x}")
