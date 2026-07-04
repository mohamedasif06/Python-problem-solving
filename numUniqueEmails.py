class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        valid = set()
        for i in emails:
            local,domain = i.split("@")#->split('@') divides the email into two parts. The part before @ is assigned to local, and the part after @ is assigned to domain.
            local = local.split('+')[0]#-> This will spit the string by '+' and assigns the list's 1st element to local
            local = local.replace('.',"")#-> This will remove the '.'
            new_email = local+'@'+domain
            valid.add(new_email)#-> Adding the element to a set.
        return len(valid) #-> Total number of valid emails.
