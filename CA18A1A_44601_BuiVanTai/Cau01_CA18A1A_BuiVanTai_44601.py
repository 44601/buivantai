"""
Đề thi 02
Bui Van Tai
Date: 30/10/2021


"""
a = input("Nhập một số nhị phân : ")
b = [int(i) for  i in a]
b  = b[::-1]
c = []
for i in range(len(b)):
    c.append(b[i]*(2**i))
sum_c = sum(c)
print("Số Thập phân : ",sum_c)
