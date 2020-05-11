from dao.employee_dao import EmployeeDao
from dto.employee_dto import EmployeeDTO
from dto.employee_dto import DomainDTO
import json


class EmployeeService():

    def __init__(self):
        self.employeeDao = EmployeeDao();
        self.empList = []

    def getEmployeeByName(self, empName: str):
        self.empList = self.employeeDao.getEmployeeInfoByName(empName)
        #print(self.empList)
        self.actualList = []
        for emp in self.empList:
            #self.actualList.append(EmployeeDTO.getItem(self.empList))
            #self.actualList.append(EmployeeDTO(emp).__dict__)
            self.actualList.append(EmployeeDTO.getItem(emp))
            # print(self.actualList[0].name)
        print(self.actualList)
        return self.actualList
            # return self.empList;

    def getEmployeeById(self, empId: int):
        self.emp = self.employeeDao.getEmployeeInfoById(empId)
        self.emp = EmployeeDTO(self.emp)

        print(self.emp)
        return self.emp

    def getDomainByName(self, empName: str):
        self.empList = self.employeeDao.getDomainInfoByName(empName)
        self.actualList = []
        for emp in self.empList:
            self.actualList.append(DomainDTO.getItem(emp))

        print(self.actualList)
        return self.actualList

    def getDomainById(self, empId: int):
        self.emp = self.employeeDao.getDomainInfoById(empId)
        self.emp = DomainDTO(self.emp)

        print(self.emp)
        return self.emp

    def getNameByDomain(self, empName: str):
        self.empList = self.employeeDao.getNameInfoByDomain(empName)
        self.actualList = []
        for emp in self.empList:
            self.actualList.append(DomainDTO(emp))

        print(self.actualList)
        return self.actualList

    def getEmployees(self):
        self.empList = self.employeeDao.getEmployees()
        self.actualList = []
        #if self.empList != None:
        for emp in self.empList['data']:
            # print(json.dumps(EmployeeDTO(emp), default=lambda o: o.__dict__, sort_keys=True, indent=4))
            self.actualList.append(EmployeeDTO(emp).__dict__)
        return self.actualList
