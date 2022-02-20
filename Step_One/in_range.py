def in_range(nums, lowest, highest):
    """Print numbers inside range.

    - nums: list of numbers
    - lowest: lowest number to print
    - highest: highest number to print

    For example:

      in_range([10, 20, 30, 40], 15, 30)

    should print:

      20 fits
      30 fits
    """

    # YOUR CODE HERE
    lowest_fit = False
    highest_fit = False
    for num in nums:
      if num <= lowest:
        lowest_fit = True
      if num >= highest:
        highest_fit = True
    if lowest_fit:
      print(f"{lowest} fits")
    if highest_fit:
      print(f"{highest} fits")

in_range([10, 20, 30, 40, 50], 15, 30)            
