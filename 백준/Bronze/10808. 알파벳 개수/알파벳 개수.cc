#include <bits/stdc++.h>
using namespace std;

int a[26];
string s;

int main() {
    getline(cin, s);
    
    for (char c: s) a[c-'a']++;
    for (int i=0; i<26; i++) cout << a[i] << ' ';
    
    return 0;
}