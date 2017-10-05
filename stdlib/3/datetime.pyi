import sys
from typing import Optional, SupportsAbs, Tuple, overload

MINYEAR = 0
MAXYEAR = 0

_TimeTuple = Tuple[int, int, int, int, int, int, int, int, int]

class tzinfo:
    def tzname(self, dt: Optional[datetime]) -> str: ...
    def utcoffset(self, dt: Optional[datetime]) -> Optional[timedelta]: ...
    def dst(self, dt: Optional[datetime]) -> Optional[timedelta]: ...
    def fromutc(self, dt: datetime) -> datetime: ...

class timezone(tzinfo):
    utc = ...  # type: timezone
    min = ...  # type: timezone
    max = ...  # type: timezone

    def __init__(self, offset: timedelta, name: str = ...) -> None: ...
    def __hash__(self) -> int: ...

_tzinfo = tzinfo
_timezone = timezone

class date:
    min = ...  # type: date
    max = ...  # type: date
    resolution = ...  # type: timedelta

    def __init__(self, year: int, month: int, day: int) -> None: ...

    @classmethod
    def fromtimestamp(cls, t: float) -> date: ...
    @classmethod
    def today(cls) -> date: ...
    @classmethod
    def fromordinal(cls, n: int) -> date: ...

    @property
    def year(self) -> int: ...
    @property
    def month(self) -> int: ...
    @property
    def day(self) -> int: ...

    def ctime(self) -> str: ...
    def strftime(self, fmt: str) -> str: ...
    def __format__(self, fmt: str) -> str: ...
    def isoformat(self) -> str: ...
    def timetuple(self) -> tuple: ...  # TODO return type
    def toordinal(self) -> int: ...
    def replace(self, year: int = ..., month: int = ..., day: int = ...) -> date: ...
    def __le__(self, other: date) -> bool: ...
    def __lt__(self, other: date) -> bool: ...
    def __ge__(self, other: date) -> bool: ...
    def __gt__(self, other: date) -> bool: ...
    def __add__(self, other: timedelta) -> date: ...
    @overload
    def __sub__(self, other: timedelta) -> date: ...
    @overload
    def __sub__(self, other: date) -> timedelta: ...
    def __hash__(self) -> int: ...
    def weekday(self) -> int: ...
    def isoweekday(self) -> int: ...
    def isocalendar(self) -> Tuple[int, int, int]: ...

class time:
    min = ...  # type: time
    max = ...  # type: time
    resolution = ...  # type: timedelta

    def __init__(self, hour: int = ..., minute: int = ..., second: int = ..., microsecond: int = ...,
                 tzinfo: Optional[tzinfo] = ...) -> None: ...

    @property
    def hour(self) -> int: ...
    @property
    def minute(self) -> int: ...
    @property
    def second(self) -> int: ...
    @property
    def microsecond(self) -> int: ...
    @property
    def tzinfo(self) -> Optional[_tzinfo]: ...

    def __le__(self, other: time) -> bool: ...
    def __lt__(self, other: time) -> bool: ...
    def __ge__(self, other: time) -> bool: ...
    def __gt__(self, other: time) -> bool: ...
    def __hash__(self) -> int: ...
    def isoformat(self) -> str: ...
    def strftime(self, fmt: str) -> str: ...
    def __format__(self, fmt: str) -> str: ...
    def utcoffset(self) -> Optional[timedelta]: ...
    def tzname(self) -> Optional[str]: ...
    def dst(self) -> Optional[int]: ...
    def replace(self, hour: int = ..., minute: int = ..., second: int = ...,
                microsecond: int = ..., tzinfo: Optional[_tzinfo] = None) -> time: ...

_date = date
_time = time

