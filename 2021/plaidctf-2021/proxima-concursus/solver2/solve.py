from braindead import *
log.enable()

ans = '''
696e666c61746f6e9e878022e2dab2af81774645ab547f3f10315663afa8d1922a5e8fa0d8fe0fd5
7461755f5f5f5f5f940b4126b9090a2e63769cb72a7e2e6e10315663afa8d1922a5e8fa0d8fe0fd5
5a626f736f6e5f5f28ab158e2ce563e5d3dc5ae75d8c4b48b36710aacc2ac18e8db6b5b071a533e4
57626f736f6e5f5f7fdfcacf37d1265e21773c300d133c81b36710aacc2ac18e8db6b5b071a533e4
'''.split()

r = io.connect(('proxima.pwni.ng', 1337))

io.interactive(r)
