class Solution:
    # string approach
    # def isPalindrome(self, x: int) -> bool:
    #     num_str = str(x)
    #     num_list = list(num_str)
    #     num_list.reverse()
    #     num_list = ''.join(num_list)
    #     if num_str == num_list:
    #         return True
    #     else:
    #         return False

    # reverse the number approach
    # def isPalindrome(self,x:int)->bool:
    #     if x<0:
    #         return False
    #     orginal_num = x
    #     reverse_num = 0
    #     while x>0:
    #         last_digit = x % 10
    #         reverse_num = reverse_num*10+last_digit
    #         x//=10
    #     return orginal_num==reverse_num

    # reverse half approach
        def isPalindrome(self,x:int)->bool:
            # any number ending in 0 cannot be a palindrome unless it is 0 like 10- > 01
            if x<0 or (x!=0 and x%10==0):
                return False    
            reverse_half = 0
            while x>reverse_half:
                digit = x % 10
                reverse_half = reverse_half *10+digit
                x = x //10
            return x == reverse_half or x == reverse_half//10