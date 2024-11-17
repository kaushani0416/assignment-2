from math import comb

def probability_at_least_N(k, N):
    # Total individuals in the k-th generation
    total_individuals = 2**k

    # Probability of a single individual having Aa Bb
    prob_AaBb = 0.25

    # Calculate the probability of having fewer than N individuals with Aa Bb
    prob_fewer_than_N = 0.0
    for i in range(N):
        prob_fewer_than_N += comb(total_individuals, i) * (prob_AaBb**i) * ((1 - prob_AaBb)**(total_individuals - i))

    # Complement probability to get at least N individuals with Aa Bb
    prob_at_least_N = 1 - prob_fewer_than_N

    return prob_at_least_N


if __name__ == "__main__":
    k = int(input("Enter the value of k (generation, k ≤ 7): "))
    N = int(input("Enter the value of N (number of individuals, N ≤ 2^k): "))
    
    result = probability_at_least_N(k, N)
    print(f"The probability that at least {N} individuals have Aa Bb in generation {k} is: {result:.6f}")
