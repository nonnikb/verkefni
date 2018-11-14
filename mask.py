number = 0x6f73
#0110 1111 0111 0011
#0111 1000 0000 0000
#0000 0000 0001 1000
#taka 11-14 fyrir númer á spurningu
#3-4 fyrir svarið
question_mask = number & 0x7800

answer_mask = number & 0x0018

question_number = question_mask >> 0xB

answer = answer_mask >> 3

print(question_number)
print(answer)