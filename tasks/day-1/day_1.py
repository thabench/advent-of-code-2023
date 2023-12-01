import re
from word2number import w2n
from inputs.input_getter import get_input

response = get_input("https://adventofcode.com/2023/day/1/input")
response = response.split("\n")


# PART ONE
def get_calibration_value_result(input_response):
    calibration_values = []
    for line in input_response:
        num_value = [x for x in line if x.isnumeric()]
        if not num_value:
            continue
        if len(num_value) == 1:
            calibration_values.append(int(num_value[0] * 2))
            continue
        calibration_value = int(num_value[0] + num_value[-1])
        calibration_values.append(calibration_value)

    result = sum(calibration_values)
    return result


print(get_calibration_value_result(response))


# PART TWO

def convert_to_number(text_line):
    if not text_line:
        return 0
    text_line_fw = re.findall(r'(\d|one|two|three|four|five|six|seven|eight|nine)', text_line)
    text_line_bw = re.findall(r'(\d|eno|owt|eerht|ruof|evif|xis|neves|thgie|enin)', text_line[::-1])
    text_line_bw_fixed = [x[::-1] for x in text_line_bw]
    first = w2n.word_to_num(text_line_fw[0])
    last = w2n.word_to_num(text_line_bw_fixed[0])
    return int(str(first) + str(last))


part_two_response = []
for line in response:
    part_two_response.append(convert_to_number(line))

print(sum(part_two_response))
