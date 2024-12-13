import random
import sys

def generate_data(length, filename="data.txt"):
    if int(length) < 1:
        sys.exit("Length cannot be less than 1.")
    data_file = open(filename, "w")
    result = ""
    for _ in range(0, int(length)):
        result += str(random.randrange(1, 10000, 1)) + "\n"
    result = result.rstrip()
    data_file.write(result)
    data_file.close()

if len(sys.argv) == 3:
    generate_data(sys.argv[1], sys.argv[2])
elif len(sys.argv) == 2:
    generate_data(sys.argv[1])
elif len(sys.argv) == 1:
    sys.exit("No length provided.")
else:
    sys.exit("Too many arguments provided.")
    