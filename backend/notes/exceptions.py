from rest_framework.exceptions import APIException


class NotesDoesNotExist(APIException):
    status_code = 400
    default_detail = 'You have not added any Notes yet.'


class SuccessfullyDeleted(APIException):
    status_code = 200
    default_detail = 'Selected Note Deleted.'
