import matplotlib.pyplot as plt

f = open("data.txt", "r")
lines = f.readlines()
tmp_arr = []
hum_arr = []
count_arr = []
for msg in lines:
    msg = msg.split(',')
    tmp_arr.append(float(msg[0]))
    hum_arr.append(float(msg[1]))
    count_arr.append(int(msg[2][:-1]))

print(tmp_arr)
print(hum_arr)
print(count_arr)
print(len(count_arr))
plt.figure(1)
plt.plot(count_arr, tmp_arr, label = "Temperature in Celsius")
plt.title("Temperature in Celsius")
plt.figure(2)
plt.plot(count_arr, hum_arr, label = "")
plt.title("Relative Humidity")
plt.show()
