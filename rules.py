## Rule 1
## (S, E, M, nil, (E', C', D'))
## ->
## (S, E', M, C', D')

def rule1(S, E, M, C, D):
    if C:
        raise ValueError('Rule 1 cannot be applied')
    (Ep, Cp, Dp) = D
    return (S, Ep, M, Cp, Dp)
