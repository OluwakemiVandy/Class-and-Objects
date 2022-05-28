class Student:
    def __init__(self, name:str, age:int, tracks:list, score:float):
       self.name=str(name)
       self.age= int(age)
       self.track=list(tracks)
       self.score=float(score)
     


    def change_name(self,change_name):
       self.change_name= change_name
       print("The student name is", self.change_name )

    def change_age(self,new_age):
       self.age=new_age
       print("The student age is", self.age)

    def add_tracks(self,track):
       self.track.append(track)
       print("The student track is", self.track)

    def get_score(self):   
        print("Bob scored",self.score)

   
Bob=Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)
    

Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_tracks("UI/UX")
Bob.get_score()
