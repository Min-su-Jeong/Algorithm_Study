#include <bits/stdc++.h>
using namespace std;

int idx;
string s;
vector<string> v = { "c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z=" };

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    cin >> s;
    for(int i = 0; i < v.size(); i++)
    {
        while(true) {
            idx = s.find(v[i]);
            if(idx == string::npos) break;
            s.replace(idx, v[i].length(), "_");
        }
    }
    cout << s.length();
}