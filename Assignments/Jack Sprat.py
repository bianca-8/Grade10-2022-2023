def level2(number):
    #add your level 2 code here
    for i in range(1,number+1):
      if number % i == 0:
        print(i)

def level2Plus(number):
    #add your level 2+ code here
    sum = 0
  
    for i in range(1,number+1):
      if number % i == 0:
        sum += i
    return sum

def level3(number):
    #add your level 3 code here
    sum = 0
  
    for i in range(1,number+1):
      if number % i == 0:
        sum += i

    if sum == number + 1:
      return "Lean"
    elif sum >= 3 * number:
      return "Fat"
    else:
      return "Neither"

def level4(number):
    #add your level 4 code here
    sum = 0
    sum2 = 0
  
    for i in range(1,number+1):
      if number % i == 0:
        sum += i
    
    for j in range(1,number+2):
      if (number+1) % j == 0:
        sum2 += j

    if sum == j and sum2 > 3 * j:
      return "Jack Sprat"
    else:
      return "Not"

def level4Plus():
    #add your level 4+ compile
    sum = 0
    sum2 = 0
    answer = ""
    answer2 = ""
  
    for i in range(1,1001):
      for j in range(1,i+1):
        if i % j == 0:
          sum += j
          if sum == i + 1:
            answer = answer + " " + str(i) + " "
      sum = 0
      
    for k in range(2,1002):
      for l in range(1,k+1):
        if k % l == 0:
          sum2 += l
          if sum2 > 3 * k:
            if answer.count(str(k-1) + " ") == 1:
              answer2 = answer2 + " " + str(k-1)
      sum2 = 0
              
    return answer2[1:]

#add input here
number = 15
#add function calls here to test the number inputted
level2(number)
level2Plus(number)
level3(number)
level4(number)
level4Plus()
