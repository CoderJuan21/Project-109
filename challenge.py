import csv
import pandas as pd
import statistics
import plotly.figure_factory as ff
import plotly.graph_objects as go

df = pd.read_csv("data2.csv")
score = df["Score"].tolist()

score_mean = statistics.mean(score)
score_median = statistics.median(score)
score_mode = statistics.mode(score)
score_sd = statistics.stdev(score)

#print("mean,median,mode and standard deviation is {}, {}, {} and {}".format(score_mean, score_median, score_mode, score_sd))

score_first_sd_start, score_first_sd_end = score_mean - score_sd, score_mean + score_sd
score_second_sd_start, score_second_sd_end = score_mean -(2* score_sd), score_mean +(2* score_sd)
score_third_sd_start, score_third__sd_end = score_mean - (3* score_sd), score_mean +(3* score_sd)

score_list_of_data_within_one_sd = [result for result in score if result > score_first_sd_start and result < score_first_sd_end]
score_list_of_data_within_two_sd = [result for result in score if result > score_second_sd_start and result < score_second_sd_end]
score_list_of_data_within_three_sd = [result for result in score if result > score_third_sd_start and result < score_third__sd_end]

print("{}% of data for score lies within one standard deviation ".format(len(score_list_of_data_within_one_sd)*100.0/len(score)))
print("{}% of data for score lies within second standard deviation ".format(len(score_list_of_data_within_two_sd)*100.0/len(score)))
print("{}% of data for score lies within third standard deviation ".format(len(score_list_of_data_within_three_sd)*100.0/len(score)))

fig = ff.create_distplot([score], ["result"], show_hist= False)
fig.add_trace(go.Scatter(x = [score_mean, score_mean], y = [0,0.17], mode = "lines", name = "mean"))
fig.add_trace(go.Scatter(x = [score_first_sd_start, score_first_sd_start], y = [0,0.17], mode = "lines", name = "standard deviation 1"))
fig.add_trace(go.Scatter(x = [score_second_sd_start, score_second_sd_start], y = [0,0.17], mode = "lines", name = "standard deviation 2"))
fig.add_trace(go.Scatter(x = [score_third_sd_start, score_third_sd_start], y = [0,0.17], mode = "lines", name = "standard deviation 3"))
fig.show()