class Solution:
    def day_of_week(self, s, k):
        week = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
        mp = {}
        for i, d in enumerate(week):
            mp[d] = i
        return week[(mp[s] + k) % 7]
