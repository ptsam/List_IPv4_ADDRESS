def find_ipaddr(A):
  octets = []
  addr = []
  octet = []
  for k in range(1,4):
    if len(A[:k]) > 1 and  A[:k][0] == '0':
      continue
    else:
      oct1 = int(A[:k])
      temp2 = A[k:]
      oct2 = ''
      for k2 in range(1,4):
         if len(temp2[:k2]) > 1 and  temp2[:k2][0] == '0':
           continue
         else:
           oct2 = int(temp2[:k2])
           temp3 = temp2[k2:]
           oct3 = ''
           if len(temp3) > 1:
             for k3 in range(1,4):
               if len(temp3[:k3]) > 1 and  temp3[:k3][0] == '0':
                  continue
               else:
                  oct3 = int(temp3[:k3])
                  temp4 = temp3[k3:]
                  if len(temp4) <= 3 and len(temp4) > 0:
                    if oct1 <= 255 and oct2 <= 255 and \
                       oct3 <= 255 and int(temp4) <= 255:
                         if (len(temp4) > 1 and temp4[0] != '0') or len(temp4) == 1:
                           addr.append('.'.join([str(oct1),str(oct2),str(oct3),str(int(temp4))])) 
                           octets.append(addr)
  return list(set(addr))


A = input("Enter ip string:")
ip_addr = find_ipaddr(A)
print("Possible IP addresses from string '%s' " % A)
print(ip_addr)

