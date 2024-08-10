import time

from pydantic import BaseModel, conint


class RGB(BaseModel):
    R: conint(ge=0, le=255)
    G: conint(ge=0, le=255)
    B: conint(ge=0, le=255)

    model_config = {
        'validate_assignment': True
    }


class Statement:
    def __init__(
            self,
            working_seconds: int,
            protected_seconds: int,
            sync_period: float = 1.0,
            default_color: RGB = RGB(R=0, G=0, B=0)
    ):
        if protected_seconds > working_seconds:
            raise ValueError("protected_seconds can not be greater than working_seconds")

        self._start_at: float = time.time()
        self._working_seconds: int = working_seconds
        self._protected_seconds: int = protected_seconds
        self._sync_period: float = sync_period
        self._default_color: RGB = default_color
        self._color: RGB = default_color
        self._updated_at = 0.0

    def get_color(self) -> RGB:
        if self._updated_at + self._working_seconds < time.time():
            return self._default_color
        return self._color

    def set_color(self, color: RGB) -> bool:
        next_change_available_in = self.next_change_available_in()
        if self._updated_at + self._protected_seconds < time.time():
            self._updated_at = time.time()
            self._color = color
            return True
        else:
            return False

    def next_change_available_in(self) -> float:
        next_change_available_in = self._updated_at + self._protected_seconds - time.time()
        if next_change_available_in < 0:
            next_change_available_in = 0.0
        return next_change_available_in

    def seconds_until_next_sync(self) -> float:
        elapsed_time = time.time() - self._start_at
        full_periods_passed = int(elapsed_time // self._sync_period)
        next_sync_time = self._start_at + (full_periods_passed + 1) * self._sync_period
        return next_sync_time - time.time()


statement = Statement(
    working_seconds=300,
    protected_seconds=10
)
