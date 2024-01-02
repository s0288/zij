# Give feedback.
Provide learning experiences to others.

For developers:

- run locally with 'python src/manage.py runserver'
- run docker file with (make sure you set up your own .env file):
  - docker build -t zij .
  - docker run -p 8000:8000 --env-file=.env zij
