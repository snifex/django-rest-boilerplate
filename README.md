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