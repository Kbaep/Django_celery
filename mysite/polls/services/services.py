import time
from polls.models import Balance
from mysite.celery import app


@app.task(serializer = 'json')
def activebalance(id: int) -> None:
    print('timeeeeeeeeeeeeeeeeeeeeeeeeeeee')
    time.sleep(15)
    Balance.objects.filter(id=id).update(status='Activ')

