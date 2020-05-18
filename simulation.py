import numpy as np


PROMOTER = "promoter"
DETRACTOR = "detractor"
PASSIVE = "passive"


POSSIBLE_RESPONSES = [PROMOTER, DETRACTOR, PASSIVE]

PROMOTER_PROB = 0.4
DETRACTOR_PROB = 0.3
PASSIVE_PROB = 1 - PROMOTER_PROB - DETRACTOR_PROB

RESPONSE_PROBS = np.array([PROMOTER_PROB, DETRACTOR_PROB, PASSIVE_PROB])


assert np.all(RESPONSE_PROBS >= 0.0)
assert np.isclose(np.sum(RESPONSE_PROBS), 1.0)


SURVEYS_SENT = 10000
RESPONSE_RATE = 0.03
SAMPLE_SIZE = int(SURVEYS_SENT * RESPONSE_RATE)

N_SIMULATIONS = 10000


def get_simulated_nps():

    responses = np.random.choice(POSSIBLE_RESPONSES, p=RESPONSE_PROBS, replace=True, size=SAMPLE_SIZE)

    return np.mean(responses == PROMOTER) - np.mean(responses == DETRACTOR)


nps_simulations = np.array(
    [get_simulated_nps() for _ in range(N_SIMULATIONS)]
)

std_error = np.sqrt((PROMOTER_PROB * (1 - PROMOTER_PROB) + DETRACTOR_PROB * (1 - DETRACTOR_PROB) + 2 * PROMOTER_PROB * DETRACTOR_PROB) / SAMPLE_SIZE)

print(f"mean {np.mean(nps_simulations)} expected value {PROMOTER_PROB - DETRACTOR_PROB}")
print(f"std error from simulations: {np.std(nps_simulations)}")
print(f"std error calculated analytically: {std_error}")



