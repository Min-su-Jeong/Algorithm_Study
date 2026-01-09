#include <string>
#include <vector>

using namespace std;

bool check(char c, string skip) {
    for (int i=0; i<skip.size(); i++) {
        if (c == skip[i]) return false;
    }
    return true;
}

string solution(string s, string skip, int index) {
    string ret = "";

    for (char c: s) {
        for (int i=0; i<index;) {
            c += 1;
            if (c == 'z'+1) c = 'a';
            if (check(c, skip)) i++;
        }
        ret += c;
    }
    return ret;
}