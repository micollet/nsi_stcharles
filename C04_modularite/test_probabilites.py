import probabilites


print(probabilites.probabilite_evenement(4,7))



#probabilites de l'enonce
P_X = 0.3
P_nonY_sachant_X = 0.45
P_Y_sachant_nonX = 0.28

P_Y_sachant_X = 1 - P_nonY_sachant_X
P_X_inter_Y = probabilites.probabilite_A_inter_B(P_X,P_Y_sachant_X)
print(P_X_inter_Y)

P_nonX= 1 - P_X
P_nonX_inter_Y = probabilites.probabilite_A_inter_B(P_nonX,P_Y_sachant_nonX)
print(P_nonX_inter_Y)

#probabilites de l'enonce
P_X = 0.3
P_nonY_sachant_X = 0.45
P_Y_sachant_nonX = 0.28

P_X_union_Y = probabilites.probabilite_A_union_B(P_X, P_Y_sachant_nonX)
print(P_X_union_Y)

P_X = 0.3
P_nonY_sachant_X = 0.45
P_Y_sachant_nonX = 0.28

P_nonX= 1 - P_X
P_Y_sachant_X = 1 - P_nonY_sachant_X
P_Y =  probabilites.probabilite_A_inter_B(P_nonX,P_Y_sachant_nonX) + probabilites.probabilite_A_inter_B(P_X,P_Y_sachant_X)

print(P_Y)