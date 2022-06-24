# Using SQLAlchemy's Imperative style to separate data and domain layers

_(Imperative style was previously named Classic style)_

### Data
`database.py`

Each database table is defined with a `Table` object.

<img width="441" alt="image" src="https://user-images.githubusercontent.com/1622811/172561593-0fdc92d0-3862-4a5b-b357-49e354232bcd.png">

Tables can be queried directly using [SQLAlchemy's select function](https://docs.sqlalchemy.org/en/14/tutorial/data_select.html) 

### Domain Models
`domain.py`

Regular python classes containing business logic.

<img width="407" alt="image" src="https://user-images.githubusercontent.com/1622811/172561651-a175c7e8-12ad-430a-abd9-b48e4adf040f.png">


### Mapping
`orm.py`

The domain models are mapped to the respective `Table` using the `map_imperatively` register, enabling all the regular SQLAlchemy ORM features.

<img width="281" alt="image" src="https://user-images.githubusercontent.com/1622811/172561706-78a75689-cfdb-4904-9469-5a4a070c55cc.png">

All columns in the `Table` get automatically created as attributes of the mapped class when `map_imperatively` is called.

Relationships are configured with a dictionary of properties. The string representation of the class names can be used so there is no import dependency on either data or domain models.

<img width="496" alt="image" src="https://user-images.githubusercontent.com/1622811/172561797-7c559066-0f34-43df-95a1-ce293ed61d36.png">

As neither the data or domain models are dependent on the other, this pattern could be applied when using architectures that attempt to
separate the two.

Interestingly, the `__init__` method is called on mapped classes when objects are created on retrieval from the db.
When using the Declarative style, this does not happen and a method decorated with `@orm.reconstructor` is required for this behaviour.

### Advantages
* The database models are isolated from all business logic and can be kept thin
* Objects in the domain layer can be shaped to more closely represent the business model, rather than just the persisted view of it
* Models can be made more flexible and re-usable as they aren't subclasses of sqlalchemy models, only bound to them at runtime

### Disadvantages
* More typing as most fields will exist in both places
* Not as popular as the Declarative style so may seem unusual

### Further Reading

[SQLAlchemy mapping styles docs](https://docs.sqlalchemy.org/en/14/orm/mapping_styles.html#imperative-a-k-a-classical-mappings)

[Flask mapping docs](https://flask.palletsprojects.com/en/2.1.x/patterns/sqlalchemy/#manual-object-relational-mapping)

### Instructions
Only SQLAlchemy needs to be installed.

A SQLite db will be used by default.

Start an interactive session with `python -i orm.py`

Run tests with `python -m unittest`
