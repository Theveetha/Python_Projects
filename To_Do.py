'''
# Step 1
print("Please enter a To Do Task : ")
Task = input()
print("Today's Tasks are")
print(Task)
print("********************")
user_prompt = "Enter a todo : "
text = input(user_prompt)
print(text)
print("********************")

# Step 2
user_prompt = ("Enter a todo : ")
todo1 = input(user_prompt)
todo2 = input(user_prompt)
todo3 = input(user_prompt)
# print(todo1)
# print(todo2)
# print(todo3)
todos = [todo1, todo2, todo3]
print(todos)
print(type(todos))
'''


n = int(input("Please enter number of tasks to add : "))
todos = []
for i in range(0,n):
    user_prompt = input("Enter a ToDo : ")
    todos.append(user_prompt)
print("To Do List : ")
for i in range(0,len(todos)):
    print(f"{i+1} -> {todos[i]}")
