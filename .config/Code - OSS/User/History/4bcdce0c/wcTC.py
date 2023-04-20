

# IF ... ELSE
def age_of_majority(country):
    if country == "USA":
        res = 21
    else:
        res = 18
    return res


# MATCH ... CASE
print(age_of_majority("USAA"))


# def age_of_majority(country):
#     match country:
#         case "USA":
#             res = 21
#         case _:
#             res = 18
#     return res


# print(age_of_majority("USA"))