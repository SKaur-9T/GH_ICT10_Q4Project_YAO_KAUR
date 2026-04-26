#KAUR -- SEATWORK 2 
from pyscript import document, display

class Classmate:
    def __init__(self, name, section, favorite_subject):
        self.name = name
        self.section = section
        self.favorite_subject = favorite_subject

    def introduce(self):
        return "Hi! I am " + self.name + " from " + self.section + ". My favorite subject is " + self.favorite_subject + "."


classmates = [
    Classmate("Leona", "Topaz", "PE"),
    Classmate("Phoebe", "Topaz", "English"),
    Classmate("Harmony", "Topaz", "Music"),
    Classmate("Calvin", "Topaz", "Math"),
    Classmate("Sean", "Topaz", "PE"),
    Classmate("Skyler", "Topaz", "TLE")
]


def add_classmate(event):
    name = document.getElementById("name").value
    section = document.getElementById("section").value
    subject = document.getElementById("subject").value

    new_classmate = Classmate(name, section, subject)
    classmates.append(new_classmate)

    document.getElementById("output").innerHTML = "Successful added!"


def show_list(event):
    output = document.getElementById("output")
    output.innerHTML = ""

    for c in classmates:
        display(c.introduce(), target="output")
