# import tkinter as tk
# from tkinter import messagebox
# import json
# import datetime

# # Global Variable so these variable can be accessable in every function
# tasks=[]
# filename="tasks.json"

# def load_task():
#     global tasks
#     try:
#         with open(filename,"r") as f:
#             tasks=json.load(f)
#     except:
#         tasks=[]

# def save_tasks():
#     with open(filename,"w") as f:
#         json.dump(tasks,f,indent=4)
#     messagebox.showinfo("Saved","Tasks saved successfully!")


# #Adding new task , Lets go

# def add_task():
#     title=title_entry.get()
#     category=category_entry.get()
#     deadline=deadline_entry.get()

#     if not title or not category or not deadline:
#         messagebox.showerror("Missing Info.All filed required!")
#         return
#     tasks.append({"title":title,"category":category,"deadline":deadline,"done":False})
#     update_task_list()
#     title.entry.delete(0,tk.END)
#     category.entry.delete(0,tk.END)
#     deadline.entry.delete(0,tk.END)

# #Update displayed task list
# def update_task_list():
#     task_list.delete(0,tk.END)
#     for t in tasks:
#         status="✅" if t["done"] else "❌"
#         task_list.insert(tk.END,f"{t['title']} | {t['category']} | {t['deadline']} | {status}")

# #Mark selected task as done

# def mark_done():
#     selcted=task_list.curselection()
#     if selcted:
#         index=selcted[0]
#         task[index]['done']=True
#         update_task_list()

# #view Tasks by category

# def filter_by_category():
#     cat=category_filter.get()
#     task_list.class ModelNameDetail(DetailView):
#         model = ModelName
#         template_name=''
