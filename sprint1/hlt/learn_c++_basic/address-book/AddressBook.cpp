#include<iostream>
#include<string>
#define MAX 1000 //do not end with ";"
using namespace std;

struct Person
{
    string m_Name;
    int m_Sex;
    int m_Age;
    string m_Phone;
    string m_Addr;
};

struct AddressBook
{
    struct Person personArray[MAX];
    int m_Size;
};

void showMenu()
{
    cout<<"1. Add new person"<<endl;
    cout<<"0. Exit"<<endl;
}

void addPerson(AddressBook * abs)
    {
        if(abs->m_Size == MAX)
        {
            cout<<"AddressBook is full!"<<endl;
            return;
        }
        else
        {
            string name;
            cout<<"Please enter the name: "<<endl;
            cin>>name;
            abs->personArray[abs->m_Size].m_Name = name;

            int sex;
            cout<<"Please enter the sex number: "<<endl;
            cout<<"1 --- man"<<endl;
            cout<<"2 --- woman"<<endl;
            while(true)
            {
                cin>>sex; //cin out of while() may make program never stop 
                if(sex == 1 || sex == 2)
                {
                    abs->personArray[abs->m_Size].m_Sex = sex;
                    break; //break from while()
                }
                cout<<"Please enter right number: "<<endl;
            }
            
            int age;
            cout<<"Please enter the age: "<<endl;
            cin>>age;
            abs->personArray[abs->m_Size].m_Age = age;

            string phone;
            cout<<"Please enter the phone number: "<<endl;
            cin>>phone;
            abs->personArray[abs->m_Size].m_Phone = phone;

            string addr;
            cout<<"Please enter the address: "<<endl;
            cin>>addr;
            abs->personArray[abs->m_Size].m_Addr = addr;

            abs->m_Size++;

            cout<<"Added successfully!"<<endl;

            system("pause");
            system("cls");

        }
    }

int main()
{
    AddressBook abs;
    abs.m_Size = 0;

    while (true)
    {
        showMenu();
        int select;
        cin>>select;
        switch (select)
        {
            case 1:
            addPerson(&abs); //end with ";" when use function
                break;

            case 0:
            cout<<"bye~"<<endl;
            system("pause");
            return 0; //shut dowm main()
                break;
        
            default:
                break;
        }
    }
}