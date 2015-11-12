from datetime import timedelta

class TaskError(Exception):
    pass

class ScheduleError(Exception):
    pass

class Tasks:
    def __init__(self, a_name, a_beginning, an_end):
        if an_end < a_beginning:
            raise TaskError('The begin time must precede the end time')
        if an_end - a_beginning < timedelta(minutes=5):
            raise TaskError('Minimum duration is 5 minutes')
        self.name = a_name
        self.begins = a_beginning
        self.ends = an_end

    def excludes(self, an_other):
        raise NotImplemented('Abstract method. Use a derived class')

class Activities(Tasks):
    def excludes(self, an_other):
        return isinstance(an_other, Activities)

class Statuses(Tasks):
    def excludes(self, an_other):
        return False
