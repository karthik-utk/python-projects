def add(task_i):
    task_i["title"] = input('Enter the name of task: ')
    task_i["text"] = input('Enter the task details: ')
    task_i["status"] = int(input('Enter the task status(1/0): '))
    task_i["date"] = input('Enter the date of the task (dd/mm/yy): ')

    l.append(task_i)

def delete():
    c = int(input('Which task you want to delete: '))
    del l[c - 1]
    print('Task deleted.')

def view(a):
    print(f'There are total {a} tasks.')
    i = 0
    
    while i < len(l):
        print(f'Task - {i + 1}:\n{"[x]" if l[i]["status"] else "[]"} --- {l[i]["title"]}: \n Task date: {l[i]["date"]} \n Task:\n{l[i]["text"]}')
        i += 1

    done = sum(1 for t in l if t["status"])
    pending = i - done
    print(f'Total Tasks : {i} | Done: {done} | Pending: {pending}')

def modify_task():
    c = int(input("Which task's status you want to modify: "))
    l[c - 1]["status"] = 1 - l[c - 1]["status"]
    print('Task status updated')

    
choice = 'y'
l = []

try:
    with open("tasks.txt","r") as f:
        for line in f:
            words = line.strip().split('||')
            l.append({"title":words[0],"text":words[1],"status": 0 if words[2] == 'Pending' else 1,"date":words[3]})
except:
    l = []

i = len(l)

while(choice != 'n'):

    print('Welcome to Todo')
    print(f'Total Tasks : {i}')
    print('Choose a Option: ')
    c = int(input('1.Add a task\n2.Delete a task\n3.View a task\n4.Update status\n'))

    match c:
        case 1:
            i += 1
            task = dict()
            add(task)
        case 2:
            i -= 1
            delete()
        case 3:
            view(i)
        case 4:
            modify_task()

    choice = input('Do you want to continue(y/n): ')
else:
    print('To-do application closed')
    with open("tasks.txt","w") as f:
        for j in l:
            f.write(f'{j["title"]}||{j["text"]}||{"Finished" if j["status"] else "Pending"}||{j["date"]}' + '\n')

    