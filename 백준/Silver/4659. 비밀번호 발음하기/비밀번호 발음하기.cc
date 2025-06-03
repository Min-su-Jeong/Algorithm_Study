#include <bits/stdc++.h>
using namespace std;

string s;

bool includeV(int idx) {
    return (idx == 'a' || idx == 'e' || idx == 'i' || idx == 'o' || idx == 'u');
}

int main() {
    ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

    while(true) {
        cin >> s;
        if (s == "end") break;
        
        int vcnt = 0, ccnt = 0, prev = -1;
        bool flag = 0, include_v = 0;

        for (int i=0; i<s.size(); i++) {
            // 조건 1
            int idx = s[i];
            if (includeV(idx)) vcnt++, ccnt = 0, include_v = 1;
            else vcnt = 0, ccnt++;

            // 조건 2
            if (vcnt == 3 || ccnt == 3) flag = 1;

            // 조건 3
            if (i >= 1 && (prev == idx) && (idx != 'e' && idx != 'o')) flag = 1;
            prev = idx;
        }
        
        if (!include_v) flag = 1;
        if (flag) cout << '<' << s << "> is not acceptable.\n";
        else cout << '<' << s << "> is acceptable.\n";
    }
    return 0;
}