from abc import ABC, abstractmethod
import time


class Work(ABC):
    @abstractmethod
    def work(self):
        pass


class Eat(ABC):
    @abstractmethod
    def eat(self):
        pass


class Worker(Work, Eat):
    def work(self):
        print("I'm a normal worker. I'm working.")

    def eat(self):
        print("Lunch break....(5 secs)")
        time.sleep(5)


class SuperWorker(Work, Eat):
    def work(self):
        print("I'm a super worker. I work very hard!")

    def eat(self):
        print("Lunch break....(3 secs)")
        time.sleep(3)


class WorkManager:
    def __init__(self):
        self.worker = None

    def set_worker(self, worker):
        assert isinstance(worker, Work), "`worker` must be able to work"
        self.worker = worker

    def manage(self):
        if self.worker is not None:
            self.worker.work()


class EatManager:
    def __init__(self):
        self.worker = None

    def set_worker(self, worker):
        assert isinstance(worker, Eat), "`worker` must be able to eat"
        self.worker = worker

    def lunch_break(self):
        if self.worker is not None:
            self.worker.eat()


class Robot(Work):
    def work(self):
        print("I'm a robot. I'm working....")


work_manager = WorkManager()
work_manager.set_worker(Worker())
work_manager.manage()

eat_manager = EatManager()
eat_manager.set_worker(Worker())
eat_manager.lunch_break()

work_manager.set_worker(SuperWorker())
work_manager.manage()

eat_manager.set_worker(SuperWorker())
eat_manager.lunch_break()

work_manager.set_worker(Robot())
