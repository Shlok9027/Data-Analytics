
num_1 = float(input("Enter the Num 1 : "));
num_2 = float(input("Enter the num 2 : "));


choice = input("Enter the operation you want to perfrom [+ , - , * , / ,%] : ");


if choice == "+" :
    print(f'Addition : {num_1 + num_2}');
elif choice == "-" : 
    print(f'Substraction : {num_1 - num_2}');
elif choice == "*":
    print(f'Multipliction : {num_1 * num_2}');

elif choice == '/':
    print(f'Division : {num_1 / num_2}');
elif choice == '%':
    print(f'Modulus : {num_1 % num_2}')