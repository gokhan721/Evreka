# Evreka
Navigation Folder(Part-One)

- Getting navigation record data that is sent by vehicles in last 48 hours.

How to Run:

- create virtual env or conda env and activate it.
- Install necessary packages with "pip install -r req.txt" command.
- Go to "manage.py" directory.
- Migrate data with "python manage.py migrate".
- Populate it to db with "python manage.py makemigrations"
- To be ensure run one more time "python manage.py migrate"
- Run server with "python manage.py runserver"
- Server start at "localhost:8000"

- Optional:
  - If you wanna add data to db you can use admin panel.
  - First create super user "python manage.py create superuser"
  - Go to webpage "localhost:8000/admin"
  - enter username passw.
  - First add vehicle data, then add navigation records due to foreign key.


Suggestions:

- Suggestions are placed in "suggestions.txt" into navigation folder.


Database_Model Folder(Part-two)

- Entity-diagram and function in this folder.
