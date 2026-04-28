def probability(favorable, total):
    return favorable / total if total != 0 else None

def complement(p):
    return 1 - p

def union(pA, pB, pA_and_B):
    return pA + pB - pA_and_B

def conditional(pA_and_B, pB):
    return pA_and_B / pB if pB != 0 else None

print("1. Basic Probability P(A)")
print("2. Complement P(A')")
print("3. Union P(A ∪ B)")
print("4. Conditional P(A|B)")

choice = int(input("Choose option: "))

if choice == 1:
    f = int(input("Favorable outcomes: "))
    t = int(input("Total outcomes: "))
    print("P(A) =", probability(f, t))

elif choice == 2:
    p = float(input("Enter P(A): "))
    print("P(A') =", complement(p))

elif choice == 3:
    pA = float(input("P(A): "))
    pB = float(input("P(B): "))
    pAB = float(input("P(A ∩ B): "))
    print("P(A ∪ B) =", union(pA, pB, pAB))

elif choice == 4:
    pAB = float(input("P(A ∩ B): "))
    pB = float(input("P(B): "))
    print("P(A|B) =", conditional(pAB, pB))

else:
    print("Invalid choice") 