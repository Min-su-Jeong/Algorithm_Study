#include <iostream>
#include <string>

using namespace std;

int main(void) {
    string str;
    cin >> str;

    for (char c: str) {
        if ('a' <= c && c <= 'z') c -= 32;
        else if ('A' <= c && c <= 'Z') c += 32;
        cout << c;
    }
    return 0;
}