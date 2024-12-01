exp_tracker={}
print('EXPENSE TRACKER')
print('<----------------->')
print()
option=0
while option<=7:
        print('1.Initial amount:')
        print('2.Add initial amount')
        print('3.Enter expense:')
        print('4.View Expense:')
        print('5.Edit expense:')
        print('6.Delete expense:')
        print('7.Exit')
        print()
        try:
            option=int(input('Enter your option:'))
            while option<=0 or option>7:
                print('Please enter a valid option')
                option=int(input('Enter your option:'))

    
            if option==1:
                budget=int(input('Enter your budget:'))
                if budget<=0:
                    print('Please enter valid amount')
                else:
                    print('initial amount=',budget)
                    print()

            elif option==2:
                while True:
                    try:
                        add_budget=int(input('Add your extra budget:'))
                        if add_budget>0:
                            budget=budget+add_budget
                            print('Current budget=',budget)
                            break
                        else:
                            print('Please enter a positive integer')
                            
                    except:
                        print('Please enter a valid number!')
                        
            elif option==3:
                while True:
                    expense=input('Enter your expense:')
                    try:
                        amount=int(input('amount:'))
                        if expense in exp_tracker:
                            exp_tracker[expense]+=amount
                            break
                        elif amount<budget:
                            exp_tracker[expense]=amount
                            break
                        else:
                            print('your budget is done,try again after adding new budget')   
                            break
                            
                    except:
                        print('invalid input,Enter a valid integer')
                            
                            
                print('EXPENSE','AMOUNT')
                print('-------','-------')
                bal=0
                for i,j in exp_tracker.items():
                    print(i,'  ',j)
                    bal=bal+j
                bal=budget-bal
                print('----------------')
                print('balance:',bal)
                print('Initial amount=',budget)
                print()
                        
                                    
                        
            elif option==4:
                bal=0
                print('EXPENSE','AMOUNT')
                print('-------','-------')
                for i,j in exp_tracker.items():
                    print(i,'  ',j)
                    bal=bal+j
                bal=budget-bal
                print('----------------')
                print('balance:',bal)
                print('Initial amount=',budget)
                print()
            elif option==5:
                exp=input('which expense you want to edit:')
                if exp in exp_tracker:
                    while True:
                        new_exp=input('change to:')
                        if new_exp=='':
                            print('please enter new expense:')
                        else:
                            if new_exp in exp_tracker:
                                print('Expense already exist')
                                
                            else:
                                break
                    exp_tracker[new_exp]=exp_tracker.pop(exp)
                    print('expense edited')
                else:
                    print('not found')
            elif option==6:
                while True:
                    x=input('which expense you want to delete:')
                    if x in exp_tracker:
                        exp_tracker.pop(x)
                        print('deleted',x)
                        
                    
                        print('Initial amount=',budget)
                        print()
                        break
                    else:
                        print('Expense not found!Please try again')
            elif option==7:
                print('EXIT')
                break
        except:
                        print('its invalid,Try again ')
                    



        
        
