from sqlalchemy import create_engine

engine = create_engine('sqlite:///new_todo_test.db')
print(engine)
