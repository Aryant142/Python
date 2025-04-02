i=1
while i<=3 :
    j=1
    while j <=3 :
        print ( 2  , end= " ")
        j+=1
    print()
    i+=1 

#  output

# 2 2 2 
# 2 2 2 
# 2 2 2 


# a = 1
# while a <= 3:
#     for j in range(1, a + 1):
#         print(j, end='')
#     print()  # This line should be indented at the same level as the for-loop
#     a += 1

# output
# 1
# 12
# 123

# a = 3
# while a > 0:
#     for j in range(1, a + 1):
#         print(j, end='')
#     print()  # This should be aligned with the for loop
#     a -= 1

# output
# 123
# 12
# 1     

    
# i = 5
# num = 65
# while i >= 1:
#     j = 1
#     while j <= i:
#         print(chr(num), end="")
#         num += 1
#         j += 1
#     print()  # Moves to the next line after the inner loop finishes
#     i -= 1  # Decrease i after each full row is printed

# output
# ABCDE
# FGHIJ
# KLMNO
# PQRST
# UVWXY

# num=65
# for i in range(1, 4 + 1):
#     for j in range(i):
#         print(chr(num), end="")
#         num+= 1
#     print()


#output
# A
# BC 
# DEF
# GHIJ

# for i in range(1,5):
#     for j in range (1,8):
#         if  j >= 5-i and j <= 3+i:
#             print("*",end=' ')
#         else :
#             print(" ",end =' ')             
#     print()
            
                    
#  output
        
#        *       
#      * * *     
#    * * * * *               
#  * * * * * * *       
    
# for i in range(1,5):
#     for j in range (1,8):
#         if  j >=i  and j <= 8-i :
#             print("*",end=' ')
#         else :
#             print(" ",end =' ')             
#     print()
            
 
#  output 

# * * * * * * * 
#   * * * * *   
#     * * *     
#       *     

# for i in range(1,5):                                                               
#     for j in range (1,8):
#         if  j >= 5-i and j <= 3+i:
#             print(j,end=' ')
#         else :
#             print(" ",end =' ')             
#     print()    
    
#  output   
#       4       
#     3 4 5     
#   2 3 4 5 6   
# 1 2 3 4 5 6 7 


# for i in range(1,5):                                                               
#     for j in range (1,8):
#         if  j <= 5-i or j >= 3+i:
#             print("*",end=' ')
#         else :
#             print(" ",end =' ')             
#     print()        
    
# output    
    
# * * * * * * * 
# * * *   * * * 
# * *       * * 
# *           * 