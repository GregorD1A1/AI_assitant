import datetime
from todoist_api_python.api import TodoistAPI
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


todoist_key = os.getenv('TODOIST_API_TOKEN')
api = TodoistAPI(todoist_key)

personal_project_id = 2302397862

def get_tasks_in_date_range(start_date, end_date):
    # Convert dates to datetime objects
    start_date = datetime.datetime.strptime(start_date, "%m/%d/%Y")
    end_date = datetime.datetime.strptime(end_date, "%m/%d/%Y")


    # Get all tasks
    tasks = api.get_tasks(project_id=personal_project_id)

    # Filter tasks based on date range
    tasks_in_date_range = [task.content for task in tasks if
                           task.due and start_date <= datetime.datetime.strptime(task.due.date, "%Y-%m-%d") <= end_date]

    return tasks_in_date_range


def edit_task(name, new_name=None, description=None, date=None):
    tasks = api.get_tasks(project_id=personal_project_id)

    task = [task for task in tasks if task.content == name][0]
    task_id = task.id

    response = task.update(task_id, content=new_name, description=description, due=date)

    return response