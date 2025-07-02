#include <bits/stdc++.h>
using namespace std;

int N, ret;
string s;

bool isGroupWord(const string& s) {
    vector<bool> visited(26, false);
    char prev = 0;

    for (char c : s) {
        if (c != prev) {
            if (visited[c - 'a']) return false;
            visited[c - 'a'] = true;
        }
        prev = c;
    }
    return true;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    cin >> N;
    while (N--) {
        cin >> s;
        if (isGroupWord(s)) ret++;
    }

    cout << ret << '\n';
    return 0;
}