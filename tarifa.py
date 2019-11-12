#can use up to x mb/month
x = int(input())
times = int(input())
sum = 0
nums = []

for i in range(times):
    nums.append(int(input()))

for i in range(len(nums)):
    if nums[i] <= x:
        if i == len(nums)-1:
            sum += (x- nums[i])
            print(sum+x)
        else:
            sum += (x - nums[i])
    if nums[i] > x:
        if i == len(nums)-1:
            sum += (x - nums[i-1])
            print(sum)
        else:
            sum += (nums[i] - x)