#include"WorkerManager.h"

//"::" scope
WorkerManager::WorkerManager() {
    //initialize properties
    this->m_EmpNum = 0;
    this->m_EmpArray = NULL;
}

void WorkerManager::showMenu() {
    cout << "Welcome to the EmployeeManagement system!" << endl;
    cout << "1. Add employee information" << endl;
    cout << "2. Show employee information" << endl;
    cout << "3. Delete ex-employee" << endl;
    cout << "4. Modify employee information" << endl;
    cout << "5. Find employee information" << endl;
    cout << "6. Sort by number" << endl;
    cout << "7. Clear document" << endl;
    cout << "0. Exit" << endl;
}

void WorkerManager::exitSystem() {
    cout << "bye~" << endl;
    system("pause");
    exit(0); //exit function
}

void WorkerManager::addEmp() {
    int addNum = 0;
    cout << "Please enter the number of employees to add: " << endl;
    cin >> addNum;

    if (addNum > 0) {
        int newSize = this->m_EmpNum + addNum;
        Worker** newSpace = new Worker * [newSize];

        if (this->m_EmpArray != NULL) {
            for (int i = 0; i < this->m_EmpNum; i++) {
                newSpace[i] = this->m_EmpArray[i];
            }
        }

        for (int i = 0; i < addNum; i++) {
            int id;
            string name;
            int deptId;

            cout << "Please enter the " << i + 1 << "-th employee number: " << endl;
            cin >> id;
            cout << "Please enter the " << i + 1 << "-th employee name: " << endl;
            cin >> name;
            cout << "Please enter the " << i + 1 << "-th employee rank: " << endl;
            cout << "1. Employee" << endl;
            cout << "2. Manager" << endl;
            cout << "3. Boss" << endl;
            cin >> deptId;

            Worker* worker = NULL;
            switch (deptId) {
            case 1:
                worker = new Employee(id, name, 1);
                break; //need 'break;' here
            case 2:
                worker = new Manager(id, name, 2);
                break;
            case 3:
                worker = new Boss(id, name, 3);
                break;
            default:
                break;
            }

            newSpace[this->m_EmpNum + i] = worker;
        }
        delete[] this->m_EmpArray;
        this->m_EmpArray = newSpace;
        this->m_EmpNum = newSize;

        cout << "Successfully added " << addNum << " new employees!" << endl;
    }
    else {
        cout << "Incorrect input, please try again." << endl;
    }

    system("pause");
    system("cls");
}

WorkerManager::~WorkerManager() {

}