#include <bits/stdc++.h>
using namespace std;

int N;
string s, ret;
vector<string> v;

void go() {
    while (true) {
        if (ret.size() && ret.front() == '0') ret.erase(ret.begin());
        else break;
    }
    if (ret.size() == 0) ret = "0";
    v.push_back(ret);
    ret = "";
}

bool cmp(string a, string b) {
    if (a.size() == b.size()) return a < b;
    return a.size() < b.size();
}

int main() {
    ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

    cin >> N;
    while (N--) {
        cin >> s;
        ret = "";
        for (int i=0; i<s.size(); i++) {
            int idx = s[i];
            if (idx < 65) ret += s[i];
            else if (ret.size()) go();
        }
        if (ret.size()) go();
    }
    sort(v.begin(), v.end(), cmp);
    for (string i: v) cout << i << '\n';
    
    return 0;
}