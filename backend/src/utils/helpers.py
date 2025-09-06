def format_response(data, status=200, message=''):
    return {
        'status': status,
        'message': message,
        'data': data
    }