A=15
L=0.3
k_string=raw_input("please enter conductivity:(in W/m.K)):")
print("\n ehi you just told me that "+" A= "+str(A)+" L= "+str(L)+" k= " +k_string)
R=L/(float(k_string)*A)
print("\n the resistance will be "+str(R))