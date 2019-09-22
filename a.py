cat_list = ["aaa", 123 ,"bbb", "ccc"]

def cat_string(cat_list: list):
    ans = ""
    for cat in cat_list:
        if isinstance(cat, str):
            ans += cat
    return ans

print(cat_string(cat_list))
