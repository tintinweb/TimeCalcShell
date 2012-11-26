#! /usr/bin/env python
# vim:ts=4:sw=4:expandtab
'''
Created on Aug 3, 2012

@author: tintinweb
'''
import time, datetime
import re

DEBUG=False

def interactive():
    data = ""
    tlast=time.time()
    while not data=="exit":
        tdelta=time.time()-tlast
        data=raw_input("+%0.3fs #>"%(tdelta))
        # do not allow \n OR " "* (spaces) as commands
        tlast=time.time()
        print eval_str(data)
            
def dbg_print(data):
    if DEBUG: print data

def eval_str(data):
    sum_int = 0
    zwi_int = 0
    history = ['+']
    
    for line in data.split("\n:"):
        for tok in line.split(" "):
            tok=tok.strip("\n")
            if tok=="": continue
            m = re.search(r"(-){0,1}(\d{1,2}):(\d{1,2})",tok)
            if m:
                p=m.groups()
                if p[0]=="-":
                    zwi_int += (int("%s%s"%(p[0],p[1]))+float(p[2])/60)
                if not p[0] or p[0]=="+":
                    zwi_int += (int(p[1])+float(p[2])/60)
                    
                        
            if history[-1]=="+":
                dbg_print( "OP ADD %5s"%repr(zwi_int))
                sum_int +=zwi_int
                zwi_int=0
            elif history[-1]=="-":
                dbg_print( "OP SUB %5s"%repr(zwi_int))
                sum_int -=zwi_int
                zwi_int=0
            else:
                pass
                #data :)

                        
            history.append(tok)
            
    dbg_print( "-------")
    dbg_print( sum_int)
    dbg_print( history )
    return sum_int
                
                
if __name__=="__main__":
    d="""
    -13:24
    +
    6:56
    
    """
    DEBUG=False
    #print eval_str(d)
    print "type \"exit\" to quit shell"
    interactive()