import os


def clear_console():
    if os.name == 'nt':
        os.system('cls')
    
    else:
        os.system('clear')


def get_start_num():
    start_num = input("Enter a starting number:\n>>>> ")

    while start_num.isdigit() == False:
        clear_console()

        print("Please enter a valid number.")

        start_num = input("Enter a starting number:\n>>>> ")

    return start_num


def get_n_terms():
    n = input("\nEnter the amount of terms to show:\n>>>> ")

    while n.isdigit() == False:
        clear_console()

        print("Please enter a valid number.")

        n = input("Enter the amount of terms to show:\n>>>> ")

    return int(n)


def next_num(start_num, n):
    for i in range(1, n):
            results = []

            repeat_counter = 1

            for num in range(0, len(start_num)):
                try:
                    if start_num[num] == start_num[num + 1]:
                        repeat_counter += 1

                    else:
                        results.append(str(repeat_counter))

                        results.append(start_num[num])

                except IndexError:
                    results.append(str(repeat_counter))

                    results.append(start_num[num])

            results = "".join(results)

            print(results)

            start_num = results


def look_say_seq():
    clear_console()
    
    start_num = get_start_num()

    n = get_n_terms()
    
    clear_console()
    
    if n == 1:
        print("Starting at {}, the 1 term in the sequence is: {}".format(start_num, start_num))

    else:
        print("Starting at {}, the {} terms in the sequence are:\n{}".format(start_num, n, start_num))

        next_num(start_num, n)


def main():
    look_say_seq()


if __name__ == "__main__":
    main()