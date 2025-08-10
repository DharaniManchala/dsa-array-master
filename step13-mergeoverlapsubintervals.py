def merge_intervals(intervals):
    if not intervals:
        return []
    
    # Step 1: Sort intervals by start time
    intervals.sort(key=lambda x: x[0])
    
    merged = []
    for interval in intervals:
        # If no overlap, add the interval
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            # Overlap case: update the end time
            merged[-1][1] = max(merged[-1][1], interval[1])
    
    return merged


# Example usage
intervals = [[1,3],[2,6],[8,10],[15,18]]
print(merge_intervals(intervals))  # Output: [[1,6],[8,10],[15,18]]
