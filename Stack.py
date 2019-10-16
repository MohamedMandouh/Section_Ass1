def main() :
    x=[]
    while x :
        print(x)
        print( 'choose what to do in the queue    1- insert 2- remove 3- end the program')
        decision = (input('enter you choice ....'))
        
        if decision == '1':
            x.append(input("pleast enter an element to the insert")) 
        elif decision == '2':
            if len(x) == 0:
              print("list is clear .... you must enter elements in the list first")
            else:
               x.pop()
        elif decision == '3':
            break
            
        else:
             print ('enter a proper input')
  
    
main()
    