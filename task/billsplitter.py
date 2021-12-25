import random


def bill_share(bill_, friends_):
    return round(bill_ / friends_, 2)


count_of_friends = int(input("Enter the number of friends joining (including you):\n"))
try:
    assert count_of_friends > 1, "\nNo one is joining for the party"
    print("\nEnter the name of every friend (including you), each on a new line:")
    list_of_friends = [input() for _ in range(count_of_friends)]
    bill = int(input("\nEnter the total bill value:\n"))
    lucky = input('\nDo you want to use the "Who is lucky?" feature? Write Yes/No:\n')
    lucky_name = random.choice(list_of_friends)
    friends = {}.fromkeys(list_of_friends, bill_share(bill, count_of_friends))
    if lucky == "Yes":
        print(f"\n{lucky_name} is the lucky one!\n")
        friends = {key: bill_share(bill, (count_of_friends - 1)) for key, value in friends.items() if key != lucky_name}
        friends[lucky_name] = 0
    else:
        print("\nNo one is going to be lucky\n")
    print(friends)
except AssertionError as error:
    print(error)
