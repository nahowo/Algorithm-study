int height, multiple;
long long total;
int main()
{
	scanf("%d", &height);
	scanf("%d", &multiple);

	long long num = multiple;

	for (int i = 1; i <= height; i++)
	{
		int temp;
		scanf("%d", &temp);

		
		total += (long long)(num * temp);

		total = total % 1000000007;

		num = (num * multiple) % 1000000007;

	}

	printf("%lld", total);

	return 0;
}