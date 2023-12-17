# Adjusted genetic algorithm to solve the 8 queens problem with better parameters and methods

def genetic_algorithm(board_size, population_size=500, generations=1000, mutation_rate=0.01):
    def random_board():
        return [random.randint(0, board_size - 1) for _ in range(board_size)]

    def calculate_conflicts(board):
        conflicts = 0
        for i in range(len(board)):
            for j in range(i + 1, len(board)):
                if board[i] == board[j] or abs(board[i] - board[j]) == j - i:
                    conflicts += 1
        return conflicts

    def reproduce(x, y):
        n = len(x)
        c = random.randint(0, n - 1)
        return x[:c] + y[c:]

    def mutate(x):
        n = len(x)
        c = random.randint(0, n - 1)
        m = random.randint(0, n - 1)
        x[c] = m
        return x

    def random_selection(population, fitness):
        population_with_fitness = list(zip(population, fitness))
        total_fitness = sum(fitness)
        selection_probs = [f / total_fitness for _, f in population_with_fitness]
        return population[np.random.choice(len(population), p=selection_probs)]

    # Generate initial population
    population = [random_board() for _ in range(population_size)]
    for generation in range(generations):
        # Calculate the fitness of each individual
        fitness = [1 / (1 + calculate_conflicts(individual)) for individual in population]
        if max(fitness) == 1:
            return population[fitness.index(max(fitness))]
        new_population = []
        for i in range(population_size):
            x = random_selection(population, fitness)
            y = random_selection(population, fitness)
            child = reproduce(x, y)
            if random.random() < mutation_rate:
                child = mutate(child)
            new_population.append(child)
        population = new_population
    return None

# Now let's run the algorithm with the improved parameters
solution = genetic_algorithm(BOARD_SIZE)

# If a solution was found, we can visualize it
if solution:
    # Create a board with the solution
    board = np.zeros((BOARD_SIZE, BOARD_SIZE))
    for i in range(BOARD_SIZE):
        board[solution[i], i] = 1

    # Visualize the solution
    plot_board(board)
else:
    print("No solution was found with the current genetic algorithm parameters.")