import random

def GenerateLotto(numbers):
    lottoResult = []
    while True:
        num = random.randint(1, numbers)
        if (num in lottoResult):
            continue
        elif (len(lottoResult) == 6):
            break
        else:
             lottoResult.append(num)
    lottoResult.sort()
    return lottoResult
               
print(GenerateLotto(10))
