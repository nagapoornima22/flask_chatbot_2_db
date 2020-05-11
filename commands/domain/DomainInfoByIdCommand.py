from __future__ import annotations
from abc import ABC, abstractmethod

from commands.abstractcommands import AbstractCommand
from services.employee_service import EmployeeService


class DomainInfoById(AbstractCommand):
    def __init__(self):
        self.employeeService = EmployeeService()

    def execute(self, empId: int):
        return self.employeeService.getDomainById(empId)


if __name__ == "__main__":
    """
    The client code can parameterize an invoker with any commands.
    """
    empInfo = DomainInfoById()
    empInfo.execute(2)
