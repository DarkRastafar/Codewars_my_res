def order(sentence):
  if sentence == "":
    return sentence
  else:
    arr = sentence.split()
    for i in range(len(arr) - 1):
      for j in range(0, len(arr) - i - 1):
        if get_digit(arr[j]) > get_digit(arr[j + 1]):
          arr[j], arr[j + 1] = arr[j + 1], arr[j] 


    return " ".join(arr)

def get_digit(word):
  for num in word:
    if num.isdigit():
      return num





print(order("is2 Thi1s T4est 3a"), "Thi1s is2 3a T4est")
print(order("4of Fo1r pe6ople g3ood th5e the2"), "Fo1r the2 g3ood 4of th5e pe6ople")
print(order(""), "")