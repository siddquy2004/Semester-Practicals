#include <iostream>
#include <vector>
#include <string>
using namespace std;

struct student {
    int roll_number;
    string name;
    string course;
    float marks;
};

class student_management_system {
private:
    vector<student> students;
public:
    void add_student() {
        student s;
        cout << "enter roll number: ";
        cin >> s.roll_number;
        cin.ignore();
        cout << "enter name: ";
        getline(cin, s.name);
        cout << "enter course: ";
        getline(cin, s.course);
        cout << "enter marks: ";
        cin >> s.marks;
        students.push_back(s);
        cout << "student added successfully!\n";
    }

    void display_students() {
        if (students.empty()) {
            cout << "no students to display.\n";
            return;
        }
        for (const auto& s : students) {
            cout << "roll number: " << s.roll_number << endl;
            cout << "name: " << s.name << endl;
            cout << "course: " << s.course << endl;
            cout << "marks: " << s.marks << endl;
            cout << "------------------------\n";
        }
    }

    void search_student() {
        int roll;
        cout << "enter roll number to search: ";
        cin >> roll;
        for (const auto& s : students) {
            if (s.roll_number == roll) {
                cout << "student found!\n";
                cout << "name: " << s.name << endl;
                cout << "course: " << s.course << endl;
                cout << "marks: " << s.marks << endl;
                return;
            }
        }
        cout << "student not found.\n";
    }

    void delete_student() {
        int roll;
        cout << "enter roll number to delete: ";
        cin >> roll;
        for (auto it = students.begin(); it != students.end(); ++it) {
            if (it->roll_number == roll) {
                students.erase(it);
                cout << "student deleted successfully.\n";
                return;
            }
        }
        cout << "student not found.\n";
    }
};

int main() {
    student_management_system sms;
    int choice;
    do {
        cout << "\nstudent information management system\n";
        cout << "1. add student\n";
        cout << "2. display students\n";
        cout << "3. search student\n";
        cout << "4. delete student\n";
        cout << "5. exit\n";
        cout << "enter your choice: ";
        cin >> choice;
        switch (choice) {
            case 1:
                sms.add_student();
                break;
            case 2:
                sms.display_students();
                break;
            case 3:
                sms.search_student();
                break;
            case 4:
                sms.delete_student();
                break;
            case 5:
                cout << "exiting...\n";
                break;
            default:
                cout << "invalid choice. try again.\n";
        }
    } while (choice != 5);

    return 0;
}
