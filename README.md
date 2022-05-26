# Using SQLAlchemy's Imperative style to separate data and domain layers

_(Imperative style was previously named Classic style)_

[SQLAlchemy mapping styles docs](https://docs.sqlalchemy.org/en/14/orm/mapping_styles.html#imperative-a-k-a-classical-mappings)

[Flask mapping docs](https://flask.palletsprojects.com/en/2.1.x/patterns/sqlalchemy/#manual-object-relational-mapping)

### Data
Each database table is defined with a `Table` object.

As the table definitons are compact, a reasonable number of tables can likely be defined in the same a module.

### Domain Models
Regular python classes are created and then mapped to the respective `Table`s using the `map_imperatively` register.
All columns in the `Table` get automatically created as attributes of the mapped class when `map_imperatively` is called.

Relationships are configured with a dictionary of properties.

Business logic can now be integrated into these objects while keeping the data layer thin.
As neither of the models is dependent on the other this approach is applicable to any architecture that attempts to
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
