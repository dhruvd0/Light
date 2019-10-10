userId=input("enter id")
userPass=input("enter password")

di1 = {"username": userId, "password": userPass}
import numpy as np

# Save
np.save('my_file.npy', di1) 

# Load
read_dictionary = np.load('my_file.npy').item()
print(read_dictionary)