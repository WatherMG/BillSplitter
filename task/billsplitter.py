import random

count_of_friends = int(input("Enter the number of friends joining (including you):\n"))
try:
    assert count_of_friends > 1, "\nNo one is joining for the party"
    print("\nEnter the name of every friend (including you), each on a new line:")
    list_of_friends = [input() for _ in range(count_of_friends)]
    bill = int(input("\nEnter the total bill value:\n"))
    lucky = input('\nDo you want to use the "Who is lucky?" feature? Write Yes/No:\n')
    friends = {}.fromkeys(list_of_friends, 0)
    if lucky == "Yes":
        print(f"\n{random.choice(list_of_friends)} is the lucky one!")
    else:
        print("\nNo one is going to be lucky")
except AssertionError as error:
    print(error)