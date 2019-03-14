from tasks import add

print(add.delay(1, 1).get(timeout=3.))
