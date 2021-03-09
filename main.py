#!/usr/bin/env python3
        
import json

import coords    as cd
import customers as cs

# Class representing the application
class App:
    office    = None
    customers = None
    invited   = None

    # Construction initializes the terms
    def __init__(self):
        self.office    = cd.Coords(53.339428, -6.257664)
        self.customers = []
        self.invited   = []

    # Reads the customer from a file, provided by caller
    def read_customers(self, fname):
        # Clears previous configuration
        self.customers.clear()

        # Closes the file when f gets out of scope
        with open(fname, 'r') as f:
            for line in f:
                # I'm parsing the json here and converting the data to the types
                # expected by the internal apis.
                jsline = json.loads(line)
                coords = cd.Coords(
                    float(jsline['latitude']),
                    float(jsline['longitude'])
                )
                self.customers.append(
                    cs.Customer(jsline['user_id'], jsline['name'], coords)
                )

    # Invites all customers inside a circle radius (projected on Earth)
    def invite_near_customers(self, distance):
        # Clears previous configuration
        self.invited.clear()

        for customer in self.customers:
            # Check distance between office and customer
            dst = customer.coords.distance(self.office)
            # Invites if less than argument
            if dst <= distance:
                self.invited.append(customer)

        # The list is sorted in ascending order by user_id
        self.invited.sort(key = lambda c: c.user_id)

    # Write the invited array to file
    def write_invited(self, fname):
        with open(fname, 'w+') as f:
            # Just go through all the invited customers in the array and 
            # print their id and name separated by a single tab to file
            for customer in self.invited:
                f.write('{}\t{}\n'.format(customer.user_id, customer.name))

# If the script is being run instead of imported for testing,
# Execute the program
if __name__ == '__main__':
    import sys 

    # Collect the arguments of the program, if they have been passed.
    # Otherwise, assigns default values
    dst      = int(sys.argv[1]) if len(sys.argv) > 1 else 100
    inp_file = sys.argv[2] if len(sys.argv) > 2 else 'customers.txt'
    out_file = sys.argv[3] if len(sys.argv) > 3 else 'output.txt'

    # Application execution
    app = App()
    app.read_customers(inp_file)
    app.invite_near_customers(dst)
    app.write_invited(out_file)

