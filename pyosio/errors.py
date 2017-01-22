# coding=utf-8
from requests import RequestException


class OSIOClientError(Exception):

    """An error during your request occurred.
    Super class for all Open Sensor api errors.
    """

    def __init__(self, message, error_type=None):
        self.type = error_type
        self.message = message
        if error_type is not None:
            self.message = '%s: %s' % (error_type, message)

        super(OSIOClientError, self).__init__(self.message)


class OSIOClientApiError(OSIOClientError):
    pass


class OSIOClientAuthError(OSIOClientError):
    pass


class TimeoutError(OSIOClientError):

    """A request timeout occurred.
    """

    def __init__(self, timeout):
        self.timeout = timeout
