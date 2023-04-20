from PairingHeap import PairingHeap 
from datetime import datetime
class Task():
    def __init__(self, weightage_=-1, date_=(0,0,0), personal_priority_=None, task_=""):
        self.date = datetime(date_[0], date_[1], date_[2])
        self.personal_priority = personal_priority_
        self.weightage = weightage_
        self.task = task_
        self.priority = self.priority_calculator()
       
    def priority_calculator(self):
        date = 4*((self.date-datetime.now()).days)
        weightage = 3*(self.weightage)
        personal = 2*(self.personal_priority)
        self.priority = ((date + weightage + personal) // 3)*-1
        return (self.priority)


p = PairingHeap()
task1= Task(10,(2023, 4, 21),10,"DO DS")
task2= Task(15,(2023, 4, 21),10,"LA")
p.Insert((task1.priority,task1.task))
print(p.Top())
p.Insert((task2.priority,task2.task))
print(p.Top())
        
