from celery import Celery, Task

app = Celery('tasks', broker='redis://172.16.20.141:6379/10')


@app.task
def add(x, y):
    return x + y