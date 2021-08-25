#!/usr/bin/env python3
loop = 0
while (loop < 10):
	noun = input("Choose a noun: ")
	plural_noun = input("Choose a plural noun: ")
	noun2 = input("Choose another noun: ")
	place = input("Name a proper noun(location): ")
	adjective = input("Choose an adjective: ")
	noun3 = input("Give one more noun please: ")
	print("Sup, you stupid {}!".format(noun))
	print("What did you do with my {}?".format(plural_noun))
	print("So you think you can just get away with this? You must think I'm dumber than a {}.".format(noun2))
	print("Why don't you go back to",place,"just like your {} {}!".format(adjective, noun3))
	loop += 1