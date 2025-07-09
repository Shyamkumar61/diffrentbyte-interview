from sqlmodel import Field, Column, Integer, SQLModel, Text


class Employee(SQLModel, table=True):

    id : int = Field(primary_key=True)
    name : str = Field(nullable=False)
    email : str = Field(nullable=False)
    message : str = Field(nullable=False)
