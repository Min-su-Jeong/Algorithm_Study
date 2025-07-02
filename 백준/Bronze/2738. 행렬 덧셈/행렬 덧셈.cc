#include <iostream>

using namespace std;

const int MAX = 101;
int n, m;
int arr1[MAX][MAX], arr2[MAX][MAX];

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    
	cin >> n >> m;
	for (int i = 0; i < n; i++) 
		for (int k = 0; k < m; k++) 
			cin >> arr1[i][k];

	for (int i = 0; i < n; i++) 
		for (int k = 0; k < m; k++) 
			cin >> arr2[i][k];

	for (int i = 0; i < n; i++) {
		for (int k = 0; k < m; k++) 
			cout << arr1[i][k] + arr2[i][k] << ' ';
		cout << '\n';
	}
	return 0;
}