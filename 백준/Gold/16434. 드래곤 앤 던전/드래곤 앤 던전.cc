#include <bits/stdc++.h>
using namespace std; 
typedef long long ll;

const int MAX = 130004;
ll n, attack, t[MAX], a[MAX], h[MAX], l, r, ret;

bool check(ll mid) {
	ll mxHP = mid;
	ll init_attack = attack;
	for(int i = 0; i < n; i++){
		if(t[i] == 2) {
			mid = min(mxHP, mid + h[i]);
			init_attack += a[i];
		} else {
			ll cnt = h[i] / init_attack + (h[i] % init_attack ? 1 : 0); 
			mid -= (cnt - 1) * a[i];
		}   
		if(mid <= 0) return false;
	}
	return true; 
}

int main(){ 
	ios::sync_with_stdio(false);
	cin.tie(NULL); cout.tie(NULL);

	cin >> n >> attack;
	for(int i = 0; i < n; i++){
		cin >> t[i] >> a[i] >> h[i]; 
	} 

	l = 1, r = 1e18 + 4; 
	while(l <= r){
		ll mid = (l + r) / 2; 
		if(check(mid)){
			r = mid - 1; 
			ret = mid;
		} else l = mid + 1; 
	}
    cout << ret << '\n';

	return 0;
}