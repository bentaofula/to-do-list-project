from sqlalchemy.orm import sessionmaker
from models import Task, User, Category, engine
import click

Session = sessionmaker(bind=engine)
session = Session()

@click.group()
def cli():
    """CLI for managing tasks in the todo list"""
    pass

@click.command()
@click.argument('title')
@click.argument('user_id', type=int)
@click.argument('category_id', type=int)
def create_task(title, user_id, category_id):
    """Create a new task"""
    task = Task(title=title, user_id=user_id, category_id=category_id)
    session.add(task)
    session.commit()
    click.echo('Task created successfully.')

@click.command()
@click.argument('user_id', type=int)
def list_tasks(user_id):
    """List tasks for a specific user"""
    tasks = session.query(Task).filter(Task.user_id == user_id).all()
    if tasks:
        click.echo(f'Tasks for User ID {user_id}:')
        for task in tasks:
            click.echo(f'- {task.title}')
    else:
        click.echo(f'No tasks found for User ID {user_id}.')

@click.command()
def list_users():
    """List all users"""
    users = session.query(User).all()
    if users:
        click.echo('Users:')
        for user in users:
            click.echo(f'- User ID: {user.id}, Name: {user.name}')
    else:
        click.echo('No users found.')

@click.command()
def list_categories():
    """List all categories"""
    categories = session.query(Category).all()
    if categories:
        click.echo('Categories:')
        for category in categories:
            click.echo(f'- Category ID: {category.id}, Name: {category.name}')
    else:
        click.echo('No categories found.')

@click.command()
@click.argument('task_id', type=int)
def complete_task(task_id):
    """Mark a task as completed"""
    task = session.query(Task).get(task_id)
    if task:
        task.completed = True
        session.commit()
        click.echo('Task marked as completed.')
    else:
        click.echo(f'Task with ID {task_id} not found.')

@click.command()
@click.argument('task_id', type=int)
def delete_task(task_id):
    """Delete a task"""
    task = session.query(Task).get(task_id)
    if task:
        session.delete(task)
        session.commit()
        click.echo('Task deleted successfully.')
    else:
        click.echo(f'Task with ID {task_id} not found.')

cli.add_command(create_task)
cli.add_command(list_tasks)
cli.add_command(list_users)
cli.add_command(list_categories)
cli.add_command(complete_task)
cli.add_command(delete_task)

if __name__ == '__main__':
    cli()
