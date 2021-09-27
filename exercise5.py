from statistics import mean, median, mode

list_integre = [int(i) for i in input("Give me integers separated by comma?").split(",")]
print(f"Sum: {sum(list_integre)}")
print(f"Mean: {mean(list_integre)}")
print(f"Median: {median(list_integre)}")
print(f"Mode: {mode(list_integre)}")
