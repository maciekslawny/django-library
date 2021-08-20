from celery import task

@task
def celery_function():
    print('wykonanie zadania celery')