# Employee Data Deductions App

This app is used to showcase and edit tabular data live in an app with database used [Supabase](https://supabase.com/)  

## Usage 

First clone the repo locally.
```bash
git clone https://github.com/Laoode/dashbboard-reflex
```
Then set up a virtual environment as outlined in our documentation. After this run `pip install -r requirements.txt`.

First, create migration scripts based on the `rx.Model` definitions and update
the default sqlite database with that schema. This only needs to be done once
when a new app is created.

```bash
reflex db init
```

Then run the app with the following command:

```bash
reflex run
```

## Applying Database Schema Changes

If changes are made to the database models after initialization, they can be
applied by running the following commands:

```bash
reflex db makemigrations --message "Brief description of the change"
```

```bash
reflex db migrate
```

**Be sure to install the appropriate DB driver in your environment.** In the
*example above, that would be `pip install "psycopg[binary]"`.

After configuring a different database, execute `reflex db migrate` to populate
it with the latest schema before running the app.
