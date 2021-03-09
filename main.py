#!/usr/bin/env python3
        
import json

import coords    as cd
import customers as cs

class App:
    office    = None
    customers = None
    invited   = None

    def __init__(self):
        self.office    = cd.Coords(53.339428, -6.257664)
        self.customers = []
        self.invited   = []

    def read_customers(self, fname):
        self.customers.clear()
        with open(fname, 'r') as f:
            for line in f:
                jsline = json.loads(line)
                coords = cd.Coords(
                    float(jsline['latitude']),
                    float(jsline['longitude'])
                )
                self.customers.append(
                    cs.Customer(jsline['user_id'], jsline['name'], coords)
                )

    def invite_near_customers(self, distance):
        self.invited.clear()
        for customer in self.customers:
            dst = customer.coords.distance(self.office)
            if dst <= distance:
                self.invited.append(customer)
        self.invited.sort(key = lambda c: c.user_id)

    def write_invited(self, fname):
        with open(fname, 'w+') as f:
            for customer in self.invited:
                f.write('{}\t{}\n'.format(customer.user_id, customer.name))

# If the script is being run instead of imported for testing,
# Execute the program
if __name__ == '__main__':
    import sys 

    # Collect the arguments of the program, if they have been passed.
    # Otherwise, assigns default values
    dst      = sys.argv[1] if len(sys.argv) > 1 else 100
    inp_file = sys.argv[2] if len(sys.argv) > 2 else 'customers.txt'
    out_file = sys.argv[3] if len(sys.argv) > 3 else 'output.txt'

    app = App()
    app.read_customers(inp_file)
    app.invite_near_customers(dst)
    app.write_invited(out_file)

