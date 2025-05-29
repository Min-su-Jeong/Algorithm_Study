#include <bits/stdc++.h>
using namespace std;
#define prev p

int N, T, A, B, asum, bsum;
string s, prev;

string print(int a) {
    string m = "00" + to_string(a / 60);
    string s = "00" + to_string(a % 60);
    return m.substr(m.size()-2, 2) + ":" + s.substr(s.size()-2, 2);
}

int changeToInt(string s) {
    return atoi(s.substr(0, 2).c_str()) * 60 + atoi(s.substr(3, 2).c_str());
}

void go(int &sum, string s) {
    sum += (changeToInt(s) - changeToInt(prev));
}

int main() {
    ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

    cin >> N;
    for (int i=0; i<N; i++) {
        cin >> T >> s;
    
        if (A > B) go(asum, s);
        else if (A < B) go(bsum, s);
        
        T == 1 ? A++ : B++;
        prev = s; 
    }
    if (A > B) go(asum, "48:00");
    else if (A < B) go(bsum, "48:00");

    cout << print(asum) << '\n';
    cout << print(bsum) << '\n';
    return 0;
}