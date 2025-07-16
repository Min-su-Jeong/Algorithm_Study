#include <bits/stdc++.h>
using namespace std;

int k;
char a[20];
bool visited[10];
vector<string> ret;

bool check(char x, char y, char op) {
	if (x < y && op == '<') return true;
	if (x > y && op == '>') return true;
	return false;
}

void go(int depth, string num) {
	if (depth == k+1) {
		ret.push_back(num);
		return;
	}

	for (int i=0; i<10; i++) {
		if (visited[i]) continue;
		if (depth == 0 || check(num[depth-1], i+'0', a[depth-1])) {
			visited[i] = 1;
			go(depth+1, num + to_string(i));
			visited[i] = 0;
		}
	}
	return;
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL); cout.tie(NULL);

	cin >> k;
	for (int i=0; i<k; i++) cin >> a[i];

	go(0, "");
	sort(ret.begin(), ret.end());

	cout << ret[ret.size()-1] << '\n' << ret[0] << '\n';
	return 0;
}