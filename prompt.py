from datetime import datetime
import pickle

class Task:

    def __init__(self, name):
        # Set input attributes
        self.name = name # analogo a dizer: grava directamente o que receberes (com o mesmo nome do argumento)
        
        # Set time of creation as attribute
        self.time = str(datetime.now())[:16] # actual time as a string

    def __str__(self):
        return f"{self.name}, {self.time}"
    
###########################################

def save_data(tasks: list[Task]):
    """
    saves the list of tasks into a file
    """

    with open('todo.pickle', 'wb') as handle:
        pickle.dump(tasks, handle, protocol=pickle.HIGHEST_PROTOCOL)

def load_data():
    """
    reads the file 'todo.pickle' and returns the list of tasks
    if the file does not exists returns an empty list
    """

    try:
        with open('todo.pickle', 'rb') as handle:
            return pickle.load(handle)
    except:
        return []

##### User-interface
list_of_tasks = []
for _ in range(30000):
    

    task_name = input('Enter a task: ')
    # If user input is not empty, create task and save it on list
    if task_name != '':
        task = Task(task_name)
        list_of_tasks.append(task)   
    
    # Otherwise (if it's empty), display tasks and break
    else:
        print('Your tasks are:')
        for task in list_of_tasks:
            print(task)
        break