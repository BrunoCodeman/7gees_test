Some points about the solution
===

- It was simplified as much as possible to achieve the objectives in the easiest possible way.
That's the reason why there's only one file for all models and the same for schema 
and everything else.

- SQLite3 was used because it's Django default engine and to not overengineer the test

- Django-graphene was used to not reinvent the wheel.

- Some good practices like validations, splitting things in packages/projects, 
environment configuration (nginx/apache, gunicorn, containerization, etc) 
where skipped so the code can be executed without rocket science