from speedtest import Speedtest
st = Speedtest()
print("your connection's download speed is:", st.download())
print ("your connection's upload speed is:", st.upload())