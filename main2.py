# YAO -- SKILLS TEST
from pyscript import display, document
import numpy as np  # np is just a common alias for numpy
import logging
logging.getLogger('matplotlib').setLevel(logging.ERROR) # removes the cache thingy
import matplotlib.pyplot as plt  # plt is just a common alias for matplotlib    
#preloadto avoid font cache message during user section
plt.figure()
plt.plot([0,1], [0,1])
plt.close()


absences = np.array([0, 0, 0, 0, 0])
days = np.array(["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"])

def attendancechecker(e):
    plt.clf()
    document.getElementById("output1").innerHTML = ""  # clear the output

    days_value = int(document.getElementById("day").value)
    absences_value = int(document.getElementById("absent").value)
    
    absences[days_value] += absences_value


    absence_tracker = plt.plot(days, absences, marker='o', color='pink')
    
    plt.show()
    plt.title("Weekly Attendance (Absences)")
    plt.xlabel("Days")
    plt.ylabel("Absences")