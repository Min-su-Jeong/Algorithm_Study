#include <bits/stdc++.h>
using namespace std;

int ret = 0;
string s;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    cin >> s;

    for (char c : s) {
        if (c >= 'A' && c <= 'C') ret += 3;
        else if (c >= 'D' && c <= 'F') ret += 4;
        else if (c >= 'G' && c <= 'I') ret += 5;
        else if (c >= 'J' && c <= 'L') ret += 6;
        else if (c >= 'M' && c <= 'O') ret += 7;
        else if (c >= 'P' && c <= 'S') ret += 8;
        else if (c >= 'T' && c <= 'V') ret += 9;
        else if (c >= 'W' && c <= 'Z') ret += 10;
    }

    cout << ret << '\n';
    return 0;
}