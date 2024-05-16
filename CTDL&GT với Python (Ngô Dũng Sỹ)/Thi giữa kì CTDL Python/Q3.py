import math
#-----------------------
def isPrime(n):
    # Write your statements here
    #...
    # End your statements
#end isPrime
#--------------------------
def findLastPrime(a):
    # Write your statements here
    #.....
    #End your statements
#end findLastPrime
# DO NOT ADD NEW OR CHANGE STATEMENTS IN THIS FUNCTION
def inputList(a, n):
    for i in range(n):
        a.append(int(input(f"a[{i}]=")))
# end inputList
#========================DO NOT EDIT GIVEN STATEMENTS IN THE MAIN FUNCTION.============================
#===IF YOU CHANGE, THE GRADING SOFTWARE CAN NOT FIND THE OUTPUT RESULT TO SCORE, THUS THE MARK IS 0.===
def main():
  print("TEST Q3 (2 marks):");
  a = list()
  n = int(input("Enter n = "))
  inputList(a, n)
  result = findLastPrime(a)
  print("OUTPUT:")
  print(f"{result}")
#end main
#--------------------------------
if __name__ == "__main__":
  main()
#============================================================
