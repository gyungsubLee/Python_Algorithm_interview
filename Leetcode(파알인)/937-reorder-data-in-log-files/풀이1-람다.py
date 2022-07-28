class Solution:
    def reorderLogFiles(self, logs):
        letters, digits = [], []
        for log in logs:
            print(log.split()[1])
            if log.split()[1].isdigit():
                digits.append(log)
            else:
                letters.append(log)
        letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
        return letters + digits

