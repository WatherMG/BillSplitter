count_of_friends = int(input("Enter the number of friends joining (including you):\n"))
if count_of_friends > 0:
    print("Enter the name of every friend (including you), each on a new line:")
    list_of_friends = [input() for _ in range(count_of_friends)]
    friends = {}.fromkeys(list_of_friends, 0)
    print(friends)
else:
    print("\nNo one is joining for the party")
