#include"WorkerManager.h"

//"::" scope
WorkerManager::WorkerManager() {

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

WorkerManager::~WorkerManager() {

}