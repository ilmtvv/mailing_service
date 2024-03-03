<h1 align="center">SPAM</h1>
<h5 align="center">PACKAGES</h5>

- python = "^3.10"
- Django = "4.2"
- psycopg2-binary = "^2.9.9"
- uuid = "^1.30"
- crispy-bootstrap5 = "^2023.10"
- django-crispy-forms = "^2.1"
- python-dotenv = "^1.0.1"
- ipython = "^8.21.0"
- python-crontab = "^3.0.0"
- pillow = "^10.2.0"
- redis = "^5.0.2"

<h5 align="center">CREATE .env</h5>

[EXAMPLE](https://github.com/ilmtvv/mailing_service/blob/develop/sample_env)

<h5 align="center">CREATE MANAGERS</h5>

- [GROUPS]
- COMMAND [create_managers]

<h5 align="center">COMMAND FOR MAILING IN DJANGO SHELL</h5>
python manage.py pre_mailing --pk_mailing=int:pk

<h1 align="center">SCREENSHOTS</h1>
<p align="center"><img width="720px" src="screenshots/Screenshot 2024-03-04 at 01-11-43 spam.png"/></p>
<p align="center"><img width="720px" src="screenshots/Screenshot 2024-03-04 at 01-12-58 spam.png"/></p>
<p align="center"><img width="720px" src="screenshots/Screenshot 2024-03-04 at 01-28-29 spam.png"/></p>
<p align="center"><img width="720px" src="screenshots/Screenshot 2024-03-04 at 01-28-36 spam.png"/></p>
<p align="center"><img width="720px" src="screenshots/Screenshot 2024-03-04 at 01-28-49 spam.png"/></p>
<p align="center"><img width="720px" src="screenshots/Screenshot 2024-03-04 at 01-29-39 spam.png"/></p>

- if object.mailing_status == 0 CREATED
- if object.mailing_status == 1 ACTIVATING
- if object.mailing_status == 2 STOP
- if object.mailing_status == -1 SUCCESS
