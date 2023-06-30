# A Denontration of List operations sort, pop and for loops

perfumes = ["Eros", "Ysl Y", "Tom ford oud", "Intense Man"]
message = f"""My priority perfumes are {perfumes[0]}, then {perfumes[3]}.
{perfumes[1]} would be nice and {perfumes[2]} would be a bonus"""
print(message)
perfumes.insert(2, 'Stronger with you')
print()
print(f"{perfumes[0]} has a fresh and senual vibe")
print(f"{perfumes[3]} is strong initially but becomes fruity and sweet")
print(f"{perfumes[1]} is a mystery but i'll check it out")
print(f"{perfumes[2]} has a deep woody scent. It's dark and bold")

# perfumes.append('Stronger with you')
# perfumes.insert(2, 'Stronger with you')

print(f"{perfumes[4]} is sweet warm and comforting")

print(f"\n", perfumes)
# print(perfumes.pop(-3))
# print(perfumes)
# perfumes.sort()
# print(perfumes)
print(sorted(perfumes))
print(len(perfumes))

print()
for perfume in perfumes:
    print(perfume)

print()
for perfume_num in range(len(perfumes)):
    print(perfume_num)
