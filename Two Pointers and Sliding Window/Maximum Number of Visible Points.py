import math

class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        x0, y0 = location
        angles = []
        same_location_count = 0

        for x, y in points:
            if x == x0 and y == y0:
                same_location_count += 1
            else:
                angle_deg = math.degrees(math.atan2(y - y0, x - x0))
                angles.append(angle_deg)

        angles.sort()

        # Handle circular nature by adding angles + 360
        angles += [a + 360 for a in angles]

        max_visible = 0
        left = 0

        # Sliding window to find the maximum number of points within the angle
        for right in range(len(angles)):
            # Adjust the window so that the difference between angles is within the view angle
            while right < len(angles) and angles[right] - angles[left] > angle:
                left += 1
            max_visible = max(max_visible, right - left + 1)

        return max_visible + same_location_count