#!/usr/bin/env python3

import click
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Task, User, task_user


engine = create_engine('sqlite:///new_todo_test.db', echo=True)
Session = sessionmaker(bind=engine)
session = Session()

@click.group()
def func():
    pass

@click.command()
def list_tasks():
    tasks = session.query(Task).all()
    if tasks:
        click.echo("All Tasks:")
        for task in tasks:
            t = (task.id, task.title, task.user_id)
            click.echo(f"Task: {t}")
    else:
        click.echo("No tasks found") 

@click.command()
def list_users():
    users = session.query(User).all()
    if users:
        click.echo("All Users:")
        for user in users:
            u = {
                "id": user.id,
                "username": user.username,
                "email": user.email
            }
            click.echo(u)
    else:
        click.echo("No users found")

@click.command()
@click.option("--title", prompt="Enter the task title", help="Task title")
@click.option("--user-id", prompt="Enter the user ID", help="User ID")
def add_task(title, user_id):
    user_id = int(user_id)
    user = session.query(User).filter(User.id == user_id).first()
    if not user:
        click.echo("User not found")
        return

    task = Task(title=title, user_id=user_id)
    session.add(task)
    session.commit()
    click.echo("Task added successfully")

@click.command()
@click.option("--task-id", prompt="Enter the task ID", help="Task ID")
def delete_task(task_id):
    task_id = int(task_id)
    task = session.query(Task).filter(Task.id == task_id).first()
    if task:
        session.delete(task)
        session.commit()
        click.echo("Task deleted successfully")
    else:
        click.echo("Task not found")

@click.command()
def recent_tasks():
    task = session.query(Task).order_by(Task.id.desc()).first()
    if task:
        click.echo(f"Recently added task: {task}")
    else:
        click.echo("No tasks found")

func.add_command(list_tasks)
func.add_command(list_users)
func.add_command(add_task)
func.add_command(delete_task)
func.add_command(recent_tasks)

if __name__ == '__main__':
    func()
