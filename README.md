# django-blog
python2.7 django1.8个人blog博客系统
win和MAC兼容，clone项目。修改settings下配置邮箱已经数据库
python manage.py makemigrations
python manage.py migrate
runserver
#android-rest Build Status

Demo Rest. Check out the project's documentation.
Prerequisites

    virtualenv
    postgresql
    redis
    travis cli
    heroku toolbelt

Initialize the project

Create and activate a virtualenv:

virtualenv env
source env/bin/activate

Install dependencies:

pip install -r requirements/local.txt

Create the database:

createdb androidrest

Initialize the git repository

git init
git remote add origin git@github.com:hernanramirez/android-rest.git

Migrate the database and create a superuser:

python androidrest/manage.py migrate
python androidrest/manage.py createsuperuser

Run the development server:

python androidrest/manage.py runserver

Create Servers

By default the included fabfile will setup three environments:

    dev -- The bleeding edge of development
    qa -- For quality assurance testing
    prod -- For the live application

Create these servers on Heroku with:

fab init

Automated Deployment

Deployment is handled via Travis. When builds pass Travis will automatically deploy that branch to Heroku. Enable this with:

travis encrypt $(heroku auth:token) --add deploy.api_key

