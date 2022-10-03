"""nested list python hr"""

"""method 1"""

# Result=[]
# scorelist=[]

# if __name__ == '__main__':
#     for _ in range(int(input())):
#         name = input()
#         score = float(input())
#         Result+=[[name,score]]
#         scorelist+=[score]
#     b=sorted(list(set(scorelist)))[1] 
#     for a,c in sorted(Result):
#         if c==b:
#             print(a)


"""method 2"""


# if __name__ == '__main__':
#     L=[]
#     n=int(input())
#     for _ in range(n):
#         name = input()
#         score = float(input())
#         L.append([name,score])
#     k=[]
#     for i in range(n):
#         k.append(L[i][1])
#     k.sort()
        
#     i=1
#     while i<n and k[0]==k[i]:
#         i=i+1
#     m=k[i]
#     s=[]
#     for j in range(n):
#         if L[j][1]==m:
#             s.append(L[j][0])
#     s.sort()
#     for z in range(len(s)):
#      print(s[z])


