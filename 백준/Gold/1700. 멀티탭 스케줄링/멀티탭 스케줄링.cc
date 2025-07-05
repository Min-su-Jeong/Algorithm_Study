#include <bits/stdc++.h>
using namespace std;

const int MAX = 104;
const int INF = INT_MAX;
int N, K, a[MAX], ret;
bool visited[MAX];
vector<int> v;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    cin >> N >> K;
    for (int i=0; i<K; i++) cin >> a[i];
    for (int i=0; i<K; i++) {
        if (!visited[a[i]]) {
            if (v.size() == N) {
                int lastIdx = 0, pos;
                for (int _a: v) {
                    int hereIdx = INF;
                    for (int j=i+1; j<K; j++) {
                        if (_a == a[j]) {
                            hereIdx = j;
                            break;
                        }
                    }
                    if (lastIdx < hereIdx) {
                        lastIdx = hereIdx;
                        pos = _a;
                    }
                }
                visited[pos] = 0;
                ret++;
                v.erase(find(v.begin(), v.end(), pos));
            }
            v.push_back(a[i]);
            visited[a[i]] = 1;
        }
    }
    cout << ret << '\n';
    return 0;
}