import inspect


class TerminatedError(Exception):
    """Raised when the bot has been termined by user or critical error"""


class WheelError(Exception):
    """Base class for all wheel exceptions"""


class WheelNotAccessibleError(WheelError):
    """Raised when a wheel accessed."""

    def __init__(self, wheel: str) -> None:
        self.wheel = wheel

    def __str__(self) -> str:
        return f"Wheel '{self.wheel}' could not be activated!"

class UnexpectedWheelError(WheelError):
    """Raised when a wheel was accessed, but not the correct one"""

    def __init__(self, expected: str, got: str) -> None:
        self.expected_wheel = expected
        self.got_wheel = got

    def __str__(self) -> str:
        return f"Unexpected wheel accessed. Expected '{self.expected_wheel}', got '{self.got_wheel}'!"


class InterfaceError(Exception):
    """Base class for all interface exceptions"""

class BedNotAccessibleError(InterfaceError):
    """Raised when the bed map could not be opened."""


class BedNotFoundError(InterfaceError):
    """Raised when the bed map could not be opened."""






class InventoryError(InterfaceError):
    """Base class for all inventory exceptions"""






class InventoryNotOpenError(InventoryError):
    """Raised when attempting an interaction within the
    inventory when it is not open"""

    def __init__(self) -> None:
        self.action = inspect.stack()[1][3]
        
    def __str__(self) -> str:
        return f"Attempted interaction '{self.action}' with closed inventory!"


class InventoryNotAccessibleError(InventoryError):
    """Raised when the inventory cannot be accessed."""


class InventoryNotClosableError(InventoryError):
    """Raised when the inventory cannot be closed"""



class ReceivingRemoveInventoryTimeout(InventoryError):
    """Raised when the 'Receiving Remote Inventory' text does not disappear."""


class NoItemsAddedError(InventoryError):
    """Raised when items were not added to the inventory if expected."""

    def __init__(self, expected_item: str) -> None:
        self.item = expected_item

    def __str__(self) -> str:
        return f"Expected item {self.item} was not added!"

class NoItemsDepositedError(InventoryError):
    """Raised when the 'X items deposited.' message does not appear."""


class NoGasolineError(InventoryError):
    """Raised when a structure can not be turned on"""

    def __init__(self, structure_name) -> None:
        self.structure = structure_name

    def __str__(self) -> str:
        return f"{self.structure} is out of gasoline!"

class PlayerError(Exception):
    """Base exception for all player errors"""

class PlayerDidntSpawnError(PlayerError):
    """Raised when the player could not spawn in"""

class PlayerDidntTravelError(PlayerError):
    """Raised when the travel screen could not be detected"""


class LogsNotOpenedError(Exception):
    """Raised when the logs could not be opened"""


class ServerNotFoundError(Exception):
    """Raised when a server could not be found after 15 minutes."""


class DediNotInRangeError(Exception):
    """Raised when the dedi deposit text could not be detected"""

class DinoNotMountedError(Exception):
    """Raised when a dino cannot be mounted, either because it does not
    have a saddle, or because its not close enough."""