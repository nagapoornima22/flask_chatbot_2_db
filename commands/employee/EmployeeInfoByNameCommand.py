from __future__ import annotations
from abc import ABC, abstractmethod

from commands.abstractcommands import AbstractCommand
from services.employee_service import EmployeeService


class EmployeeInfoByName(AbstractCommand):
    def __init__(self):
        self.employeeService = EmployeeService()

    def execute(self, empName: str):
        #print("emp name"+empName)
        return self.employeeService.getEmployeeByName(empName)


if __name__ == "__main__":
    """
    The client code can parameterize an invoker with any commands.
    """
    empInfo = EmployeeInfoByName()
    empInfo.execute("p")
