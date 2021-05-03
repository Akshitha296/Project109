import pandas as pd
import statistics
import csv

df = pd.read_csv("StudentsPerformance.csv")
math_list = df["math score"].to_list()
reading_list = df["reading score"].to_list()
writing_list = df["writing score"].to_list()

math_mean = statistics.mean(math_list)
math_median = statistics.median(math_list)
math_mode = statistics.mode(math_list)

print("Mean, Median, Mode for math is ", math_mean, math_median, math_mode)

reading_mean = statistics.mean(reading_list)
reading_median = statistics.median(reading_list)
reading_mode = statistics.mode(reading_list)

print("Mean, Median, Mode for reading is ", reading_mean, reading_median, reading_mode)

writing_mean = statistics.mean(reading_list)
writing_median = statistics.median(reading_list)
writing_mode = statistics.mode(reading_list)

print("Mean, Median, Mode for writing is ", reading_mean, reading_median, reading_mode)

math_sd = statistics.stdev(math_list)
reading_sd = statistics.stdev(reading_list)
writing_sd = statistics.stdev(reading_list)

print("Math SD is ", math_sd)
print("Reading SD is ", reading_sd)
print("Writing SD is ", reading_sd)

math_first_sd_start = math_mean - math_sd
math_first_sd_end = math_mean + math_sd

math_second_sd_start = math_mean-(math_sd*2)
math_second_sd_end = math_mean+(math_sd*2)

math_third_sd_start = math_mean-(math_sd*3)
math_third_sd_end = math_mean+(math_sd*3)

math_data_within_first_sd = [result for result in math_list if result>math_first_sd_start and result<math_first_sd_end]
math_data_within_second_sd = [result for result in math_list if result>math_second_sd_start and result<math_second_sd_end]
math_data_within_third_sd = [result for result in math_list if result>math_third_sd_start and result<math_third_sd_end]

percentage_math_1 = len(math_data_within_first_sd)*100/len(math_list)
percentage_math_2 = len(math_data_within_second_sd)*100/len(math_list)
percentage_math_3 = len(math_data_within_third_sd)*100/len(math_list)

print("Percentage of math data within 1st sd is ", percentage_math_1)
print("Percentage of math data within 2nd sd is ", percentage_math_2)
print("Percentage of math data within 3st sd is ", percentage_math_3)

reading_first_sd_start = reading_mean - reading_sd
reading_first_sd_end = reading_mean + reading_sd

reading_second_sd_start = reading_mean-(reading_sd*2)
reading_second_sd_end = reading_mean+(reading_sd*2)

reading_third_sd_start = reading_mean-(reading_sd*3)
reading_third_sd_end = reading_mean+(reading_sd*3)

reading_data_within_first_sd = [result for result in reading_list if result>reading_first_sd_start and result<reading_first_sd_end]
reading_data_within_second_sd = [result for result in reading_list if result>reading_second_sd_start and result<reading_second_sd_end]
reading_data_within_third_sd = [result for result in reading_list if result>reading_third_sd_start and result<reading_third_sd_end]

percentage_reading_1 = len(reading_data_within_first_sd)*100/len(reading_list)
percentage_reading_2 = len(reading_data_within_second_sd)*100/len(reading_list)
percentage_reading_3 = len(reading_data_within_third_sd)*100/len(reading_list)

print("Percentage of reading data within 1st sd is ", percentage_reading_1)
print("Percentage of reading data within 2nd sd is ", percentage_reading_2)
print("Percentage of reading data within 3st sd is ", percentage_reading_3)

writing_first_sd_start = writing_mean - writing_sd
writing_first_sd_end = writing_mean + writing_sd

writing_second_sd_start = writing_mean-(writing_sd*2)
writing_second_sd_end = writing_mean+(writing_sd*2)

writing_third_sd_start = writing_mean-(writing_sd*3)
writing_third_sd_end = writing_mean+(writing_sd*3)

writing_data_within_first_sd = [result for result in writing_list if result>writing_first_sd_start and result<writing_first_sd_end]
writing_data_within_second_sd = [result for result in writing_list if result>writing_second_sd_start and result<writing_second_sd_end]
writing_data_within_third_sd = [result for result in writing_list if result>writing_third_sd_start and result<writing_third_sd_end]

percentage_writing_1 = len(writing_data_within_first_sd)*100/len(writing_list)
percentage_writing_2 = len(writing_data_within_second_sd)*100/len(writing_list)
percentage_writing_3 = len(writing_data_within_third_sd)*100/len(writing_list)

print("Percentage of writing data within 1st sd is ", percentage_writing_1)
print("Percentage of writing data within 2nd sd is ", percentage_writing_2)
print("Percentage of writing data within 3st sd is ", percentage_writing_3)