# dic = {
#     "a": 1
#     "b": 2

# print(dic)

# def get_name(user: dict):
#     match user:
#         case {"location": {"city": city, "country": country}}:
#             return f"{city}, {country}"
#         case {"location": location}:
#             return location

# v1 = {"location": "seoul, south korea"}
# v2 = {"location": {
#             "city": "seoul",
#             "country": "south korea"
#         }}
# get_name(user=v1)
# get_name(user=v2)


# def add_all(nums: list):
#     match nums:
#         case []:
#             return 0
#         case [int(head) | float(head), *tail]:
#             return head + add_all(tail)
#         case _:
#             raise ValueError(f"Sorry, only number please")
# add_all(nums=[1, 2, 3, 4, 5])

# def literal_match(lang: str):
#     match lang:
#         case "korean":
#             return "Great!"
#         case "english":
#             return "Very nice!"
#         case _:
#             return "Which language do you speak?"

# literal_match(lang="english")

# l1 = ["a", "b", "c", "d"]
# l2 = [1, 2, 3, 4, 5]

# list(zip(l1, l2, strict=True))

import sys

print(sys.version < "3.9")