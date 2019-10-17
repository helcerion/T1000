from datetime import datetime, timedelta

from ..entity import Events

class EventsRepo(object):
    def __init__(self, persistence):
        self._repo = persistence

    def getFromToday(self):
        return self.getFromDate(datetime.today().date().isoformat())

    def getFromDate(self, date: str) -> Events:
        return self._repo.getFromDate(date)
        

    def getMonth(self):
        year = str(datetime.today().year)
        month = datetime.today().month
        from_date = datetime.strptime('-'.join([year, str(month)]), '%Y-%m').date().isoformat()
        to_date = (datetime.strptime('-'.join([year, str(month + 1)]), '%Y-%m') + timedelta(days=-1)).date().isoformat()
        return self._repo.getFromInterval(init=from_date, end=to_date)

    def all(self):
        pass
