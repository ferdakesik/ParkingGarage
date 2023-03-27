class Garage():

    def __init__(self):
        self.spaces = 5
        self.currentTicket = {
            "1": False,
            "2": False,
            "3": False,
            "4": False,
            "5": False,
            }

    def takeTicket(self):
        #- This should decrease the amount of tickets available by 1
        #- This should decrease the amount of parkingSpaces available by 1

        if self.spaces <= 5 and self.spaces > 0:
            print(f"You have ticket number {self.spaces}.\n")
            self.spaces -= 1

        else:
            print("Garage is full. Go away. Come back another day.")
            return

    def payForParking(self):
        ticketNumber = input("Enter ticket numer. ")
        if ticketNumber in self.currentTicket.keys():
            payment = int(input("Please enter payment "))
            if payment == 20:
                self.currentTicket[ticketNumber] = True
                print("Your ticket has been paid! You have 15 minutes to leave.")
            elif payment > 20:
                print("Thanks for the extra cash!")
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
        ticketNumber=input("\nEnter your ticket number? ")
        
        if self.currentTicket[ticketNumber]==True:
            print("Thank you, have a great day. Drive safe. Don't play with ya phone fool!\n")
            self.spaces =+ 1
            self.currentTicket[ticketNumber]=False
            
            
        elif self.currentTicket[ticketNumber]==False:
            print("Please pay for parking rate!\n")
            self.payForParking()
            
        else:
           print("Something is not valid.")            
            
            
        #- If the ticket has not been paid, display an input prompt for payment
        #- Once paid, display message "Thank you, have a nice day!"
        #- Update parkingSpaces list to increase by 1 (meaning add to the parkingSpaces list)
        #- Update tickets list to increase by 1 (meaning add to the tickets list)


class Kiosk():
    parking = Garage()
    @classmethod
    def main(self):
        while True:
            decision = input("What would you like to do? 1 = [take ticket] / 2 = [pay] / 3 = [leave Garage] ")
            if decision == "close":
                break

            elif decision == "1":
                self.parking.takeTicket()

            elif decision == "2":
                self.parking.payForParking()

            elif decision == "3":
                self.parking.leaveGarage()

            else:
                print("Not a valid command. Try again.")
            

if __name__ == "__main__":
    Kiosk.main()
