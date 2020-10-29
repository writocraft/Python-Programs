https://l.facebook.com/l.php?u=https%3A%2F%2Fyoutu.be%2Fx084tfX4JnI&h=AT2gLFPQbcNlr2ljUlsqaNCozYpjE9YFCh8o_fysBPR2mEAD6rTxE_ayoY23DFNFfrvSqQ6EktuRm_uORUI8aq9jO_TgtjfoE5BEy00IKwD4fJR2Flx1Deph0pH7MUThbBev_5XAG2xRFnJ5c10f&s=1
def isArmstrong(x): 
      
    n = order(x) 
    temp = x 
    sum1 = 0
      
    while (temp != 0): 
        r = temp % 10
        sum1 = sum1 + power(r, n) 
        temp = temp // 10
  
    # If condition satisfies 
    return (sum1 == x) 
