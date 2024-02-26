def permute(nums):
    if len(nums) == 1:
        return [nums]  
    else:
        permutations = []
        for i in range(len(nums)):
            current_num = nums[i]
            remaining_nums = nums[:i] + nums[i+1:] 
            for perm in permute(remaining_nums):
                permutations.append([current_num] + perm) 
        return permutations 
input_list = [1, 2, 3]
print("Input list:", input_list)
print("Permutations:", permute(input_list))
