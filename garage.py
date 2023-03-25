class garage():

    spaces = [0, 0, 0, 0, 0]
    tickets = [1, 2, 3, 4, 5]
    currentTicket = {
        "1": False,
        "2": False,
        "3": False,
        "4": False,
        "5": False,
        }

    def __init__(self, spaces, ticket, currentTicket):
        self.spaces = spaces #list
        self.tickets = ticket #list
        self.currentTicket = currentTicket

    def takeTicket(self):
        #- This should decrease the amount of tickets available by 1
        #- This should decrease the amount of parkingSpaces available by 1
        for space in spaces:
            if space == 0:

                self.tickets = self.tickets.remove(ticket)
                self.spaces = self.spaces.remove(spaces)

            else:
                print("Garage is full. Go away. Come back another day.")
                return

    def payForParking(self):
        ticketNumber = int(input("Enter ticket numer."))
        if ticketNumber in self.currenTicket.keys():
            payment = int(input("Please enter payment"))
            if payment == 20:
                self.currentTicket[ticketNumber] = True
                print("Your ticket has been paid! You have 15 minutes to leave.")
            else:
                print("Parking costs $20. Please pay the correct amount.")
        elif ticketNumber not in self.currentTicket.keys():
            print("That ticket number is incorrect. Please enter the correct ticket number.")
            
        #- Display an input that waits for an amount from the user and store it in a variable
        #- If the payment variable is not empty then (meaning the ticket has been paid) ->  display a message to the user that their ticket has been paid and they have 15mins to leave
        #- This should update the "currentTicket" dictionary key "paid" to True

    
    def leaveGarage(self):
        #- If the ticket has been paid, display a message of "Thank You, have a nice day"
        #- If the ticket has not been paid, display an input prompt for payment
        #- Once paid, display message "Thank you, have a nice day!"
        #- Update parkingSpaces list to increase by 1 (meaning add to the parkingSpaces list)
        #- Update tickets list to increase by 1 (meaning add to the tickets list)


car1 = garage(spaces, tickets, currentTicket)
garage.takeTicket()
garage.payForParking()
garage.leaveGarage()
