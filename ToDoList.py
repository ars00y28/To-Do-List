
class task: # blue print for each task 
    def __init__(self,title:str):
        self.__title = title
        self.__CompleteStatus = False
        self.__description = ''
    @property 
    def title(self): #  returns title of the task 
        return self.__title
    
    @title.setter
    def title(self,NewTitle): # changes title of the task 
        self.__title = NewTitle
    
    @property
    def complete(self): # if the task is complete or not 
        return self.__CompleteStatus
    
    @complete.setter # change the complete status 
    def complete(self,NewCompleteStatus):
        self.__CompleteStatus = NewCompleteStatus
    
    @property # description of each individual task 
    def description(self):
        return self.__description
    
    @description.setter # change description 
    def description(self,NewDescription):
        self.__description = NewDescription


    def __repr__(self) -> str:
        return f"Title: {self.__title} \n Description: {self.__description} \n Complete status: {self.__CompleteStatus} \n"


class ToDoList: # blue print of the whole List
    def __init__(self):
        self.__ToDoList = [] # array that stores all the tasks in the list 
    @property
    def ToDoList(self):
        return self.__ToDoList

    def CreateItem(self,title): # creaeting an task  using the 'task' class
        TempItem = task(title)
        self.__ToDoList.append(TempItem)
        return TempItem
    
    def RemoveItem(self,RemoveTitle): #removes an item from the list by the task title 
        y = 0 
        remove = False
        for i in self.__ToDoList: # 
            if i.title == RemoveTitle:
                self.__ToDoList.pop(y)
                remove = True
            y = y + 1
        return remove

    @property
    def GetCompletedTask(self): # returns all the completed tasks 
        CompletedTask = []
        for i in self.__ToDoList:
            if i.complete == True:
                CompletedTask.append(i)
        return CompletedTask

    @property
    def GetIncompletedTask(self): # returns all the incomplete tasks
        IncompletedTask = []
        for i in self.__ToDoList:
            if i.complete == False:
                IncompletedTask.append(i)
        return IncompletedTask


    def __repr__(self) -> str:
        return f"To do list: {self.__ToDoList}"

NewList = ToDoList()

while True:
    UserAddItem = input('Do you want to add an item ? y/n: ').strip()
    if UserAddItem != 'n':
        TempItemTitle = input("Enter task title: ").strip()
        TempItem = NewList.CreateItem(TempItemTitle)
        WantDescription = input('Do you want to add Description? y/n: ').strip()
        if WantDescription != 'n':
            TempDescription = input("Description: ").strip()
            TempItem.description = TempDescription
    else:
        print()
        print(NewList)
        break
'''
main program is asking you to add tasks, its descriptions, if any of the tasks are completd or not and
if you want to delete any of the tasks or not. and at the end prints the tasks completed tasks and incompleted tasks.
The objects in this file can be used to create an to-do-list app using different librabry like tkinter. For now 
i have just created a sample of what it can do using the main program. 
'''

while True:
    UserWantChangeStatus = input('Have you completed any of the task ? y/n: ').strip()
    if UserWantChangeStatus != 'n':
        TempCompletedItem = input('Title of the task you have completed: ')
        for i in NewList.ToDoList:
            if i.title == TempCompletedItem:
                i.complete = True
    else:
        UserWantDelete = input('Do you want to delete any task? y/n: ').strip()
        if UserWantDelete !='n':
            TempDeleteItem = input('Title of the task that you want to delete: ')
            NewList.RemoveItem(TempDeleteItem)
        else:
            print()
            print(NewList)
            print()
            print('Completed tasks')
            print(NewList.GetCompletedTask)
            print()
            print("Incompleted tasks")
            print(NewList.GetIncompletedTask)
            break