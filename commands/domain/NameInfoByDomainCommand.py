from __future__ import annotations
from abc import ABC, abstractmethod

from commands.abstractcommands import AbstractCommand
from services.employee_service import EmployeeService


class NameInfoByDomain(AbstractCommand):
    def __init__(self):
        self.employeeService = EmployeeService()

    def execute(self, DomainName: str):
        return self.employeeService.getNameByDomain(DomainName)


if __name__ == "__main__":
    """
    The client code can parameterize an invoker with any commands.
    """
    empInfo = NameInfoByDomain()
    empInfo.execute("P")
