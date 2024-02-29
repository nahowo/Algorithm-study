#include <iostream>
#include <algorithm>
using namespace std;

int mx[202020] = { 0 }, arr[202020] = { 0 };
int main(void)
{
    ios_base::sync_with_stdio(false); cin.tie(NULL);
    int N, i, first = 0, second = 0, now;

    cin >> N;
    for (i = 1; i <= N + 2; i++) //맨 마지막 스위치까지 고려해주기
    {
        mx[i] = -2e9;
        if (i <= N) cin >> arr[i];
        else arr[i] = 0;
        if (i >= 3) mx[i] = max(mx[i], mx[i - 3] + (arr[i - 2] + arr[i - 1] + arr[i]) * 2); //두배
        mx[i] = max(mx[i], mx[i - 1] + arr[i]);
    }

    cout << mx[N + 2];
}