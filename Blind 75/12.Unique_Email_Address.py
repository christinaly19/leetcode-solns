# Question 929 Unique Email Addresses
class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        emailsMap = {}
        count = 0
        for email in emails:
            atIndex = email.find("@")
            firstPart = email[:atIndex + 1]
            lastPart = email[atIndex + 1:]
            if '+' in firstPart:
                ignoreIndex = email.find("+")
                firstPart = firstPart[:ignoreIndex]
                firstPart = firstPart + "@"
            if '.' in firstPart:
                firstPart = firstPart.replace('.', '')
            cleanedEmail = firstPart + lastPart
            print(cleanedEmail)
            if cleanedEmail in emailsMap:
                continue 
            else: 
                emailsMap[cleanedEmail] = 1
                count = count + 1
        return count
