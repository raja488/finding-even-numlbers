def is_even_or_odd(user_input):
    if user_input %2==0:
        print("your number is even ")
    else:
        print("your number is odd ")


if __name__ == "__main__":
    user_input=int(input("enter a number:"))
    is_even_or_odd(user_input)
    
