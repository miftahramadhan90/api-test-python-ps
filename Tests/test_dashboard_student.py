from userDefinedVariable import *
import pytest


@pytest.mark.usefixtures("student_session")
class TestDashboardStudent:

    def test_dashboard_student(self):
        dashboard = self.student_session.get(f'{baseURL}{dashboard_path}')

        assert dashboard.status_code == 200, "fail load dashboard page"
        assert 'latest_five_assessments' in dashboard.json()["data"]
