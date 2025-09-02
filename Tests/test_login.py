from payload.loginPayload import *
from userDefinedVariable import *
import pytest

@pytest.mark.usefixtures("student_session")
class TestLoginStudent:
    def test_login_student_failed(self):
        login = self.student_session.post(f'{baseURL}{login_path}', data=student_invalid_login)
        assert login.status_code == 400, f"status is unexpected : {login.status_code}"


    def test_login_blocked_student(self):
        pass

