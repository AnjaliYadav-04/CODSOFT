import tkinter
import tkinter.messagebox
import pickle

#for main window
window=tkinter.Tk()
window.title("My To do list")

#function for adding tasks
def adding_task():
    todo=task_add.get()
    if todo != "":
        tdo_box.insert(tkinter.END,todo)
        task_add.delete(0,tkinter.END)
    else:
        tkinter.messagebox.showwarning(title="Alert !!",message="for adding task,Please enter some Task")

#function for deleting tasks
def task_delete():
    try:
        todo_index=tdo_box.curselection()[0]
        tdo_box.delete(todo_index)
        task_add.delete(0,tkinter.END)
    except IndexError:
        tkinter.messagebox.showwarning(title="Alert !!",message="For Deleting Task you need to select a task")

#function for loading takss
def loading_task():
    try:
        todo_lst=pickle.load(open("tasks.dat","rb") )
        tdo_box.delete(0,tkinter.END)
        for todo in todo_lst: 
            tdo_box.insert(tkinter.END,todo)
    except:
        tkinter.messagebox.showwarning(title="Alert !!",message="Cannot find task.dat ")        

#function for saving the tasks
def saving_task():
  try:  
    todo_list=tdo_box.get(0,tdo_box.size())
    pickle.dump(todo_list,open("tasks.dat","wb"))
  except :
      tkinter.messagebox.showwarning(title="Alert !!", message="error for saving tasks")  


#function for updating tasks
def updating_task():
   try:
       tdo_index=tdo_box.curselection()[0]
       update_task=task_edited.get()
       if update_task !="":
           tdo_box.delete(tdo_index)
           tdo_box.insert(tdo_index,update_task)
           task_edited.delete(0,tkinter.END)
       else:
           tkinter.messagebox.showwarning(title="Alert !!",message="for updating task,Please Enter some text.")    
   except:
       tkinter.messagebox.showwarning(title="Alert !!",message="for updating the task, please select the task first")
       
lst_frame=tkinter.Frame(window)
lst_frame.pack()
tdo_box=tkinter.Listbox(lst_frame,height=30,width=60)
tdo_box.pack(side=tkinter.LEFT)
#creating scroolar which are generally in RIGHT side
scroll_bar=tkinter.Scrollbar(lst_frame)
scroll_bar.pack(side=tkinter.RIGHT,fill=tkinter.Y)

# creating box for tasks need to be perform
tdo_box.config(yscrollcommand=scroll_bar.set)
#scroll_bar.config(command=lst_frame.yview)

task_add=tkinter.Entry(window,width=80)
task_add.pack()

task_edited=tkinter.Entry(window,width=80)
task_edited.pack()

#task button for adding task
task_button1=tkinter.Button(window,text="For Adding Your Task Click here",font=("arial",18,"bold"),background="blue",width=35,command=adding_task)
task_button1.pack()

#Task button for Deleting task
task_button2=tkinter.Button(window,text="For Deleting Your Task Click here",font=("arial",18,"bold"),background="Yellow",width=35,command=task_delete)
task_button2.pack()

load_task_button=tkinter.Button(window,text="Click Here to load the tasks",font=("arial",18,"bold"),background="purple",width=35,command=loading_task)
load_task_button.pack()

#save particular task for me we can created
save_task_button=tkinter.Button(window,text="Click Here to Save the tasks",font=("arial",18,"bold"),background="skyblue",width=35,command=saving_task)
save_task_button.pack()

update_task_button=tkinter.Button(window,text="Click here to update your tasks",font=("arial",18,"bold"),background="green",width=35,command=updating_task)
update_task_button.pack()





window.mainloop()