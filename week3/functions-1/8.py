def spy_game(nums):
    st = "".join([str(x) for x in nums])
    if st.find("007") != -1:
        return True
    return False

print(spy_game([0, 0, 7, 1, 2]))
print(spy_game([0, 0, 1, 7, 2]))