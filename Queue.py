class stack :
    i = []
    def stackout(self) :
        self.i.pop(0)   
    def stackin(self , f) :
        self.i.append(f)

def main() :
    x = stack()
    while True :
        print(x.i)
        print( 'choose what to do in the queue    1- insert 2- remove 3- end the program')
        decision = (input('enter you choice ....'))
        if decision == '1':
            x.stackin(input("pleast enter an element to insert")) 
        elif decision == '2':
            if len(x.i) == 0:
              print("list is clear .... you must enter elements in the list first")
            else:
               x.stackout()
        elif decision == '3':
            break
            
        else:
             print ('enter a proper input')
  
    
main()
    