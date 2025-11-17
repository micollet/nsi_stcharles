#module probabilite

def probabilite_evenement(issues_favorables,issues_totales):
    assert issues_totales > 0, "Le nombre total d'issue doit être > 0"
    return(issues_favorables/issues_totales)

def probabilite_A_inter_B(P_A,P_B_sachant_A):
    return P_A*P_B_sachant_A

def probabilite_A_union_B(P_A,P_B_sachant_non_A):
    return P_A + (1-P_A)*P_B_sachant_non_A