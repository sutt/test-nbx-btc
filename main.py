from script import Script

# Exercise 3
# s = Script([81, 0x76, 0x76, 0x95, 0x93, 0x56, 0x87])
# s.evaluate(0)

# Exercise 4
script_pubkey = Script([0x6e, 0x87, 0x91, 0x69, 0xa7, 0x7c, 0xa7, 0x87])
print(script_pubkey)
# OP_2DUP 
# OP_EQUAL 
# OP_NOT 
# OP_VERIFY 
# OP_SHA1 
# OP_SWAP 
# OP_SHA1 
# OP_EQUAL
script_sig = Script([81, 82])  # FILL THIS IN
combined_script = script_sig + script_pubkey
ret = combined_script.evaluate(0)
print(ret)