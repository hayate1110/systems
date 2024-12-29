import random

def ga(N: int, M: int, n: int, N_e: int, P_m: float, P_c: float, teams: dict):
    individuals = []
    N_c = N - N_e
    
    keys = list(teams.keys())
    for i in range(N):
        genes = random.sample(keys, len(keys))
        individuals.append({"genes": genes, "fitness": 0})
    
    for i in range(M):
        elites = []
        children = []

        sum_f = 0
        for individual in individuals:
            individual["fitness"] = f(individual["genes"])
            sum_f += individual["fitness"]

        individuals = sorted(individuals, key=lambda x: x["fitness"], reverse=True)
        
        print(f"{i}世代目:")
        print(f'    遺伝子列={individuals[0]["genes"]}')
        print(f'    適合度={individuals[0]["fitness"]}')
        print(f'    連続出演者数={(1/individuals[0]["fitness"]) - 1}')
        print()

        for j in range(N_e):
            elites.append(individuals[j])
            sum_f -= individuals[j]["fitness"]
    
        for j in range(N_c // 2):
            parent1 = {}
            a = random.random()
            for k in range(N_e, N):
                parent1 = individuals[k]
                p = individual["fitness"] / sum_f
                if a < p:
                    break
                else:
                    a -= p

            parent2 = {}
            a = random.random()
            for k in range(N_e, N):
                parent2 = individuals[k]
                p = individual["fitness"] / sum_f
                if a < p:
                    break
                else:
                    a -= p

            a = random.random()
            if a < P_c:
                split_point = int(random.random() * n)

                parent1_rest = [element for element in parent1["genes"] if element not in parent2["genes"][:split_point]]
                parent2_rest = [element for element in parent2["genes"] if element not in parent1["genes"][:split_point]]
                children.append({"genes": parent1["genes"][:split_point] + parent2_rest, "fitness": 0})
                children.append({"genes": parent2["genes"][:split_point] + parent1_rest, "fitness": 0})
            else:
                children.append(parent1)
                children.append(parent2)

        for j in range(N_c-1):
            for k in range(n):
                a = random.random()
                if a < P_m:
                    index1, index2 = random.sample(range(len(children[j]["genes"])), 2)
                    children[j]["genes"][index1], children[j]["genes"][index2] = children[j]["genes"][index2], children[j]["genes"][index1]

        individuals = children + elites

    return sorted(individuals, key=lambda x: x["fitness"], reverse=True)
            
def f(genes: list):
    total_common_members_count = 0
    for i, (current_team_name, next_team_name) in enumerate(zip(genes, genes[1:])):
        current_team_members = teams[current_team_name]
        next_team_members = teams[next_team_name]
        common_members = current_team_members & next_team_members
        total_common_members_count += len(common_members)

    return 1 / (total_common_members_count + 1)

def show_time_table(genes: list):
    for i, (current_team_name, next_team_name) in enumerate(zip(genes, genes[1:])):
        current_team_members = teams[current_team_name]
        next_team_members = teams[next_team_name]
        common_members = current_team_members & next_team_members

        print(f"{i+1}. {current_team_name}")
        if not common_members == set():
            print(f"    次のショーケースに連続出演する人:")
            for member in common_members:
                print(f"    - {member}")

    print(f"{len(genes)}番目: {genes[-1]}")

def count_common_members(genes):
    total_common_members_count = 0
    for current_team_name, next_team_name in zip(genes, genes[1:]):
        current_team_members = teams[current_team_name]
        next_team_members = teams[next_team_name]
        common_members = current_team_members & next_team_members
        total_common_members_count += len(common_members)
    return total_common_members_count

if __name__ == "__main__":
    teams = {}

    with open("teams.txt", "r") as file:
        line = file.readline()
        while line:
            line = line.strip().split()
            team_name = line[0]
            team_member = set(line[1:])
            teams[team_name] = team_member
            line = file.readline()

    N = 30 # 個体数
    n = len(teams) # 遺伝子数
    M = 1000 # 世代数
    N_e = 3 # エリート個体数
    P_m = 0.005 # 突然変異確率
    P_c = 0.9 # 交配確率

  
    individuals = ga(N, M, n, N_e, P_m, P_c, teams)
    
    for i, individual in enumerate(individuals[:1]):

        print(f"[候補{i+1}]")
        print()
        print(f'連続出演者数={count_common_members(individual["genes"])}')
        show_time_table(individual["genes"])
        print("----------")