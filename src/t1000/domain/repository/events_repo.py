from datetime import datetime, timedelta

from ..entity import Events


class EventsRepo():
    def __init__(self, persistence):
        self._repo = persistence

    def get_from_today(self) -> Events:
        return self.get_from_date(datetime.today().date().isoformat())

    def get_from_date(self, date: str) -> Events:
        return self._repo.get_from_date(date)

    def get_month(self) -> Events:
        year = str(datetime.today().year)
        month = datetime.today().month
        from_date = datetime.strptime('-'.join([year, str(month)]), '%Y-%m').\
            date().isoformat()
        to_date = (datetime.strptime('-'.join([year, str(month + 1)]), '%Y-%m')
                   + timedelta(days=-1)).date().isoformat()
        return self._repo.get_from_interval(init=from_date, end=to_date)

    def all(self):
        pass
