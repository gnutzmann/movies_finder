# movies_finder

1. GET SOURCE

   > _git clone https://github.com/gnutzmann/movies_finder.git_

2. CREATE ENVIRONMENT

   > _cd movies_finder/backend/_

   > _python -m venv env_

3. ACCESS ENVIRONMENT

   > _source env/bin/activate_

   PS.: the command to deactivate is 'deactivate'

   > export FLASK_APP=movies_finder

   > export FLASK_ENV=development

4. INSTALL REQUIREMENTS

   > _pip install -r requirements.txt_

5. BUILD AND RUN AN IMAGE AS A CONTAINER

   > _cd movies_finder/docker/_

   > _sudo docker-compose up -d_

6. IMPORT DATA TO MONGODB

   > _cd movies_finder/app/util/_

   > _python import_movies_

7. To run app

   > _flask run_
