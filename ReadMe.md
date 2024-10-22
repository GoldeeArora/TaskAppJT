# TaskApp

## Setup
- Unzip the folder and move into the codebase root directory
- Create virtual environment: `python -m virtualenv venv`
- Enable virtual environment: Windows - `venv\Scripts\activate`, Linux/Unix - `source venv\bin\activate`
- Run `pip install -r requirements.txt`
- Run `python manage.py runserver`
- Superuser credentials: username - admin, password - admin

## APIs Testing

#### 1. Create Task
- Navigate to http://localhost:8000/tasks/create/ in browser
- Enter Name and Description of task
- Press POST button
- Note down the returned id 

#### 1. Assign Task
`Currently there are only two users with ids 1 and 2 in the database. More can be added via the admin panel or createsuperuser command.`
- Navigate to http://localhost:8000/tasks/[id]/assign/. (Enter a task id here)
- Switch to the raw_data tab in the browsable api
- Remove the prefilled json and add the following: `{"user_ids": [1, 2]}`
- You can choose the users you wish to add
- Note: Task's other fields can be modified using this api as well
- Press PATCH

#### 1. View User's Tasks
- Navigate to http://localhost:8000/users/[id]/tasks/. (Enter a user id here)
- Details of each tasks assigned to this user including the other user's each task is assigned to is visible