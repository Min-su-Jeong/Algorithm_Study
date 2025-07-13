#include <bits/stdc++.h>
using namespace std;

const int MAX = 68;
int N; 
char a[MAX][MAX];

string quad(int y, int x, int size) {
    if (size == 1) return string(1, a[y][x]);

    char b = a[y][x];
    string ret = "";

    for (int i=y; i<y+size; i++) {
        for (int j=x; j<x+size; j++) {
            if (b != a[i][j]) {
                ret += "(";
                ret += quad(y, x, size/2);
                ret += quad(y, x+size/2, size/2);
                ret += quad(y+size/2, x, size/2);
                ret += quad(y+size/2, x+size/2, size/2);
                ret += ")";
                return ret;
            }
        }
    }
    return string(1, a[y][x]);
}

int main() {
    scanf("%d", &N);
    for (int i=0; i<N; i++) {
        scanf("%s", a[i]);
    }
    cout << quad(0, 0, N) << '\n';

    return 0;
}