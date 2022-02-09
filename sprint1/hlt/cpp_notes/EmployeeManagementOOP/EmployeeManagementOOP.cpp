#include<iostream>
#include"WorkerManager.h"
using namespace std;

int main() {
    WorkerManager wm;

    int choice = 0;

    while (true) {
        wm.showMenu();
        cout << "Please enter your choice :" << endl;
        cin >> choice;

        switch (choice)
        {
        case 1:
            break;

        case 2:
            break;

        case 3:
            break;

        case 4:
            break;

        case 5:
            break;

        case 6:
            break;

        case 7:
            break;

        case 0:
            wm.exitSystem();
            break;

        default:
            system("clc");
            break;
        }
    }

    wm.showMenu();

    system("pause");
    return 0;
}