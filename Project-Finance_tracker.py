# Expense-Tracker project using loops,conditionals,list,dictionaries

print(" Finance-Expense Tracker ");

Expenses=[];                                               # using list of dictionaries as the primary storage concept

print("Welcome to our expense tracker !");

while True:
    print("=======MENU=======");
    print("1. Add Expense");
    print("2. View Expenses");
    print("3. Delete Expense");
    print("4. Exit");

    choice=int(input("Enter your choice (1-4) : "));                    # asking for choice of user

    if choice==1:                                                       # adding expenses in tracker
        name=input("Enter expense name : ");
        amount=float(input("Enter expense amount : "));
        category=input("Enter expense category : ");
        date=input("Enter expense date (YYYY-MM-DD) : ");
        expense={"Name":name,"Amount":amount,"Category":category,"Date":date};
        Expenses.append(expense);
        print("Expense added successfully !");

    elif choice==2:                                                       # viewing expenses of user
        if  len(Expenses)==0:
            print("No expenses to show !");
        else:
            for i,expense in enumerate(Expenses):
                print(f"{i+1}. {expense['Name']} - ${expense['Amount']} - {expense['Category']} - {expense['Date']}");

    elif choice==3:
        if not Expenses:
            print("No expenses to delete !");
        else:
            for i,expense in enumerate(Expenses):
                print(f"{i+1}. {expense['Name']} - ${expense['Amount']} - {expense['Category']} - {expense['Date']}");
            del_choice=int(input("Enter the number of the expense to delete : "));
            if 1<=del_choice<=len(Expenses):
                del Expenses[del_choice-1];
                print("Expense deleted successfully !");
            else:
                print("Invalid choice !");

    elif choice==4:
        print("Exiting the expense tracker. Goodbye !");
        break;

    else:
        print("Invalid choice ! Please enter a number between 1 and 4.");

