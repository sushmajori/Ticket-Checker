from LINKED_LIST import * # import all the data from LINKED_list file

# start of program

# variables initialization
i=1
seat_no=0
prn=1234561230
while True: # start of while
    # try and except for handling exceptions
    try:
        # different choices for user
        print("\n1.Create Object")
        print("\n2.Insert the data about seat details of particular coach")
        print("\n3.Search the seat in the coach")
        print("\n4.Mark present or absent to seat ")
        print("\n5.Allocate new seat to vacant place")
        print("\n6.Display Reserved Seats")
        print("\n7.Display count of Vacant Seats ")
        print("\n8.Exit\n")
        ch=int(input())
        # comparing user choice
        if ch==1:
            linkedlist=LinkedList() #create object of Linked list
            newlinkedlist=LinkedList()
        elif ch==2:
            size1=linkedlist.size()
            #print(size1)
            # verify size is less then 20
            if size1==0 or size1<21:
                    
                Passenger_Name=input("\nEnter Name of Passenger : \n")
                #validation of input
                while True:
                    try:
                        if len(Passenger_Name)>4 and Passenger_Name!=None and type((Passenger_Name))==str:
                            Passenger_Name=Passenger_Name
                            break
                        else:
                            raise Exception("\nError Occured : Please Eneter Valid Passenger Name : \n")
                    except Exception as e:
                        Passenger_Name=input(e)
                        continue
                
                Gender=input("\nEnter Type Of Gender : \n")
                #validation of input
                while True:
                    try:
                        if (len(Gender)==6 or len(Gender)==4) and (Gender=="Female" or Gender=="Male" ) \
                        and Gender!=None and type(Gender)==str:
                            Gender=Gender
                            break
                        else:
                            raise Exception("\nError Occured : Please Eneter Valid Gender Type (Female or Male) : \n")
                    except Exception as e:
                        Gender=input(e)
                        continue
                
                age=int(input("\nEnter Age : \n"))
                #validation of input
                while True:
                    try:
                        if (age)>8 and age!=None and type((age))==int:
                            age=age
                            break
                        else:
                            raise Exception("\nError Occured : Please Eneter Valid age : \n")
                    except Exception as e:
                        age=input(e)
                        continue
                
                seat_no=seat_no+i
                prn=prn+i
                i=i+1
                #call to insertEnd method for insert data
                linkedlist.insertEnd([seat_no,prn,Passenger_Name,Gender,age])
                print("\nYour Seat Details : \n")
                linkedlist.printEnd() # for print current user details

        elif ch==3:
            try:
                seat_no1=int(input("\nEnter the Seat Number : "))
            except:
                print("\nNot Valid Seat Number")

            linkedlist.linearsearch(seat_no1)#call to method for searching data

        elif ch==4:
            
            linkedlist.assign_status(newlinkedlist)#call to method for assigning present or absent status
            
        elif ch==5:
            size=linkedlist.size()#call to size method to calculate size of stack
            if size==20:
                print("\nNo Vacant Seats are Available")
                # check the size of list , if less then 20 then only allow to reserve
            elif size<20:
                Passenger_Name=input("\nEnter Name of Passenger : \n")
                #validation of input
                while True:
                    try:
                        if len(Passenger_Name)>4 and Passenger_Name!=None and type((Passenger_Name))==str:
                            Passenger_Name=Passenger_Name
                            break
                        else:
                            raise Exception("\nError Occured : Please Eneter Valid Passenger Name : \n")
                    except Exception as e:
                        Passenger_Name=input(e)
                        continue
                
                Gender=input("\nEnter Type Of Gender : \n")
                #validation of input
                while True:
                    try:
                        if (len(Gender)==6 or len(Gender)==4) and (Gender=="Female" or Gender=="Male" ) \
                        and Gender!=None and type(Gender)==str:
                            Gender=Gender
                            break
                        else:
                            raise Exception("\nError Occured : Please Eneter Valid Gender Type (Female or Male) : \n")
                    except Exception as e:
                        Gender=input(e)
                        continue
                
                age=int(input("\nEnter Age : \n"))
                #validation of input
                while True:
                    try:
                        if (age)>8 and age!=None and type((age))==int:
                            age=age
                            break
                        else:
                            raise Exception("\nError Occured : Please Eneter Valid age : \n")
                    except Exception as e:
                        age=input(e)
                        continue
                
                seat_no=seat_no+i
                prn=prn+i
                i=i+1
                #call to insertEnd method for insert data
                linkedlist.insertEnd([seat_no,prn,Passenger_Name,Gender,age])
                print("\nYour Seat Details : ")
                linkedlist.printEnd()
                LinkedList.Allocate_Seats()
        elif ch==6:
            linkedlist.printList()#call to method for Displaythe data
        elif ch==8:
            break
        elif ch==7:
            size=linkedlist.size()
            total=20-size
            print("\nTotal Vacant seat Count is ",total)

        else: # default case
            print("\nWrong Choice\n")

    except:
        continue # go to while loop


