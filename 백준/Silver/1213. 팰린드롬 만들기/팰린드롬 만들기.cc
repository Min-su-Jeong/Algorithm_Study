#include <bits/stdc++.h>
using namespace std;

int cnt[200], flag;
string s, ret;
char mid;

int main() {
    ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
    cin >> s;
    for (char c: s) cnt[c]++;

    for (int i='Z'; i>='A'; i--) {
        // 알파벳이 존재할 때
        if (cnt[i]) {
            // 알파벳 개수가 홀수개인 경우
            if (cnt[i] & 1) {
                mid = char(i);
                flag++;
                cnt[i]--;
            }
            // 홀수 개의 알파벳이 2개인 경우 -> 펠린드롬 만들기 불가
            if (flag == 2) break;

            // 나머지는 앞뒤로 글자를 붙여줌
            for (int j=0; j < cnt[i]; j += 2) {
                ret = char(i) + ret;
                ret += char(i);
            }
        }
    }
    // mid가 남아있는 경우 중간에 삽입
    if (mid) ret.insert(ret.begin() + ret.size() / 2, mid);

    // 펜린드롬 생성 가능/불가능에 따른 출력
    if (flag == 2) cout << "I'm Sorry Hansoo\n";
    else cout << ret << "\n";
    
    return 0;
}