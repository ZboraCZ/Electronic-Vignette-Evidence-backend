# Electronic Vignette Evidence backend
This is Software Engineering II schools subject project that aims to provide a simple backend to basic electronic vignettes management.

Frontend part can be found [here](https://github.com/ZboraCZ/Electronic-Vignette-Evidence-frontend).

## Application setup
- Dependency management of project is done using [Poetry](https://python-poetry.org/). 
So install this dependency manager first to get project management going.
- Then set up environmental variable in your system named `EVE_CONF` with an absolute path to the configuration file.
Config file is located at `config/example.env` in this project. 
  If you can't set this path, just copy the whole file and place it somewhere the env variable can be set.
  This file contains PostgreSQL DB information that you will need to connect to it.
- To install dependencies use in project root dir:
```bash
> poetry install --no-root
```
- Install [PostgreSQL database server](https://www.postgresql.org/).
In the installation process, setup things according to config file (It should be default values as it was when this project was made).
- In PostgreSQL create Database named `eve` with nothing inside it. Leave postgres user as owner. It's because Django can't create DB on its own in migrations.
- Run migrations in the root of project from command terminal with `$ python manage.py migrate`. 
  Make sure you have PostgreSQL running( and postgres user logged in if necessary). You can manage using pgAdmin GUI.

## Running the application
Start the Django's dev server using:
```bash
> poetry run python manage.py runserver
```
The default start page is Swagger Documentation so you can see where you can go :)
#### After this you can move forward to [Running frontend Application](https://github.com/ZboraCZ/Electronic-Vignette-Evidence-frontend) 

### Running the tests
```bash
> poetry run pytest tests
```
Make sure your configuration file points to testing database.

## Swagger API Documentation
### [http://127.0.0.1:8000/api/schema/swagger-ui/](http://127.0.0.1:8000/api/schema/swagger-ui/)
