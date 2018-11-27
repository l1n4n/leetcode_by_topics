# 860. Lemonade Change
# At a lemonade stand, each lemonade costs $5.
# Customers are standing in a queue to buy from you, and order one at a time (in the order specified by bills).
# Each customer will only buy one lemonade and pay with either a $5, $10, or $20 bill.  You must provide the correct change to each customer, so that the net transaction is that the customer pays $5.
# Note that you don't have any change in hand at first.
# Return true if and only if you can provide every customer with correct change.

# GREEDY
# ervey time give the biggest change available

class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        if not bills: return True
        # till = [0]*3 no need to record no. of 20s
        till = [0] * 2
        for i in bills:
            if i == 5:
                till[0] += 1
            elif i == 10:
                till[0] -= 1
                till[1] += 1
            elif i == 20:
                if till[1] == 0:
                    till[0] -= 3
                else:
                    till[1] -= 1
                    till[0] -= 1
                # till[2] += 1
            if till[0] < 0 or till[1] < 0:
                return False
        return True
