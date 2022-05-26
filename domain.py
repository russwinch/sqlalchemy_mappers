class Base:
    """All columns and relationships in the Table object get automatically created as
    attributes on the mapped object when map_imperatively is called. They could be
    defined here to add any logic, or just for clarity and ease of use in testing.
    """
    id: str = None
    # created_at, updated_at etc, whatever


class User(Base):
    cool: bool = False  # doesn't exist in the Table, therefore won't be persisted
    addresses: ["Address"] = []

    def __init__(self, first_name: str, last_name: str) -> None:
        """If defined, __init__ is called when creating objects on retrieval from the
        db, unlike when using the declarative pattern, where a method decorated
        with @orm.reconstructor is required for this behaviour.
        """
        self.first_name = first_name
        self.last_name = last_name

    def make_cool(self):
        self.cool = True

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __repr__(self):
        return f"<User {self.id} {self.first_name}>"


class Address(Base):
    user_id: int = None
    email: str = None
    user: User = None

    def __init__(self, email: str) -> None:
        self.email = email

    def __repr__(self):
        return f"<Address {self.id} {self.email}>"
