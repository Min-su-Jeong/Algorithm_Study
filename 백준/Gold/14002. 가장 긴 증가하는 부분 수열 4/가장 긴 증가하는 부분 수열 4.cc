#include <bits/stdc++.h>
using namespace std;

const int MAX = 1004;
int n, idx, ret=1, cnt[MAX], a[MAX], prev_list[MAX];

void go(int idx){
    if(idx == -1) return; 
    go(prev_list[idx]);
    printf("%d ", a[idx]); 
    return;
}

int main(){
    scanf("%d", &n);
    for(int i = 0; i < n; i++){
        scanf("%d", &a[i]);
    }
    
    fill(prev_list, prev_list + MAX, -1);
    fill(cnt, cnt + MAX, 1);
    for(int i = 0; i < n; i++){
        for(int j = 0; j < i; j++){
            if(a[j] < a[i] && cnt[i] < cnt[j] + 1){
                cnt[i] = cnt[j] + 1;
                prev_list[i] = j;
                if(ret < cnt[i]){
                    ret = cnt[i];
                    idx = i;
                }
            }
        }
    }
    printf("%d\n", ret);
    go(idx);

    return 0;
}