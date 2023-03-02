# INSTRUCTIONS TO RUN IN WINDOWS

1. Make sure you have python 3.10
2. Run the following command in cmd.
```
python -m venv venv
```
3. Activate the virtual env
```
venv\Scripts\activate.bat
```
4. Install the packages
```
pip install -r requirements\dev.txt
```
5. Migrate the migrations
```
python manage.py migrate
```
6. Create super user
```
python manage.py createsuperuser
``` 
7. Web access for admin users
```
http:127.0.0.1:8000/admin
``` 
8. API REST
```
http://127.0.0.1:8000
``` 