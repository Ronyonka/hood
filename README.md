# Hood
#### Date of Current Version (March 25th,2019)
#### By **Ron Onyonka**
## Description
If you are like me, You really don’t know what is happening in your neighborhood most of the time. What if an important meeting happens, theft or even death wouldn’t you like to know about it. Hood is a web app that allows users to keep up to date with what is happening in their neighberhoods.



## Behaviour Driven Development
| Behaviour     | Input     | Output  |
| ------------- |:-------------:| -----:|
| User signup | User enters credentials | Redirected to a page where they can edit their profile|
| Home page | - | - |
| View Businesses | Users click on view business| Redirected to pages with businesses from that specific neighborhood |
| Viewing Annoncements | Click View Announcements| Redirected to a page with Announcements from  |
| Search Business | Enter search term in the search bar | User redirected to page with businesses containing the search term |

## Link to Live Website 
Here is a link to the live website: <https://ronhood.herokuapp.com/>


### Technologies Used

- HTML
- CSS
- django-Bootstrap4
- Python3.6
- Heroku
- Django

## Setup/Installation Requirements


### Prerequisites
You need the following to work on the project: -
* Python version 3.6 
* Pip 
* venv 
* A text Editor(vscode preferably)
* git

### Clone the repo and check into the project folder

- `git clone https://github.com/Ronyonka/hood`
- `cd hood`

### Create and activate the virtual environment

- `$ python3.6 -m venv virtual`
- `$ source virtual/bin/activate`


### Install the dependencies found in the  requirements.txt file

```bash
(virtual)$ pip install -r requirements.txt
```

### Create a database

```bash
(virtual)$ psql
    user=# CREATE DATABASE hood;
```


### Create a .env file and in it input the following:

```bash
SECRET_KEY=''
DEBUG=True #Set To False in Production
DB_NAME='hood'
DB_USER='user'
DB_PASSWORD='password'
DB_HOST='127.0.0.1'
MODE='dev' #set to prod in production
ALLOWED_HOSTS=['*']
DISABLE_COLLECTSTATIC=1
```


### Make migrations


- `(virtual)$ python3.6 manage.py makemigrations app`
- `(virtual)$ pytohon3.6 manage.py migrate`


### Run `manage.py` in the terminal

```bash
(virtual)$ python3.6 manage.py runserver
```

## Known Bugs
None at the moment.

## License
MIT License

Copyright (c) 2019 Ron Onyonka

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sub-license, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NON-INFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.