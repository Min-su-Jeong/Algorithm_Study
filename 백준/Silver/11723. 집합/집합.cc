#include <bits/stdc++.h>
using namespace std;

int M, num, ret;
char s[11];
int main() {
    scanf("%d", &M);
    for (int i=0; i<M; i++) {
        scanf("%s %d", &s, &num);
        if (s[0] == 'a' && s[1] == 'd') ret |= (1 << num);
        else if (s[0] == 'r') ret &= ~(1 << num);
        else if (s[0] == 'c') printf("%d\n", (ret & (1 << num)) == 0 ? 0 : 1);
        else if (s[0] == 't') ret ^= (1 << num);
        else if (s[0] == 'a' && s[1] == 'l') ret = (1 << 21) - 1;
        else ret = 0;
    }
    return 0;
}