# *************************** List Reverse by Three different Method ***************************

def play_quit():
    play_game = input("\n\nEnter any key to continue or \"Q\" to quit...!")
    if play_game.capitalize() == "Q":
        print(
            "Thanks for your valuable time that you spend with us....! We expect, you will be back soon...! Take care and stay home...!")
        exit()
    else:
        print("Enjoy the programme...!\n")

# First method of list reverse
def reverse_1(): # By using Built-in function
    reverse_1 = list[:]
    reverse_1.reverse()
    print(f"The user list is sorted by builtin method is {reverse_1}")

# Second method of list reverse
def reverse_2(): # List slicing methods
    print(f"The user list is sorted by list slicing method is {list[::-1]}")

# Third method of list reverse
def reverse_3(): # In this method, we alternate the 1st, 2nd, 3rd... with last elements of the list
    for i in range(list_len//2):
        list[i], list[list_len-i-1] = list[list_len-i-1], list[i]
    print(f"The user list is sorted by swapping elements method is {list}")

if __name__ == '__main__':
    
    list = []
    while True:
        
        try:
            list_len = int(input("Enter the length of list:\n"))
            for item in range(list_len):
                list.append(int(input("Enter the list elements one by one:")))
    
        except ValueError:
            print("Invalid Input...!")
            exit()
    
        print(f"Your list is {list}\n")

        reverse_1()
        reverse_2()
        reverse_3()
        play_quit()

