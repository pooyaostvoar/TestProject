
## 🔧 **Alembic and Migrations**

### When Changing Models

Whenever you make changes to your models, you need to generate new migration files and apply them to the database. This can be done using **Alembic**.

#### Steps to Follow:

1. **Make Changes to Your Models:**
   Update or create new models in the `app/models/` folder. For example, adding a new field or modifying an existing one.

2. **Generate a New Migration:**
   After modifying the models, generate a new Alembic migration file using the following command:

   ```bash
   alembic revision --autogenerate -m "Your migration name"
   ```

   - This will automatically compare your models with the current database schema and create a new migration file inside the `alembic/versions/` folder.
   - Make sure to give a meaningful message to describe the migration.

3. **Review the Generated Migration File:**
   Alembic will generate a migration file that attempts to alter the schema based on your model changes. Open the generated file and review the changes in the `upgrade()` and `downgrade()` functions. If any changes are incorrect, adjust them manually.

4. **Apply the Migration:**
   Once you’re happy with the migration file, apply it to your SQLite database (for local development) by running:

   ```bash
   alembic upgrade head
   ```

   This will apply the migration to your local SQLite database.


### **Development Database - SQLite**

Currently, the development environment uses **SQLite** for testing and development. All migrations are applied to this SQLite database. You can find it in the project's root directory as `./tests.db`.

- This is a simple local database used to quickly apply and test migrations.
- In production, you can switch to a more robust database like PostgreSQL by modifying the `DATABASE_URL` in the `.env` file or your Docker configuration and also change `sqlalchemy.url` in `alembic.ini`.

#### Checking the SQLite Database

To inspect the current state of the database and see which tables exist, you can use SQLite commands. First, start the SQLite CLI:

```bash
sqlite3 ./tests.db
```

Then, you can run commands like:

```sql
.tables  -- List all tables
```

This can be helpful when you want to verify that the migration was successful.

---

### **Important Notes for Migrations**

- **Local Development:** All migrations are applied to the SQLite database (`tests.db`).
- **Production Database:** When deploying to production (e.g., PostgreSQL), ensure that your database URL (`DATABASE_URL`) is correctly set in the `.env` file.
  