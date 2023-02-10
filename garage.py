

class ParkingGarage():
    price = 7.50
    

    def __init__(self, tickets, parkingSpaces, currentTicket):
        self.tickets = tickets              #expected list
        self.parkingSpaces = parkingSpaces  #expected list
        self.currentTicket = currentTicket  #expected dict

    
    def fillGarage(self):
        for i in range(10):
            self.ticket = "TICKET" + " " + str(i)
            self.space = "SPACE" + " " + str(i)
            self.tickets.append(self.ticket)
            self.parkingSpaces.append(self.space)

    
    def takeTicket(self):
        input_start = input("Please take a ticket (Type 'take'): ")
        if input_start.lower() == 'take':
            if len(self.tickets) > 0:  
                dict_ticket = self.tickets.pop()
                self.parkingSpaces.pop()
                self.currentTicket['taken'] = dict_ticket
            else:
                print("Sorry, we are all out of tickets.")

        # decrease tickets by 1
        # decrease spaces available by 1

    def payForParking(self):
        print(f"Your total is ${self.price}, please pay below:")
        self.payment = float(input("Payment: $"))
        if self.payment > self.price:
            change = self.payment - self.price
            print(f" Payment complete!\n${change} is your change. Please exit within the next 15 minutes. ")
            transfer = self.currentTicket.pop('taken')
            self.currentTicket['paid'] = transfer
        elif self.payment == self.price:
            print("Payment Complete! Please exit within the next 15 minutes. ")
            transfer = self.currentTicket.pop('taken')
            self.currentTicket['paid'] = transfer


        # display input prompting payment
        # updates currentticket dictionary key to paid

    def leaveGarage(self):
        if self.ticket in self.currentTicket['paid']:
            print("Thank you, have a nice day!")
            self.tickets.append(self.ticket)
            self.parkingSpaces.append(self.space)
        else:
            print("Please pay before leaving.")

        # check if ticket has been paid
        # updates parkingspaces +1
        # updates tickets +1
    


initial = ParkingGarage([],[], {'taken': '[]', 'paid': '[]'})

def run():
    initial.fillGarage()
    initial.takeTicket()    
    initial.payForParking()
    initial.leaveGarage()

run()

