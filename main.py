
def nchoosek(nums, k):
  result = [] # possible choices
  def helper(i, slate):
    if len(slate) == k:
      result.append(slate.copy())
      return
    if i > len(slate) - 1:
      return
    # include
    slate.append(nums[i])
    helper(i + 1, slate)
    slate.pop()
    # exclude
    helper(i + 1, slate)

  helper(0, [])
  return result