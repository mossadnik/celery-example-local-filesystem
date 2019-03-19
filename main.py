"""Client code with no access to tasks code base."""

from celery import Celery, signature

app = Celery('tasks')
app.config_from_object('celeryconfig')

add = signature('tasks.add')

print('1 + 1 = {}'.format(add.delay(1, 1).get(timeout=3.)))
