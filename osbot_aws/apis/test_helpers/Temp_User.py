from osbot_aws.apis.IAM import IAM
from osbot_utils.utils.Misc import random_filename, random_string


class Temp_User:
    def __init__(self):
        self.user_name  = f'temp_user_{random_string()}'
        self.iam        = IAM(user_name=self.user_name)

    def __enter__(self):
        self.iam.user_create()
        return self

    def __exit__(self, type, value, traceback):
        self.iam.user_delete()