class timedelta(SupportsAbs[timedelta]):
    min = ...  # type: timedelta
    max = ...  # type: timedelta
    resolution = ...  # type: timedelta

    def __init__(self, days: float = ..., seconds: float = ..., microseconds: float = ...,
                 milliseconds: float = ..., minutes: float = ..., hours: float = ...,
                 weeks: float = ...) -> None: ...

    @property
    def days(self) -> int: ...
    @property
    def seconds(self) -> int: ...
    @property
    def microseconds(self) -> int: ...

    def total_seconds(self) -> float: ...
    def __add__(self, other: timedelta) -> timedelta: ...
    def __radd__(self, other: timedelta) -> timedelta: ...
    def __sub__(self, other: timedelta) -> timedelta: ...
    def __rsub(self, other: timedelta) -> timedelta: ...
    def __neg__(self) -> timedelta: ...
    def __pos__(self) -> timedelta: ...
    def __abs__(self) -> timedelta: ...
    def __mul__(self, other: float) -> timedelta: ...
    def __rmul__(self, other: float) -> timedelta: ...
    @overload
    def __floordiv__(self, other: timedelta) -> int: ...
    @overload
    def __floordiv__(self, other: int) -> timedelta: ...
    @overload
    def __truediv__(self, other: timedelta) -> float: ...
    @overload
    def __truediv__(self, other: float) -> timedelta: ...
    def __mod__(self, other: timedelta) -> timedelta: ...
    def __divmod__(self, other: timedelta) -> Tuple[int, timedelta]: ...
    def __le__(self, other: timedelta) -> bool: ...
    def __lt__(self, other: timedelta) -> bool: ...
    def __ge__(self, other: timedelta) -> bool: ...
    def __gt__(self, other: timedelta) -> bool: ...
    def __hash__(self) -> int: ...


class datetime:
    # TODO: Is a subclass of date, but this would make some types incompatible.
    min = ...  # type: datetime
    max = ...  # type: datetime
    resolution = ...  # type: timedelta

    def __init__(self, year: int, month: int, day: int, hour: int = ...,
                 minute: int = ..., second: int = ..., microsecond: int = ...,
                 tzinfo: Optional[tzinfo] = ...) -> None: ...

    @property
    def year(self) -> int: ...
    @property
    def month(self) -> int: ...
    @property
    def day(self) -> int: ...
    @property
    def hour(self) -> int: ...
    @property
    def minute(self) -> int: ...
    @property
    def second(self) -> int: ...
    @property
    def microsecond(self) -> int: ...
    @property
    def tzinfo(self) -> Optional[_tzinfo]: ...

    @classmethod
    def fromtimestamp(cls, t: float, tz: Optional[_tzinfo] = ...) -> datetime: ...
    @classmethod
    def utcfromtimestamp(cls, t: float) -> datetime: ...
    @classmethod
    def today(cls) -> datetime: ...
    @classmethod
    def fromordinal(cls, n: int) -> datetime: ...
    @classmethod
    def now(cls, tz: Optional[_tzinfo] = ...) -> datetime: ...
    @classmethod
    def utcnow(cls) -> datetime: ...
    @classmethod
    def combine(cls, date: date, time: time) -> datetime: ...
    def strftime(self, fmt: str) -> str: ...
    def __format__(self, fmt: str) -> str: ...
    def toordinal(self) -> int: ...
    def timetuple(self) -> _TimeTuple: ...
    def timestamp(self) -> float: ...
    def utctimetuple(self) -> _TimeTuple: ...
    def date(self) -> _date: ...
    def time(self) -> _time: ...
    def timetz(self) -> _time: ...
    def replace(self, year: int = ..., month: int = ..., day: int = ..., hour: int = ...,
                minute: int = ..., second: int = ..., microsecond: int = ..., tzinfo:
                Optional[_tzinfo] = None) -> datetime: ...
    def astimezone(self, tz: Optional[_tzinfo] = ...) -> datetime: ...
    def ctime(self) -> str: ...
    if sys.version_info >= (3, 6):
        def isoformat(self, sep: str = ..., timespec: str = ...) -> str: ...
    else:
        def isoformat(self, sep: str = ...) -> str: ...
    @classmethod
    def strptime(cls, date_string: str, format: str) -> datetime: ...
    def utcoffset(self) -> Optional[timedelta]: ...
    def tzname(self) -> Optional[str]: ...
    def dst(self) -> Optional[int]: ...
    def __le__(self, other: datetime) -> bool: ...
    def __lt__(self, other: datetime) -> bool: ...
    def __ge__(self, other: datetime) -> bool: ...
    def __gt__(self, other: datetime) -> bool: ...
    def __add__(self, other: timedelta) -> datetime: ...
    @overload
    def __sub__(self, other: datetime) -> timedelta: ...
    @overload
    def __sub__(self, other: timedelta) -> datetime: ...
    def __hash__(self) -> int: ...
    def weekday(self) -> int: ...
    def isoweekday(self) -> int: ...
    def isocalendar(self) -> Tuple[int, int, int]: ...
