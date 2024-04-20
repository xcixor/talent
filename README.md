# talent

## Preriquistes

## Preriquistes
Please ensure that you have the following installed:

- [python 3+](https://www.python.org/downloads/)
- [pip](https://pip.pypa.io/en/stable/installing/)
- [virtualenv or any other environment manager](https://virtualenv.pypa.io/en/stable/)
- [PostgreSQL](https://www.postgresql.org/download/) (for Ubuntu, run `sudo apt-get update` and then `sudo apt-get install postgresql postgresql-contrib`)
- [python 3+](https://www.python.org/downloads/)
- [pip](https://pip.pypa.io/en/stable/installing/)
- [virtualenv or any other environment manager](https://virtualenv.pypa.io/en/stable/)

## Setup
- Clone the repository on your machine
    ```
    git clone https://github.com/xcixor/talent.git
    ```
## Development and Testing

- Change directory into the repository
    ```
    cd talent
    ```
- Install packages.
    ```
    pip install -r requirements.txt
    ```
- Create a database. To create a postgres db for this app, please do the following;
- Switch to postgres: ```sudo su postgres```. You will be prompted to provide your root password.
    - Open psql terminal: ```psql```
    - Create the database: ```CREATE DATABASE <your db name>```
    - Create a user with password: ```CREATE USER <username> WITH PASSWORD "<the password>"```. NB. The password should be in quotation marks.
    - Enable the user to create databases: ```ALTER ROLE <username> CREATEDB```
    - Giving them access to public schema: ```GRANT USAGE ON SCHEMA public TO username```
    - Give the user all privileges to the database: ```GRANT ALL PRIVILEGES ON DATABASE <your db name> TO <username>```
    - Making them the owner of the database: ```ALTER DATABASE <your db name> OWNER TO <username>```

- Switch back to your root folder and migrate the db.
    ```
    python manage.py migrate
    ```
- Create an admin.
    ```
    python manage.py createsuperuser
    ```

- Start up the development environment for the talent app.
    ```
    python manage.py runserver
    ```
- Proceed to the URL http://localhost:8000 to see your application on the browser

### Fixtures
To run a fixture on your database you need to follow the steps below:

1. Ensure that you have created the necessary migrations for the tables.
2. Ensure that you have run the migrations created on the first step on the database.
3. Finally run the command below for the respective fixture you would like to add to the database.

    ```python manage.py loaddata <fixtures file path>```

    For example:

    ```python manage.py loaddata product_categories/product_categories.json```


### Notes on testing and developing
- Always create a new branch for new features and always create it from the develop branch. To do this, first check which branch you are on with the command: ```git status```. The first line of the text printed should read **On branch develop**
- Next, create the branch with: ```git checkout -b new-branch-name```. *new-branch-name* is the name of the branch you intend to make your changes on.
- Always test you app. Use [TDD](https://technologyconversations.com/2013/12/20/test-driven-development-tdd-example-walkthrough/#:~:text=Test%2Ddriven%20development%20(TDD),to%20pass%20that%20test%2C%20and) practices to ensure you create a rigorously tested and maintainable app. You can read through the tests folder to see how some tests are written. Its a broad topic and one everybody should invest in.
- Proceed to make your changes and additions to the files to make the tests pass.
- Ensure you tests are passing and all other tests have not been affected. To run tests, run the command ```make test```
- When you are done coding, stage the changes (tell git yo want to record this changes, its like saving but to git). Use the following command to stage: ```git add .```
- Save your changes to the local repository with the command ```git commit -m "message indicating what you have done"```.
- Publish your changes remotely with the command ```git push origin new-branch-name```
- Create a pull request against main (Just click the create pull request button on github it should create against main automatically).
- Send the pr link to your team for review.
- Once the review is done, merging will be done remotely (on github) and the branch deleted.

N:B
- never commit to main locally
- Never merge locally
- if your branch is behind main (if i have merged something remotely while you were working) use git rebase main to update your branch
- Only changes made under the **talent** directory will be rendered on the browser.

### NBs
- In case new packages are installed into the application, i.e. a change in the `Pipfile` and `Pipfile.lock` files, then all you need to do is to re-run the `make dev` command to rebuild and start up the dev environment. This will re-trigger a build on the docker image, that will install the packages.
- In case you would like to delete the dev environment, run the `make tear-dev` command. This will stop and remove containers that were created for your application. This means that your Postgres Docker container will lose all data that you added on to it.
