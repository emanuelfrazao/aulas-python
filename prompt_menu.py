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


def get_user_action():
    print()
    print('1 - Add task')
    print('2 - Remove task')
    print('3 - Display tasks')
    print('4 - Exit')

    user_input = input(': ')
    
    # If input is valid, return
    if user_input in ('1', '2', '3', '4'):
        return user_input
    
    # Otherwise ask for new input
    else:
        print('invalid input: choose number from 1 to 4')
        return get_user_action()
        
list_of_tasks = load_data()
while True:
    
    # Prompt the user for an action
    action = get_user_action()
    
    if action == '1': # Add task
        task_name = input('Task name: ')
        
        # If user input is not empty, create task and save it on list
        if task_name != '':
            task = Task(task_name)
            list_of_tasks.append(task)
        else:
            print('No task was added.')
        
    
    elif action == '2':
        # Remove task
        pass
    
    elif action == '3':
        # Display tasks
        print()
        for i, task in enumerate(list_of_tasks):
            print(f"{i+1} - {task}")
    
    elif action == '4': # Exit
        # Save and exit
        save_data(list_of_tasks)
        break