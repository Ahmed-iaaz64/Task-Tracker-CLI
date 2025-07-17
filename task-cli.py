import argparse
from task_tracker import TaskTracker

def conver_arg_to_int(string):
    try:
        return int(string)
    except ValueError:
        raise ValueError("argument must be an integer")

# Parse arguments provided in the command line
def parse_args():
    
    # Initialize parser
    parser = argparse.ArgumentParser()

    # Adding optional argument
    parser.add_argument("-a", "--Add", type=str, 
                        help = "Add a task to task list with a name")
    
    parser.add_argument("-u", "--Update", nargs=2, 
                        help = "Update existing task name with id")
    
    parser.add_argument("-d", "--Delete", type=str, 
                        help = "Delete existing task with id")
    
    parser.add_argument("-mark-in-progress", "--mark-in-progress", type=str,
                         help = "Mark a task as 'in-progress")
    
    parser.add_argument("-mark-done", "--mark-done", type=str,
                        help = "Mark a task as 'done")
    
    parser.add_argument("-mark-todo", "--mark-todo", type=str,
                        help = "Mark a task as 'todo")
    
    parser.add_argument("-l", "--List", nargs='?', type=str, const="all", default="all",
                        help = "List all tasks")
    
    return parser.parse_args()


def main():

    # Initialize task tracker
    tt = TaskTracker()

    args = parse_args()

    # Match the arg with the correct instruction
    if args.Add:
        tt.add_task(args.Add)

    elif args.Update:
        id = conver_arg_to_int(args.Update[0])
        tt.update_task(id, args.Update[1])

    elif args.Delete:
        id = conver_arg_to_int(args.Delete)
        tt.delete_task(id)   

    elif args.mark_in_progress:
        id = conver_arg_to_int(args.mark_in_progress)
        tt.mark_task_in_progess(id)

    elif args.mark_done:
        id = conver_arg_to_int(args.mark_done)
        tt.mark_task_done(id)

    elif args.mark_todo:
        id = conver_arg_to_int(args.mark_todo)
        tt.mark_task_todo(id)

    elif args.List:
        # If no arg is provided this is the default
        if args.List == "all":
            tasks = tt.get_all_tasks()
            print("All tasks: \n")
            for task in tasks:
                print(f"ID: {task["id"]}, Task: {task["name"]}\nStatus: {task["status"]}\n")
        
        # if args is provided print tasks with the matching status
        else:
            tasks = tt.get_tasks_by_status(args.List)
            print(f"{args.List.capitalize()} tasks: \n")
            for task in tasks:
                print(f"ID: {task["id"]}, Task: {task["name"]}\n")


if __name__ == "__main__":
    main()
