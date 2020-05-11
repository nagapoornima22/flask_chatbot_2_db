import sqlite3
import json
import requests


class EmployeeDao():
    def __init__(self):
        self.name = "EmployeeDB"
        # print("You have reached class ", self.name)

    #def getDBConnection(self):
        #response = requests.get('http://dummy.restapiexample.com/api/v1/employees')
        #print(response)
        #result = response.json()
        #print(result)
        #return result

    def getDBConnection(self):
        return sqlite3.connect('E:/python_workspace/chatbot_2_flask/app/main/dao/company.db')

    '''def getEmployeeInfoByName(self,  empName):
        json = self.getDBConnection()
        print(json)
        for x in json.get('data'):
            if x.get('employee_name').lower() == empName:
                print("get emp detils "+x)
                return x'''

    def getEmployeeInfoByName(self, empName: str):
        self.sqliteConnection = self.getDBConnection()
        #self.sqliteConnection.row_factory = self.getJsonFormat
        cursor = self.sqliteConnection.cursor()
        sqlite_select_query = """SELECT * from EMPLOYEE where NAME like ?"""
        empName = "%" + empName + "%"
        cursor.execute(sqlite_select_query, (empName,))
        result = cursor.fetchall()
        return result
        cursor.close()
    # return json.dumps([dict(ix) for ix in result])  # CREATE JSON

    def getEmployeeInfoById(self, empId: int):
        self.sqliteConnection = self.getDBConnection()
        cursor = self.sqliteConnection.cursor()
        sqlite_select_query = """SELECT * from EMPLOYEE where Id=?"""
        cursor.execute(sqlite_select_query, (empId,))
        result = cursor.fetchone()
        return result
        cursor.close()

    def getDomainInfoByName(self, empName: str):
        self.sqliteConnection = self.getDBConnection()
        cursor = self.sqliteConnection.cursor()
        sqlite_select_query = """SELECT * from TECH where NAME like ?"""
        empName = "%" + empName + "%"
        cursor.execute(sqlite_select_query, (empName,))
        result = cursor.fetchall()
        return result
        cursor.close()

    def getDomainInfoById(self, empId: int):
        self.sqliteConnection = self.getDBConnection()
        cursor = self.sqliteConnection.cursor()
        sqlite_select_query = """SELECT * from TECH where Id=?"""
        cursor.execute(sqlite_select_query, (empId,))
        result = cursor.fetchone()
        return result
        cursor.close()

    def getNameInfoByDomain(self, DomainName: str):
        self.sqliteConnection = self.getDBConnection()
        cursor = self.sqliteConnection.cursor()
        sqlite_select_query = """SELECT * from TECH where DOMAIN like ?"""
        DomainName = "%" + DomainName + "%"
        cursor.execute(sqlite_select_query, (DomainName,))
        result = cursor.fetchall()
        return result
        cursor.close()

    def getEmployees(self):
        self.employees = self.getDBConnection()
        return self.employees


