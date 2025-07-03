# Changes on models

We set on the bash console of the docker with

```bash
docker exec -it Django /bin/bash
```

Then we execute the following commands


```bash
python manage.py makemigrations
python manage.py migrate
```

## Environment Variables

Copy the `.env.example` file to `.env` and fill in the actual values:

```bash
cp .env.example .env
```

## Creation of apps

First of all we need to create a bash console

```bash
docker exec -it Django /bin/bash
```

Then we need to move on apps

```bash
cd apps
```

Once there we create an app, you can name it as you wish

```bash
python ../manage.py startapp {nameoftheapp}
```

When the app be created we need to enter into the `apps.py` file of the app and on the name of the app we will change to:

```bash
apps.{name of the app}
```

For example

```bash
apps.blog
```

Then we need to add it onto the `settings.py` on the `PROJECT_APPS` we put the same name that we put onto the `apps.py`

```bash
PROJECT_APPS = [
    'apps.blog'
]
```
