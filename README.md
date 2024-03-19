# gloify
## Running Django
python manage.py runserver

### Bind with port
python manage.py runserver 0.0.0.0:8000

#### Install Dependencies
Before running Django, make sure to install the required dependencies using pip:

pip install -r requirements.txt

##### Start celery
Before using this command make sure redis or your message broker is running

celery -A gloify worker --loglevel=info --logfile=celery.log

###### Start celery beat

celery -A gloify beat --loglevel=info --logfile=beat.log