class ProcessError(Exception):
    pass


class InvalidProcessNameError(ProcessError):
    pass


class ProcessAlreadyExistsError(ProcessError):
    pass
