#include <bits/stdc++.h>
using namespace std;

int N;
string s, ss;
vector<string> v;

void go() {
    while (true) {
        if (ss.size() && ss.front() == '0') ss.erase(ss.begin());
        else break;
    }
    if (ss.size() == 0) ss = "0";
    v.push_back(ss);
    ss = "";
}

bool cmp(string a, string b) {
    if (a.size() == b.size()) return a < b;
    return a.size() < b.size();
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    cin >> N;
    while (N--) {
        cin >> s;
        ss = "";
        for (int i=0; i<s.size(); i++) {
            int idx = s[i];
            if (idx < 65) ss += s[i];
            else if (ss.size()) go();
        }
        if (ss.size()) go();
    }
    sort(v.begin(), v.end(), cmp);
    for (string i: v) cout << i << '\n';

    return 0;
}