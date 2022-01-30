from subprocess import check_output
from re import findall


def get_temp():
    temp = check_output(["vcgencmd", "measure_temp"]).decode()
    temp = float(findall('\d+\.\d+', temp)[0])
    return(temp)


print("CPU Temp:" + str(get_temp()) + " ºC")
