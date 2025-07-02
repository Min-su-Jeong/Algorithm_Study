#include <bits/stdc++.h>
using namespace std;

string s, bomb, ret;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    cin >> s >> bomb;
    for (char c: s) {
        ret += c;
        if (ret.size() >= bomb.size() && ret.substr(ret.size() - bomb.size(), bomb.size()) == bomb) {
            ret.erase(ret.end() - bomb.size(), ret.end());
        }
    }
    if (ret.size()) cout << ret << '\n';
    else cout << "FRULA\n";

    return 0;
}