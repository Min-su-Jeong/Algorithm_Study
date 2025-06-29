#include <bits/stdc++.h>
using namespace std;

const int MAX = 104;
int T, n, x, a[MAX];
string p, order;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    cin >> T;
    while(T--) {
        deque<int> q;
        cin >> p >> n >> order;
        x = 0;
        
        for (char c: order) {
            if (c == '[' || c == ']') continue;
            if ('0' <= c && c <= '9') x = x * 10 + c - '0';
            else {
                if (x > 0) q.push_back(x);
                x = 0;
            }
        }
        if (x > 0) q.push_back(x);

        bool error = false, rev = false;
        for (char c: p) {
            if (c == 'R') rev = !rev;
            else {
                if (q.empty()) {
                    error = true;
                    break;
                }
                if (rev) q.pop_back();
                else q.pop_front();
            } 
        }
        if (error) cout << "error" << '\n';
        else {
            cout << '[';
            if (rev) reverse(q.begin(), q.end());
            for (int i=0; i<q.size(); i++) {
                cout << q[i];
                if (i < q.size()-1) cout << ',';
            }
            cout << "]\n";
        }
    }
    return 0;
}