import base64
import sys

def x(t): return ''.join([chr(ord(t[i])^[0x66, 0x66, 0x66, 0x13, 0x37, 0x42, 0x69, 0x33, 0x01, 0x13][i%10]) for i in range(len(t))])

b="BRMUfxcqHUdxYFxJSXtYLQJRL3oISS1UACYIB20nWQMQclkmG1p5"

if str(sys.argv[1]) == "e":
	print "@muffiniks #hackvent http://hackvent.hacking-lab.com MUFFIN_BOTNET:"+base64.b64encode(x(sys.argv[2]))+":MUFFIN_BOTNET"
#b="FQ5GPlRiTlZiewlGJVsGLgUTZXoCRhJ7XjFHHTozEgkTcF9iRkdsY0kFDiJbLh5ScnsDFAM0"
#b="ChVGPlYuSU8hcBMUCjMaGjl8UkdGSy40dC0HR2R9EksyakcnUxN1dh4SSWNbIwBdJjNLAkZTGmIBR3VjFVxJPF8tBlhjPQ8ISVh2LA4KcUIC"
#b="FQ5GPlRiTlZiewlGJ2RSMQZeZDMFDgd/WycHVGQyRjIOclkpSUpuZkYmC2ZRJABdaHgVQQ=="
#b="FhECM0tiC1JydlBSRm8XIRxBbTNLDUY+UwJEE2lnEhYVKRhtAVxueARID30YGBthSyUXPwk="
else:
	print x(base64.b64decode(sys.argv[1]))