from gloify.celery import celery


@celery.task(name='celery_test')
def celery_test(name):
    print(f"OK {name}")


@celery.task
def celery_test_async(name):
    print(f"ASYNC OK {name}")


@celery.task(name='beat_test')
def beat_test():
    print("BEAT SERVICE IS OK")