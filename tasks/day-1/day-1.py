from inputs.input_getter import get_input

adv_input = get_input("https://adventofcode.com/2022/day/1/input")
adv_list = adv_input.replace("\n", " ").split("  ")

summed_elf_list = []

for elf in adv_list:
    one_elf = elf.split(" ")
    one_elf_sum = sum([int(calorie) for calorie in one_elf if calorie])
    summed_elf_list.append(one_elf_sum)

max_elf = max(summed_elf_list)
print(f"ELF WITH HIGHEST CALLORIES: {max_elf}")

summed_elf_list.sort()

two_after_max_elf = summed_elf_list[-3:-1]
top_three = sum(two_after_max_elf) + max_elf
print(f"SUM OF TOP 3 ELVES: {top_three}")
