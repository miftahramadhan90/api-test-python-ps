import requests
from requests.adapters import HTTPAdapter
from urllib3.util import Retry
from userDefinedVariable import *
from payload import loginPayload as payload
import pytest
from userDefinedVariable import *

@pytest.fixture(scope='class')
def student_session(request):
    with requests.Session() as s:
        retries = Retry(
            total=3,
            backoff_factor=1,
            status_forcelist=[502, 503, 504],
            allowed_methods={'POST', 'GET', 'DELETE', 'PATCH', 'PUT'}
        )
        # Mount the adapter with retries to the session
        adapter = HTTPAdapter(max_retries=retries)
        s.mount('https://', adapter)

        print(f"=========DEBUGGING Print password: {payload.student_login} ===========")
        res_login = s.post(f'{baseURL}{login_path}', data=payload.student_login)
        res_login.raise_for_status()

        #parse token
        access = res_login.json()["data"]["jwt"]["access"]

        #set auth_token
        s.headers.update({
            "Authorization": f'Bearer {access}',
            "Content-Type": "application/json"
        })

    # Store session in class instance for all test methods
    request.cls.student_session = s

    yield s

def admin_setup_session(request):
    pass