import json

import requests
from django.conf import settings
from models import User

class SettingsBackend(object):
    def authenticate(self, username=None, password=None):
        payload = {'username': username, 'password': password}
        header = {'Content-Type': 'application/json'}
        request = requests.post("http://susi.apphb.com/api/Login", headers=header, data=json.dumps(payload))
        if request.status_code == 200:
            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                payload = {'key': request.json()}
                request = requests.post("http://susi.apphb.com/api/Student", headers=header, data=json.dumps(payload))

                user = User.objects.create(username=username,
                    faculty_number=request.json()['facultyNumber'],
                    first_name=request.json()['firstName'],
                    last_name=request.json()['lastName'],
                    email='{}@uni-sofia.bg'.format(username)
                )
            user.set_password(password)
            user.save()
            return user
        return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
