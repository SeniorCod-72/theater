"""
# Theater Audition System

This is a simple database system built using SQLAlchemy to manage theater auditions for various roles. It includes two primary models: `Role` and `Audition`, where each `Role` can have multiple auditions, and each `Audition` is associated with one `Role`.

## Features

- **Role Management**: Manage the roles for which auditions are held.
- **Audition Management**: Track auditions for specific roles, including actor names, audition locations, and hired status.
- **Actor Management**: Retrieve information about actors hired for roles, including lead and understudy actors.
- **SQLite Database**: Uses SQLite as a database backend.

## Models

### Role Model
The `Role` model represents a role in the theater production.

- `id`: The primary key of the role.
- `character_name`: Name of the character for the role.
- `auditions`: A one-to-many relationship with the `Audition` model.

#### Methods:
- `actors()`: Returns a list of actor names who have auditioned for this role.
- `locations()`: Returns a list of audition locations for this role.
- `lead()`: Returns the first actor hired for the role, or a message if no actor has been hired.
- `understudy()`: Returns the second actor hired for the role, or a message if no second actor has been hired.

### Audition Model
The `Audition` model represents an audition for a role.

- `id`: The primary key of the audition.
- `actor`: The name of the actor who auditioned.
- `location`: The location of the audition.
- `phone`: The actor's phone number.
- `hired`: Boolean flag indicating if the actor has been hired for the role.
- `role_id`: Foreign key linking this audition to a `Role`.

#### Methods:
- `call_back()`: Sets the `hired` status to `True` when an actor is hired for the role.

## Database Configuration

This project uses SQLite for the database, and the database file is named `theater.db`.

```python
engine = create_engine('sqlite:///theater.db')
Base.metadata.create_all(engine)

