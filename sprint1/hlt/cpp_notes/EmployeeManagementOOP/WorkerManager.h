#pragma once
#include<iostream>
#include"Worker.h"
#include"Employee.h"
#include"Manager.h"
#include"Boss.h"
using namespace std;

class WorkerManager {
public:

    WorkerManager(); //constructor

    void showMenu();

    void exitSystem();

    int m_EmpNum;

    Worker** m_EmpArray;

    void addEmp();

    ~WorkerManager(); //destructor
};