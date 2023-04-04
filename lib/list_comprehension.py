#!/usr/bin/env python3
import ipdb

def return_evens(num_list):
    even_nums = [n for n in num_list if n % 2 == 0]
    return even_nums


def make_exclamation(sentence_list):
    excited = [sentence_list[n]+"!" for n in range(0,len(sentence_list))]
    return excited