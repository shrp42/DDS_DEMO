from celery import shared_task
import time

@shared_task
def slow_task():
    print("Начинаю очень долгую задачу...")
    time.sleep(10) # Имитируем тяжелую работу
    print("Ура! Задача выполнена!")
    return "Готово"