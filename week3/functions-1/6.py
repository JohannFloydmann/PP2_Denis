def reverseSent(st):
    ls = st.split()
    ls = ls[::-1]
    return " ".join(ls)

print(reverseSent(input("Enter the sentece: ")))