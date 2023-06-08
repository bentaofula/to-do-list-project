# from models import Category, User, Task
# from database import session

# def generate_seeds():


#  user1 = User(first_name="Ree", last_name="Dee")
# user2 = User(first_name="May", last_name="She")
# user = session.query(User).filter_by(id=1).first()
# # full_name = user1.full_name()
# # print(full_name)

# user1 = User(first_name='Ree', last_name='Dee')
# user2 = User(first_name='May', last_name='She')

# category1 = Category(name='Category S')
# category2 = Category(name='Category Q')

# task1 = Task(star_rating=0.1)
# task1.user = user1
# task1.category = category1

# task2 = Task(star_rating=2.2)
# task2.user = user2
# task2.category = category2

# # Accessing the full task information
# print(task1.full_task())  
# print(task2.full_task())
# # Create an instance of Category
# category1 = Category(name="Category S", price=50.0, star_rating=0.1)
# print(category1.all_tasks())

# # Add the category instance to the session
# session.add(category1)
# session.commit()


