Activity -2 :
//function to sort  will use bubble sort algorthim 
def sort (numbers):
  for i in range (len(numbers)):
    for j in range(len(numbers)-1):
        if numbers[j] > numbers[j+1]:
          numbers[j],numbers[j+1]=numbers[j+1],numbers[j]

//function to sort and find median   (pseudocode) 
def sort and find median(numbers):
numbers.sort()
n= len(numbers)
if n% 2==0:
  return(numbers[n//2-1]+number[n//2])/2
else:
  return numbers[n//2]
  
\\test case:
nums=[5,1,6,3]
print("median:",sort and find median(numbers))
