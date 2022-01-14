"""
Create a table schema from the log_input.in file. The file shows different machines running different processes.
and their respective start or stop time. The final result shows a dictionary indicating the total time each process
did run.
"""
schema = []
my_dict = {}

# open the log file and parse it into a list

with open('log_input.in') as file:
    for row in file:
        schema.append(row.split())

    for row in schema:
        # identifier to narrow down a machine-process combination
        key = (row[0], row[1])
        # start of the process
        if row[2] == 'start':
            # in case machine-process combination does already exist the time is deducted
            if key in my_dict.keys():
                my_dict[key] += -(float(row[3]))
            # creates a tuple in the dict and adds the negative time for the start process
            else:
                my_dict[key] = -(float(row[3]))
        # adds the end time per machine-process combination to the dict
        if row[2] == 'end':
            my_dict[key] += float(row[3])

print(my_dict)
