# Electronic Vignette Evidence backend
This SWI2 schools project aims to provide a simple backend to basic electronic vignettes management.
Frontend part can be found [here](https://git.pef.mendelu.cz/swi_ii/drajsajtl2).

## Running the application
You need to set environmental variable `EVE_CONF` with an absolute path to the configuration file.
You can find example configuration file in the `drajsajtl/config` directory.

Dependency management is done using [Poetry](https://python-poetry.org/).
To install dependencies use:
```bash
> poetry install --no-root
```
then, you can start the Django's dev server using:
```bash
> poetry run python manage.py runserver
```

### Running the tests
```bash
> poetry run pytest tests
```
Make sure your configuration file points to testing database.

### API Documentation
[Swagger](https://app.swaggerhub.com/apis/Jiri_Jerabek/Elektronicke-dalnicni-znamky/1.0.0#/)
