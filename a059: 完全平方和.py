n = int(input())           
for i in range(n):
  a = int(input())          
  b = int(input())          
  result = []               
  for j in range(a, b+1):   
    j2 = j**0.5 * 100      
    if j2%100==0:           
      result.append(j)      
  print(f'Case {i+1}: {sum(result)}')
