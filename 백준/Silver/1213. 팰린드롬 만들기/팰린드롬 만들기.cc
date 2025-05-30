#include <bits/stdc++.h>
using namespace std;

int a[200], flag;
char mid;
string s, ret;
map<char, int> mp;

int main() {
    ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

    cin >> s;
    for (char c: s) a[c]++;

    for (int i='Z'; i>='A'; i--) {
        // 알파벳이 존재할 때
        if (a[i]) {
            // 알파벳이 홀수일 때
            if (a[i] & 1) {
                mid = char(i);
                flag++;
                a[i]--;
            }
            // 홀수 개의 알파벳이 2개인 경우 -> 펠린드롬 만들기 불가
            if (flag == 2) break;

            // 나머지는 양쪽으로 문자 붙여주기
            for (int j=0; j<a[i]; j+=2) {
                ret = char(i) + ret + char(i);
            }
        }
    }
    // mid가 있는 경우, 남은 문자 삽입
    if (mid) ret.insert(ret.begin() + ret.size() / 2, mid);

    if (flag != 2) cout << ret << '\n';
    else cout << "I'm Sorry Hansoo" << '\n';
    
    return 0;
}